# cmake_minimum_required(VERSION 3.10)
# project(org_chart LANGUAGES CXX)

# include(CheckIncludeFileCXX)

# # Check for C++ features
# check_include_file_cxx(any HAS_ANY)
# check_include_file_cxx(string_view HAS_STRING_VIEW)
# check_include_file_cxx(coroutine HAS_COROUTINE)

# # Set C++ version
# if (HAS_ANY AND HAS_STRING_VIEW AND HAS_COROUTINE)
#     set(CMAKE_CXX_STANDARD 20)
# elseif (HAS_ANY AND HAS_STRING_VIEW)
#     set(CMAKE_CXX_STANDARD 17)
# else()
#     set(CMAKE_CXX_STANDARD 14)
# endif()
# set(CMAKE_CXX_STANDARD_REQUIRED ON)
# set(CMAKE_CXX_EXTENSIONS OFF)

# # Enable coverage if using GCC or Clang
# if (CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
#     set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --coverage")
# endif()

# # Main executable
# # add_executable(${PROJECT_NAME} main.cc)

# # ------------------------------------------------------------------------------
# # Include source directories
# aux_source_directory(controllers CTL_SRC)
# aux_source_directory(filters FILTER_SRC)
# aux_source_directory(plugins PLUGIN_SRC)
# aux_source_directory(models MODEL_SRC)
# aux_source_directory(utils UTIL_SRC)

# target_sources(${PROJECT_NAME} PRIVATE
#     ${CTL_SRC}
#     ${FILTER_SRC}
#     ${PLUGIN_SRC}
#     ${MODEL_SRC}
#     ${UTIL_SRC}
# )

# target_include_directories(${PROJECT_NAME} PRIVATE
#     ${CMAKE_CURRENT_SOURCE_DIR}
#     ${CMAKE_CURRENT_SOURCE_DIR}/models
# )

# # ------------------------------------------------------------------------------
# # Third-party dependencies
# # add_subdirectory(third_party/drogon)
# # add_subdirectory(third_party/jwt-cpp)
# # add_subdirectory(third_party/libbcrypt)
# add_subdirectory(third_party/googletest)

# target_link_libraries(${PROJECT_NAME} PRIVATE
#     # drogon
#     # jwt-cpp
#     # bcrypt
# )

# # ------------------------------------------------------------------------------
# # Boost fallback for C++14
# if (CMAKE_CXX_STANDARD LESS 17)
#     find_package(Boost 1.61.0 REQUIRED)
#     target_link_libraries(${PROJECT_NAME} PUBLIC Boost::boost)
# endif()

# # ------------------------------------------------------------------------------
# # Google Test Configuration
# enable_testing()

# file(GLOB TEST_SOURCES "tests/*.cc")

# add_executable(${PROJECT_NAME}_test ${TEST_SOURCES})
# target_include_directories(${PROJECT_NAME}_test PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/models)

# target_link_libraries(${PROJECT_NAME}_test PRIVATE
#     gtest
#     gtest_main
#     pthread
#     drogon
#     jwt-cpp
#     bcrypt
# )

# add_test(NAME AllTests COMMAND ${PROJECT_NAME}_test)

# # ------------------------------------------------------------------------------
# # Uncomment this if needed for dynamic linking of views
# # set_property(TARGET ${PROJECT_NAME} PROPERTY ENABLE_EXPORTS ON)

# cmake_minimum_required(VERSION 3.10)
# project(unit_test_generator LANGUAGES CXX)

# # Set C++ version
# set(CMAKE_CXX_STANDARD 17)
# set(CMAKE_CXX_STANDARD_REQUIRED ON)

# # GoogleTest
# add_subdirectory(third_party/googletest)

# # Add model sources
# file(GLOB MODEL_SOURCES "models/*.cc")
# file(GLOB TEST_SOURCES "tests/*.cc")

# # Add test target only (we're skipping the full drogon app for now)
# add_executable(unit_tests ${MODEL_SOURCES} ${TEST_SOURCES})

# target_include_directories(unit_tests PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/models)

# target_link_libraries(unit_tests PRIVATE gtest gtest_main)

# enable_testing()
# add_test(NAME RunAllTests COMMAND unit_tests)


cmake_minimum_required(VERSION 3.10)
project(unit_test_generator LANGUAGES CXX)


set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(third_party/googletest)

# Just compile Dummy model + test
add_executable(unit_tests
    models/Dummy.cc
    tests/test_Dummy.cc
)

target_include_directories(unit_tests PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/models
)

target_link_libraries(unit_tests PRIVATE
    gtest
    gtest_main
)

enable_testing()
add_test(NAME RunAllTests COMMAND unit_tests)
