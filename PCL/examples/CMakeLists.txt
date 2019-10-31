cmake_minimum_required(VERSION 2.6 FATAL_ERROR)
project(MY_GRAND_PROJECT)

add_compile_options(-std=c++14)

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_SOURCE_DIR}/bin)

find_package(PCL 1.7 REQUIRED)

include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})


add_executable(pcd_write src/pcd_write.cpp)
add_executable(pcd_read src/pcd_read.cpp)
add_executable(concatenate_clouds src/concatenate_clouds.cpp)
add_executable(adding_custom_pttype  src/adding_custom_pttype.cpp)
add_executable (openni_grabber src/openni_grabber.cpp)
add_executable (kdtree_search src/kdtree_search.cpp)

target_link_libraries(pcd_write ${PCL_LIBRARIES})
target_link_libraries(pcd_read ${PCL_LIBRARIES})
target_link_libraries(concatenate_clouds ${PCL_LIBRARIES})
target_link_libraries(adding_custom_pttype ${PCL_LIBRARIES})
target_link_libraries (openni_grabber ${PCL_LIBRARIES})
target_link_libraries (kdtree_search ${PCL_LIBRARIES})
