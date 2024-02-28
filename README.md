### ROS2-Iron 

Go to $Home directory

Install Python3.5 alongside your current Python3 version:
```
    cd

    mkdir python3_5_7

    wget https://www.python.org/ftp/python/3.5.7/Python-3.5.7.tgz

    tar zxvf Python-3.5.7.tgz

    cd Python-3.5.7

    ./configure --enable-shared --enable-optimizations

    make

    sudo make altinstall

    sudo ldconfig
```
Go back to the $Home

Clone the main installation files from https://github.com/novelda/Legacy-SW.git

Go to ModuleConnector/ModuleConnector-unix-1/python35-x86_64-linux-gnu

Install the setup.py
```
python3 setup.py install
```

Clone the provided X4M300_ROS2 git to $Home. 

Either use the cloned X4M300_ROS2 itself as the workspace or rename it:: uwb_ws

Go to the 'uwb_ws/support' directory and install both .deb files (use 'software install').

Now, build the ros2 packages.

```
colcon build
```

*** An issue arises if you are not in the ws named: 'uwb_ws'. In that case either rename or delete the entire 'build' folder and rebuild.

If everything went fine, connect the UWB radar module and find the device ID (e.g. /dev/ttyACM0 [default])

If not the [default] dev ID, go to the /home/arms/uwb_ws/src/novelda_x4m300/launch and edit the line#9 to the new device ID.

Rebuild the workspace.

Now you may run the launch file:

```
ros2 launch novelda_x4m300 uwblaunch.py 
```
