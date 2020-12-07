include(GoogleTest)

# =============================
# Generate C++ bindings
# =============================
set(includeDir ${CMAKE_CURRENT_BINARY_DIR}/include)
set(includeDirCppRust ${includeDir}/cpprust)
set(includeDirRust ${includeDir}/rust)
set(bridgeFile ${CMAKE_CURRENT_LIST_DIR}/src/bridge.rs)
find_program(cxxBridge cxxbridge REQUIRED PATHS $ENV{HOME}/.cargo/bin)

add_custom_command(
  OUTPUT ${includeDirCppRust}/cpprust.hpp
  DEPENDS ${bridgeFile}
  COMMAND ${cxxBridge} ${bridgeFile} --header --output
          ${includeDirCppRust}/cpprust.hpp
  WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})

add_custom_command(
  OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/cpprust.cpp
  DEPENDS ${bridgeFile}
  COMMAND ${cxxBridge} ${bridgeFile} --output
          ${CMAKE_CURRENT_BINARY_DIR}/cpprust.cpp
  WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})

add_custom_command(
  OUTPUT ${includeDirRust}/cxx.hpp
  COMMAND ${cxxBridge} --header --output ${includeDirRust}/cxx.hpp
  WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})

# =============================
# Compile generated C++ code
# =============================
add_library(
  CppRust_cpprust_cpp_gen STATIC
  ${includeDirRust}/cxx.hpp ${includeDirCppRust}/cpprust.hpp
  ${CMAKE_CURRENT_BINARY_DIR}/cpprust.cpp)
add_library(CppRust::cpprust::cpp_gen ALIAS CppRust_cpprust_cpp_gen)
target_include_directories(
  CppRust_cpprust_cpp_gen PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/include
                                 ${CMAKE_CURRENT_LIST_DIR}/..)

# =============================
# Combine C++ and Rust parts
# =============================
add_library(CppRust_cpprust STATIC src/blobstore.cpp)
target_include_directories(
  CppRust_cpprust PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/include
                         ${CMAKE_CURRENT_LIST_DIR}/..)

set(cargoTargetDir ${CMAKE_CURRENT_BINARY_DIR}/rust)
add_custom_command(
  TARGET CppRust_cpprust
  PRE_LINK
  BYPRODUCTS ${cargoTargetDir}/debug/libcpprust.a
  COMMAND CARGO_TARGET_DIR=${CMAKE_CURRENT_BINARY_DIR}/rust cargo build
  WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})
add_custom_command(
  TARGET CppRust_cpprust
  PRE_LINK
  BYPRODUCTS ${cargoTargetDir}/release/libcpprust.a
  COMMAND CARGO_TARGET_DIR=${CMAKE_CURRENT_BINARY_DIR}/rust cargo build --release
  WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries(
  CppRust_cpprust
  PUBLIC CppRust::cpprust::cpp_gen debug
         ${cargoTargetDir}/debug/libcpprust.a optimized
         ${cargoTargetDir}/release/libcpprust.a)

# =============================
# Testing
# =============================
add_executable(CppRust_cpprust_cpp_test src/blobstore_test.cpp)
target_include_directories(CppRust_cpprust_cpp_test PRIVATE ${CMAKE_CURRENT_LIST_DIR}/include ${includeDir})
target_link_libraries(CppRust_cpprust_cpp_test gtest_main CppRust_cpprust)
gtest_discover_tests(CppRust_cpprust_cpp_test)

add_test(NAME RustTestDebug
         COMMAND cargo test
         CONFIGURATIONS Debug ""
         WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})

add_test(NAME RustTestRelease
         COMMAND cargo test --release
         CONFIGURATIONS Release RelWithDebInfo
         WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})
set_tests_properties(RustTestDebug RustTestRelease PROPERTIES ENVIRONMENT "CARGO_TARGET_DIR=${cargoTargetDir}")
