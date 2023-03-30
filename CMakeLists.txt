cmake_minimum_required(VERSION 3.8)
project(husky_teleop)

set(CMAKE_BUILD_TYPE "Release")

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch
    DESTINATION share/${PROJECT_NAME})

install(DIRECTORY config
    DESTINATION share/${PROJECT_NAME})

ament_package()
