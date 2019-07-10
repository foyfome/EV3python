#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Play a sound
brick.sound.beeps(5)
# Play one of the built-in sounds
brick.sound.file(SoundFile.HELLO, 100)

# Make the light red
brick.light(Color.RED)

# Clear the display
brick.display.clear()
# Print "Hello" near the middle of the screen
brick.display.text("Hello", (60, 50))
# Print "World" directyl underneath it
brick.display.text("World")

# Show a built-in image of two eyes looking upward
brick.display.image(ImageFile.UP)

# Initialize a motor at port B
test_motor = Motor(Port.B)

# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
test_motor.run_target(500, 360)

# Play another beep sound
# This time with a higher pitch (1000 Hz) and longer duration (500 ms)
brick.sound.beep(1000, 500)