# =============================
# Preamble
# =============================
cmake_minimum_required(VERSION 3.12)
project(
  CppRust
  VERSION 0.1.0
  DESCRIPTION "C++ Rust Playground"
  LANGUAGES CXX)
enable_testing()

# =============================
# Project wide setup
# =============================
option(CPP_RUST_ENABLE_WERROR "Enable all warnings as errors" ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON) # improve Intellisense
set_property(GLOBAL PROPERTY USE_FOLDERS ON) # use folders in IDEs

# Restrict valid build types for non-multi-config generators, e.g. cannot
# accidently use build type 'Dbg' with Ninja.
get_property(isMultiConfig GLOBAL PROPERTY GENERATOR_IS_MULTI_CONFIG)
if(NOT isMultiConfig)
  set(allowableBuildTypes Debug Release RelWithDebInfo)
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "${allowableBuildTypes}")
  if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE
        Debug
        CACHE STRING "" FORCE)
  elseif(NOT CMAKE_BUILD_TYPE IN_LIST allowableBuildTypes)
    message(FATAL_ERROR "Invalid build type: ${CMAKE_BUILD_TYPE}")
  endif()
endif()

if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
  add_compile_options(-fdiagnostics-color=always)
elseif("${CMAKE_CXX_COMPILER_ID}" MATCHES "Clang")
  add_compile_options(-fcolor-diagnostics)
endif()

# =============================
# Externally provided content
# =============================
add_subdirectory(external)

# =============================
# Main targets built by this project
# =============================
add_subdirectory(libs)

# =============================
# Custom targets
# =============================
add_custom_target(
  run
  COMMAND CppRust_main
  DEPENDS CppRust_main)
