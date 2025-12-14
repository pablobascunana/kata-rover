import pytest

from src.main import Rover


def test_get_rover_point():
    rover = Rover()
    assert rover.get_rover_point() == [5, 12, "N"]

def test_rover_initialization_with_custom_position():
    rover = Rover(x=0, y=0, direction="N")
    assert rover.get_rover_point() == [0, 0, "N"]

def test_rover_initialization_with_custom_position_and_direction():
    rover = Rover(x=10, y=5, direction="E")
    assert rover.get_rover_point() == [10, 5, "E"]

def test_rover_initialization_with_all_directions():
    rover_n = Rover(x=0, y=0, direction="N")
    assert rover_n.get_rover_point() == [0, 0, "N"]
    
    rover_s = Rover(x=0, y=0, direction="S")
    assert rover_s.get_rover_point() == [0, 0, "S"]
    
    rover_e = Rover(x=0, y=0, direction="E")
    assert rover_e.get_rover_point() == [0, 0, "E"]
    
    rover_w = Rover(x=0, y=0, direction="W")
    assert rover_w.get_rover_point() == [0, 0, "W"]

def test_rover_initialization_with_custom_params_and_grid_size():
    rover = Rover(x=3, y=7, direction="S", grid_size=10)
    assert rover.get_rover_point() == [3, 7, "S"]
    assert rover.grid_size == 10

def test_rover_initialization_with_custom_params_and_obstacles():
    rover = Rover(x=1, y=1, direction="N", obstacles=[(2, 2), (3, 3)])
    assert rover.get_rover_point() == [1, 1, "N"]
    assert rover.obstacles == [(2, 2), (3, 3)]

def test_move_forward_north():
    rover = Rover()
    rover.set_rover_commands(["FORWARD"]) 
    assert rover.get_rover_point() == [5, 13, "N"]

def test_move_forward_south():
    rover = Rover()
    rover.update_rover_point([5, 12, "S"])
    rover.set_rover_commands(["FORWARD"])
    assert rover.get_rover_point() == [5, 11, "S"]

def test_move_forward_east():
    rover = Rover()
    rover.update_rover_point([5, 12, "E"])
    rover.set_rover_commands(["FORWARD"])
    assert rover.get_rover_point() == [6, 12, "E"]

def test_move_forward_west():
    rover = Rover()
    rover.update_rover_point([5, 12, "W"])
    rover.set_rover_commands(["FORWARD"])
    assert rover.get_rover_point() == [4, 12, "W"]

def test_move_backward_north():
    rover = Rover()
    rover.update_rover_point([5, 12, "N"])
    rover.set_rover_commands(["BACKWARD"])
    assert rover.get_rover_point() == [5, 11, "N"]

def test_move_backward_south():
    rover = Rover()
    rover.update_rover_point([5, 12, "S"])
    rover.set_rover_commands(["BACKWARD"])
    assert rover.get_rover_point() == [5, 13, "S"]

def test_move_backward_east():
    rover = Rover()
    rover.update_rover_point([5, 12, "E"])
    rover.set_rover_commands(["BACKWARD"])
    assert rover.get_rover_point() == [4, 12, "E"]

def test_move_backward_west():
    rover = Rover()
    rover.update_rover_point([5, 12, "W"])
    rover.set_rover_commands(["BACKWARD"])
    assert rover.get_rover_point() == [6, 12, "W"]

def test_rotate_left_from_north():
    rover = Rover()
    rover.update_rover_point([5, 12, "N"])
    rover.set_rover_commands(["L"])
    assert rover.get_rover_point() == [5, 12, "W"]

def test_rotate_left_from_west():
    rover = Rover()
    rover.update_rover_point([5, 12, "W"])
    rover.set_rover_commands(["L"])
    assert rover.get_rover_point() == [5, 12, "S"]

def test_rotate_left_from_south():
    rover = Rover()
    rover.update_rover_point([5, 12, "S"])
    rover.set_rover_commands(["L"])
    assert rover.get_rover_point() == [5, 12, "E"]

def test_rotate_left_from_east():
    rover = Rover()
    rover.update_rover_point([5, 12, "E"])
    rover.set_rover_commands(["L"])
    assert rover.get_rover_point() == [5, 12, "N"]

def test_rotate_right_from_north():
    rover = Rover()
    rover.update_rover_point([5, 12, "N"])
    rover.set_rover_commands(["R"])
    assert rover.get_rover_point() == [5, 12, "E"]

def test_rotate_right_from_east():
    rover = Rover()
    rover.update_rover_point([5, 12, "E"])
    rover.set_rover_commands(["R"])
    assert rover.get_rover_point() == [5, 12, "S"]

def test_rotate_right_from_south():
    rover = Rover()
    rover.update_rover_point([5, 12, "S"])
    rover.set_rover_commands(["R"])
    assert rover.get_rover_point() == [5, 12, "W"]

def test_rotate_right_from_west():
    rover = Rover()
    rover.update_rover_point([5, 12, "W"])
    rover.set_rover_commands(["R"])
    assert rover.get_rover_point() == [5, 12, "N"]

def test_wrapping_east_edge():
    rover = Rover(grid_size=10)
    rover.update_rover_point([9, 0, "E"])
    rover.set_rover_commands(["FORWARD"])
    assert rover.get_rover_point() == [0, 0, "E"]

def test_wrapping_west_edge():
    rover = Rover(grid_size=10)
    rover.update_rover_point([0, 0, "W"])
    rover.set_rover_commands(["FORWARD"])
    assert rover.get_rover_point() == [9, 0, "W"]

def test_wrapping_north_edge():
    rover = Rover(grid_size=10)
    rover.update_rover_point([0, 9, "N"])
    rover.set_rover_commands(["FORWARD"])
    assert rover.get_rover_point() == [0, 0, "N"]

