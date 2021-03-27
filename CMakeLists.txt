cmake_minimum_required(VERSION 2.8.12 FATAL_ERROR)

project(dena_library)

add_library(${PROJECT_NAME})

## compile
target_sources(${PROJECT_NAME}
PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include/dena.h
PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/src/dena.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/src/dena_internal.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/src/dena_internal.h
)

target_include_directories(${PROJECT_NAME}
PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/src
)

## link
find_package(Poco)
if(TARGET Poco::Poco)
    target_link_libraries(${PROJECT_NAME} PRIVATE Poco::Poco)
endif()

## install
install(TARGETS ${PROJECT_NAME} DESTINATION lib)
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/include/dena.h DESTINATION include)