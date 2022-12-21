cmake_minimum_required(VERSION 2.8)
project(libwriter)

set(CMAKE_CXX_STANDARD 11)

add_definitions(-std=c++11)
add_definitions("-Wall")
add_compile_options(-fPIC)
add_compile_options(-c)
add_library(writer_sttc STATIC libwriter_api.cpp libwriter_api.h)
add_library(writer_dymc SHARED libwriter_api.cpp libwriter_api.h)