cmake_minimum_required(VERSION 2.8.12 FATAL_ERROR)

include(GenerateExportHeader)
include(GNUInstallDirs)

project(dena_library)

add_library(${PROJECT_NAME})
generate_export_header(${PROJECT_NAME}
    BASE_NAME dena
)

## compile
target_sources(${PROJECT_NAME}
    PUBLIC
        ./include/dena.h
    PRIVATE
        ./src/dena.cc
        ./src/dena_internal.cc
        ./src/dena_internal.h
)

target_include_directories(${PROJECT_NAME}
    PUBLIC
        ${CMAKE_CURRENT_BINARY_DIR}
        ./include
    PRIVATE
        ./src
)

## link
find_package(Poco)
if(TARGET Poco::Poco)
    target_link_libraries(${PROJECT_NAME} PRIVATE Poco::Poco)
endif()

## install
install(TARGETS ${PROJECT_NAME}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

install(
    DIRECTORY ./include/
    TYPE INCLUDE
    FILES_MATCHING
        PATTERN "*.h"
        PATTERN "*.hh"
        PATTERN "*.hpp"
)
install(
    FILES ${CMAKE_CURRENT_BINARY_DIR}/dena_export.h
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)