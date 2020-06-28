find_package(Threads)

set(cPlaygroundSources base/test_main.c endian.c move_last.c signal.c
                       test_suites.h)

add_executable(cPlaygroundTests ${cPlaygroundSources})
target_compile_options(cPlaygroundTests PRIVATE ${C_PLAYGROUND_C_FLAGS_COMMON})

if(UNIX AND NOT APPLE)
  target_compile_definitions(cPlaygroundTests PUBLIC _GNU_SOURCE)
endif()

include(FetchContent)
FetchContent_GetProperties(check)
target_include_directories(
  cPlaygroundTests PRIVATE ${PROJECT_SOURCE_DIR}/src ${check_BINARY_DIR}
                           ${check_BINARY_DIR}/src)

target_link_libraries(cPlaygroundTests check Threads::Threads)

# =============================
# Custom targets
# =============================

set(cPlaygroundFullPathSources ${cPlaygroundSources})
list(TRANSFORM cPlaygroundFullPathSources PREPEND ${CMAKE_CURRENT_SOURCE_DIR}/)

find_program(CLANG_FORMAT "clang-format")
if(CLANG_FORMAT)
  add_custom_target(fmt COMMAND ${CLANG_FORMAT} -i -style=file
                                ${cPlaygroundFullPathSources})
endif()
