# =============================
# Preamble
# =============================
cmake_minimum_required(VERSION 3.12)
project(
  cPlayground
  VERSION 0.1.0
  DESCRIPTION "C Playground"
  LANGUAGES C)

# =============================
# Project-wide setup
# =============================
option(C_PLAYGROUND_USE_VALGRIND "Run tests with Valgrind" OFF)
option(C_PLAYROUND_ENABLE_WERROR "Enable all warnings as errors" ON)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_LIST_DIR}/cmake)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED YES)
set(CMAKE_C_EXTENSIONS NO) # Enable GNU and POSIX extensions

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

if("${CMAKE_C_COMPILER_ID}" STREQUAL "GNU")
  add_compile_options(-fdiagnostics-color=always)
elseif("${CMAKE_C_COMPILER_ID}" MATCHES "Clang")
  add_compile_options(-fcolor-diagnostics)
endif()

set(C_PLAYGROUND_C_FLAGS_COMMON -Wall -Wextra -Werror -Wunreachable-code
                                -Wformat=2 -DUNIX)
if(C_PLAYGROUND_ENABLE_WERROR)
  list(APPEND C_PLAYGROUND_C_FLAGS_COMMON -Werror)
endif()

# =============================
# Externally provided content
# =============================
add_subdirectory(dependencies)

# =============================
# Main targets built by this project
# =============================
add_subdirectory(src)

if(C_PLAYGROUND_USE_VALGRIND)
  add_custom_target(
    runTests
    COMMAND CK_FORK=no valgrind --error-exitcode=1 --leak-check=full
            $<TARGET_FILE:cPlaygroundTests>
    DEPENDS cPlaygroundTests)
else()
  add_custom_target(
    runTests
    COMMAND cPlaygroundTests
    DEPENDS cPlaygroundTests)
endif()
