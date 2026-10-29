# Stand-alone test for the vecgeom package: build against the installed VecGeom
# CMake package, which provides the include paths and compile definitions.
cmake_minimum_required(VERSION 3.16)
project(test_vecgeom LANGUAGES CXX)

find_package(VecGeom REQUIRED)

add_executable(test_vecgeom test_vecgeom.cpp)
target_link_libraries(test_vecgeom PRIVATE VecGeom::vecgeom)
