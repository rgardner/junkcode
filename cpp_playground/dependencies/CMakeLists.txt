include(FetchContent)

fetchcontent_declare(GSL
                     GIT_REPOSITORY
                     https://github.com/microsoft/GSL.git
                     GIT_TAG
                     02d1051fddbb9a1d43b61c2970ec383a65ca58f4)

fetchcontent_declare(Catch2
                     GIT_REPOSITORY
                     https://github.com/catchorg/Catch2.git
                     GIT_TAG
                     2c869e17e4803d30b3d5ca5b0d76387b9db97fa5 # v2.9.2
                     )

fetchcontent_getproperties(GSL)
if(NOT gsl_POPULATED)
  fetchcontent_populate(gsl)
  add_subdirectory(${gsl_SOURCE_DIR} ${gsl_BINARY_DIR})
endif()

fetchcontent_getproperties(Catch2)
if(NOT catch2_POPULATED)
  fetchcontent_populate(catch2)
  add_subdirectory(${catch2_SOURCE_DIR} ${catch2_BINARY_DIR})
endif()
