# Summit XL Autonomous
 
This repository contains two packages that work independently.

## Summit XL Tools

This package contains two tools to move the robot in case the remote control runs out of battery.

### Interactive Marker

Open rviz and allow to move the robot using the graphic interface of interactive markers. To make it work you need to install the package [interactive_marker_twist_server](http://wiki.ros.org/interactive_marker_twist_server)

```
roslaunch summit_xl_tools interactive_marker.launch`
```

### Teleop Keyboard

Allows to move the robot using the keyboard. To work you must have installed the package [teleop_twist_keyboard](http://wiki.ros.org/teleop_twist_keyboard)

```
roslaunch summit_xl_tools teleop_keyboard.launch
```

## Summit XL GPS

This package is an implementation of the [robot localization package](http://wiki.ros.org/robot_localization).

To launch all the files needed to use:

```
roslaunch summit_xl_gps summit_xl_nav.launch
```

The above command executes the following:

- Convertion from depthimage to laserscan (necessary package [depthimage_to_laserscan](http://wiki.ros.org/depthimage_to_laserscan))
- Map Server
- Move Base
- Robot Localization

To send the GPS destination point make sure that the gps receiver is working in RTK mode, this can be seen by looking at the covariance matrix in the gps topic `rostopic echo /robot/gps/fix`, must show covariances less than 0.002 equivalent to a precision of approximately 4 cm.

Open the file `gps_mission.py` in `summit_xl_gps/scripts`, set the origin point (must be the gps cordinate where the odometry started) in the varible `olat` and `olot`.

For the conversion of latitude to longitude to work you must install the package [geonav_transform](http://wiki.ros.org/geonav_transform)

