cmake_minimum_required(VERSION 2.8.12 FATAL_ERROR)

include(GenerateExportHeader)
include(GNUInstallDirs)

project(mylibrary)

add_library(${PROJECT_NAME})
generate_export_header(${PROJECT_NAME}
    BASE_NAME mylibrary
)

## compile
target_sources(${PROJECT_NAME}
    PUBLIC
        ./include/mylibrary.h
    PRIVATE
        ./src/mylibrary.cc
        ./src/mylibrary_internal.cc
        ./src/mylibrary_internal.h
)

target_include_directories(${PROJECT_NAME}
    PUBLIC
        ${CMAKE_CURRENT_BINARY_DIR}
        ./include
    PRIVATE
        ./src
)

## link
find_package(Boost)
if(TARGET Boost::Boost)
    target_link_libraries(${PROJECT_NAME} PRIVATE Boost::Boost)
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
    FILES ${CMAKE_CURRENT_BINARY_DIR}/mylibrary_export.h
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)