def test_wrapping_south_edge():
    rover = Rover(grid_size=10)
    rover.update_rover_point([0, 0, "S"])
    rover.set_rover_commands(["FORWARD"])
    assert rover.get_rover_point() == [0, 9, "S"]

def test_wrapping_backward_east():
    rover = Rover(grid_size=10)
    rover.update_rover_point([0, 0, "E"])
    rover.set_rover_commands(["BACKWARD"])
    assert rover.get_rover_point() == [9, 0, "E"]

def test_wrapping_backward_west():
    rover = Rover(grid_size=10)
    rover.update_rover_point([9, 0, "W"])
    rover.set_rover_commands(["BACKWARD"])
    assert rover.get_rover_point() == [0, 0, "W"]

def test_obstacle_detected_forward_north():
    rover = Rover(obstacles=[(0, 1)])
    rover.update_rover_point([0, 0, "N"])
    rover.set_rover_commands(["FORWARD"])
    assert rover.get_rover_point() == [0, 0, "N"]

def test_obstacle_detected_forward_south():
    rover = Rover(obstacles=[(0, 0)])
    rover.update_rover_point([0, 1, "S"])
    rover.set_rover_commands(["FORWARD"])
    assert rover.get_rover_point() == [0, 1, "S"]

def test_obstacle_detected_forward_east():
    rover = Rover(obstacles=[(1, 0)])
    rover.update_rover_point([0, 0, "E"])
    rover.set_rover_commands(["FORWARD"])
    assert rover.get_rover_point() == [0, 0, "E"]

def test_obstacle_detected_forward_west():
    rover = Rover(obstacles=[(0, 0)])
    rover.update_rover_point([1, 0, "W"])
    rover.set_rover_commands(["FORWARD"])
    assert rover.get_rover_point() == [1, 0, "W"]

def test_obstacle_detected_backward_north():
    rover = Rover(obstacles=[(0, 0)])
    rover.update_rover_point([0, 1, "N"])
    rover.set_rover_commands(["BACKWARD"])
    assert rover.get_rover_point() == [0, 1, "N"]

def test_no_obstacle_moves_normally():
    rover = Rover(obstacles=[(5, 5)])
    rover.update_rover_point([0, 0, "N"])
    rover.set_rover_commands(["FORWARD"])
    assert rover.get_rover_point() == [0, 1, "N"]

def test_obstacle_reported_in_sequence():
    rover = Rover(obstacles=[(0, 2)])
    rover.update_rover_point([0, 0, "N"])
    result = rover.set_rover_commands(["FORWARD", "FORWARD", "FORWARD"])
    assert rover.get_rover_point() == [0, 1, "N"]
    assert result == {"obstacle": (0, 2)}

def test_obstacle_reported_stops_execution():
    rover = Rover(obstacles=[(2, 0)])
    rover.update_rover_point([0, 0, "E"])
    result = rover.set_rover_commands(["FORWARD", "FORWARD", "FORWARD", "FORWARD"])
    assert rover.get_rover_point() == [1, 0, "E"]
    assert result == {"obstacle": (2, 0)}

def test_no_obstacle_returns_none():
    rover = Rover(obstacles=[(5, 5)])
    rover.update_rover_point([0, 0, "N"])
    result = rover.set_rover_commands(["FORWARD", "FORWARD"])
    assert rover.get_rover_point() == [0, 2, "N"]
    assert result is None

def test_obstacle_with_rotation_before():
    rover = Rover(obstacles=[(1, 0)])
    rover.update_rover_point([0, 0, "N"])
    result = rover.set_rover_commands(["R", "FORWARD", "FORWARD"])
    assert rover.get_rover_point() == [0, 0, "E"]
    assert result == {"obstacle": (1, 0)}

def test_invalid_command_ignored():
    rover = Rover(x=0, y=0, direction="N")
    rover.set_rover_commands(["FORWARD", "INVALID", "FORWARD"])
    assert rover.get_rover_point() == [0, 2, "N"]

def test_invalid_direction_raises_error():
    with pytest.raises(ValueError):
        Rover(x=0, y=0, direction="X")

def test_initial_position_on_obstacle_raises_error():
    with pytest.raises(ValueError):
        Rover(x=0, y=0, direction="N", obstacles=[(0, 0)])

def test_initial_position_on_obstacle_with_wrapping():
    with pytest.raises(ValueError):
        Rover(x=0, y=0, direction="N", grid_size=10, obstacles=[(0, 0)])

def test_negative_coordinates_allowed():
    rover = Rover(x=-1, y=-2, direction="N")
    assert rover.get_rover_point() == [-1, -2, "N"]

def test_empty_commands_list():
    rover = Rover(x=0, y=0, direction="N")
    result = rover.set_rover_commands([])
    assert rover.get_rover_point() == [0, 0, "N"]
    assert result is None

def test_set_rover_commands():
    rover = Rover()
    rover.set_rover_commands(["FORWARD", "L", "BACKWARD", "BACKWARD"])
    assert rover.get_rover_point() == [7, 13, "W"]

def test_set_rover_commands_2():
    rover = Rover()
    rover.set_rover_commands(["FORWARD", "L", "FORWARD", "R", "BACKWARD", "BACKWARD"])
    assert rover.get_rover_point() == [4, 11, "N"]

def test_set_rover_commands_2():
    rover = Rover()
    rover.set_rover_commands(["FORWARD", "L", "FORWARD", "BACKWARD", "BACKWARD", "L", "L", "FORWARD", "R", "R", "BACKWARD"])
    assert rover.get_rover_point() == [8, 13, "W"]
