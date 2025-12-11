import pytest

from src.main import Rover


def test_get_rover_point():
    rover = Rover()
    assert rover.get_rover_point() == [5, 12, "N"]

def test_set_rover_forward_command():
    rover = Rover()
    rover.set_rover_commands(["FORWARD"]) 
    assert rover.get_rover_point() == [5, 13, "N"]

def test_set_rover_commands():
    rover = Rover()
    rover.set_rover_commands(["FORWARD", "L", "BACKWARD", "BACKWARD"])
    assert rover.get_rover_point() == [3, 13, "W"]

