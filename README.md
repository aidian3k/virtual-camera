# Computer graphics final project
This repository shows my final project of Computer Graphics course conducted at Warsaw University of technology. The project is strictly connected to computer 
graphics and the main purpose of it is to create virtual camera which would enable user to go forward, left, back, right, zoom, and looking in every axis. To show
the idea I used four identicall cubes in the form of city between which the user can move. To accomplish the idea I stored the camera position and updated it on every
move of the user. Then by using projection matrix and view_matrix I projected the points into the 2D user world. 

The application used following technologies:
- Python - main language for creating application
- Pygame - library for drawing cubes and handling keyboard actions
- Numpy/Pyrr - libraries for mathematical aspects of the application

# How to run the application
To run the application you must have Python installed. If you have python, type in make in the main root of the project to install required dependencies for the project. Then go to the
src directory and run the application by typing python3 main.py.

# Controls

## Moving around
<table>
  <tr>
    <th>Movement</th>
    <td>Forward</td>
    <td>Backward</td>
    <td>Left</td>
    <td>Right</td>
  </tr>
  <tr>
    <th>Key</th>
    <td>W</td>
    <td>S</td>
    <td>A</td>
    <td>D</td>
  </tr>
</table>

## Looking around
<table>
  <tr>
    <th>Movement</th>
    <td>Up</td>
    <td>Down</td>
    <td>Left</td>
    <td>Right</td>
  </tr>
  <tr>
    <th>Key</th>
    <td>I</td>
    <td>K</td>
    <td>J</td>
    <td>L</td>
  </tr>
</table>

## Zooming and restarting program
## Looking around
<table>
  <tr>
    <th>Movement</th>
    <td>Zomm up</td>
    <td>Zoom down</td>
    <td>Reset</td>
  </tr>
  <tr>
    <th>Key</th>
    <td>+</td>
    <td>-</td>
    <td>SPACE</td>
  </tr>
</table>

## Some films of the application

### 1 - Presentation of the functionalities without BSP hidden surface elimination
https://github.com/aidian3k/virtual-camera/assets/93425971/71bd3176-2141-4d22-a333-567c2e614091

### 2 - Presentation of functionalities with BSP hidden surface elimination
https://github.com/aidian3k/virtual-camera/assets/93425971/7f69658d-67f3-48fc-b38d-09f823086e8d






