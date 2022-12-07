# Sample ROS python package

## Package structure
```
sample_pkg
 |- launch/
    |- sample_launch_file.launch
 |- scripts/
    |- sample_ros_node.py
 |- rviz/
    |- cfg.rviz
 |- src/
    |- sample_python_module/
      |- __init__.py
      |- main.py
      |- sample_class.py
      |- python_sub_module/
        |- __init__.py
        |- sub_class.py
 - CMakeLists.txt
 - LICENSE
 - package.xml
 - README.md
 - setup.py
```
*Note that **standard convention is to name the Python module the same as the ROS package name**. They are named differently here for clarity.*


## Notes
1. Place python nodes in the `scripts/` folder.
1. Python nodes have to be given execute permisions with chmod
    ```
    chmod +x scripts/sample_ros_node.py
    ```
   - ROS nodes do not need to have the .py extension, just need to include the shebang in the first line.
1. Place python modules and submodules under `src/` folder.
   - Python requires each module to have an `__init__.py` file.
2. Naming conventions
   - Standard convention is to name the Python module the same as the ROS package name.
      - *Note that in this package, the ROS package name and Python module names are named differently for clarity.*
   - ROS node name should be the same as the script name.
3. Any rviz files can be stored in the `rviz/` folder.

## Running nodes
```
rosrun sample_pkg sample_ros_node
```
or 
```
roslaunch sample_pkg sample_launch_file.launch
```


## References:
1. [ROS PyStyleGuide](http://wiki.ros.org/PyStyleGuide)
2. [ROS docs (Jade)](http://docs.ros.org/en/jade/api/catkin/html/howto/format2/installing_python.html)
3. [Understanding how python sources python modules](http://www.artificialhumancompanions.com/structure-python-based-ros-package/#:~:text=Python%2Dbased%20ROS%20packages%20will,it%20isn't%20already%20running.)


