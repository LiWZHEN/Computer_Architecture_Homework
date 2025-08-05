cmake_minimum_required(VERSION 3.20)

project(Homework)

add_library(shared_lib SHARED IMPORTED)
set_target_properties(shared_lib PROPERTIES
  IMPORTED_LOCATION "${CMAKE_SOURCE_DIR}/third_party/lib/shared_lib.so"
  INTERFACE_INCLUDE_DIRECTORIES "${CMAKE_SOURCE_DIR}/third_party/include"
)

add_executable(main src/main.cpp)
target_link_libraries(main shared_lib)
  