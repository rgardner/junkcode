# =============================
# Define targets
# =============================
set(cppPlaygroundSources base/main.cpp async.cpp validate_parens.cpp)

add_executable(CppPlayground_main ${cppPlaygroundSources})
add_executable(CppPlayground::main ALIAS CppPlayground_main)

include(FetchContent)
fetchcontent_getproperties(GSL)
fetchcontent_getproperties(Catch2)
target_include_directories(CppPlayground_main
                           PUBLIC ${gsl_SOURCE_DIR}/include
                                  ${catch2_SOURCE_DIR}/single_include
                                  ${CMAKE_CURRENT_LIST_DIR})

if(MSVC)
  target_compile_options(CppPlayground_main
                         PRIVATE /W4 # provides lint-like warnings
                                 /permissive- # specify standards conformance
                         )
  if(INTERVIEW_PREP_ENABLE_WERROR)
    target_compile_options(CppPlayground_main PRIVATE /WX)
  endif()
else()
  target_compile_options(CppPlayground_main
                         PRIVATE -Wall -Wextra
                                 #
                                 -Wdouble-promotion # warn if float is implicit
                                                    # promoted to double
                                 -Wnon-virtual-dtor # warn the user if a class
                                                    # with virtual functions has
                                                    # a non- virtual destructor.
                                                    # This helps catch hard to
                                                    # track down memory errors
                                 -Wnull-dereference # warn if a null dereference
                                                    # is detected
                                 -Wold-style-cast # warn for c-style casts
                                 -Woverloaded-virtual # warn if you overload
                                                      # (not override) a virtual
                                                      # function
                                 -Wpedantic # warn if non-standard C++ is used
                                 -Wunused # warn on anything being unused
                         )
  if(INTERVIEW_PREP_ENABLE_WERROR)
    target_compile_options(CppPlayground_main PRIVATE -Werror)
  endif()
endif()

target_link_libraries(CppPlayground_main PUBLIC Catch2::Catch2)

if(UNIX AND NOT APPLE)
  find_package(Threads REQUIRED)
  target_link_libraries(CppPlayground_main PUBLIC ${CMAKE_THREAD_LIBS_INIT})
endif()

# =============================
# Testing
# =============================

list(APPEND CMAKE_MODULE_PATH "${catch2_SOURCE_DIR}/contrib")
include(Catch)
catch_discover_tests(CppPlayground_main)

# =============================
# Custom targets
# =============================

set(cppPlaygroundFullPathSources ${cppPlaygroundSources})
list(TRANSFORM
     cppPlaygroundFullPathSources
     PREPEND
     ${CMAKE_CURRENT_SOURCE_DIR}/)

find_program(CLANG_FORMAT "clang-format")
if(CLANG_FORMAT)
  add_custom_target(format
                    COMMAND ${CLANG_FORMAT} -i -style=file
                            ${cppPlaygroundFullPathSources})
endif()
