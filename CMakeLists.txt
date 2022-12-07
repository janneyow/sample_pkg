cmake_minimum_required(VERSION 3.0.2)
project(sample_pkg)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
)

catkin_python_setup()


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES sample_pkg
#  CATKIN_DEPENDS roscpp rospy
#  DEPENDS system_lib
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
