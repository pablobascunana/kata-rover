class Rover:

    def __init__(self, x=None, y=None, direction=None, grid_size=None, obstacles=None):
        if x is None:
            x = 5
        if y is None:
            y = 12
        if direction is None:
            direction = "N"
        
        valid_directions = ["N", "S", "E", "W"]
        if direction not in valid_directions:
            raise ValueError(f"Invalid direction: {direction}. Must be one of {valid_directions}")
        
        self.point = [x, y, direction]
        self.grid_size = grid_size
        self.obstacles = obstacles if obstacles is not None else []
        
        if self._has_obstacle(x, y):
            raise ValueError(f"Initial position ({x}, {y}) is on an obstacle")

    def get_rover_point(self):
        return self.point

    def _apply_wrapping(self):
        if self.grid_size is not None:
            self.point[0] = self.point[0] % self.grid_size
            self.point[1] = self.point[1] % self.grid_size

    def _has_obstacle(self, x, y):
        if self.grid_size is not None:
            x = x % self.grid_size
            y = y % self.grid_size
        return (x, y) in self.obstacles

    def set_rover_commands(self, commands):

        for command in commands:
            if "FORWARD" == command:
                new_x = self.point[0]
                new_y = self.point[1]
                if self.point[2] == "N":
                    new_y += 1
                elif self.point[2] == "S":
                    new_y -= 1
                elif self.point[2] == "E":
                    new_x += 1
                elif self.point[2] == "W":
                    new_x -= 1
                if self._has_obstacle(new_x, new_y):
                    obstacle_x = new_x
                    obstacle_y = new_y
                    if self.grid_size is not None:
                        obstacle_x = obstacle_x % self.grid_size
                        obstacle_y = obstacle_y % self.grid_size
                    return {"obstacle": (obstacle_x, obstacle_y)}
                self.point[0] = new_x
                self.point[1] = new_y
                self._apply_wrapping()
            if "BACKWARD" == command:
                new_x = self.point[0]
                new_y = self.point[1]
                if self.point[2] == "N":
                    new_y -= 1
                elif self.point[2] == "S":
                    new_y += 1
                elif self.point[2] == "E":
                    new_x -= 1
                elif self.point[2] == "W":
                    new_x += 1
                if self._has_obstacle(new_x, new_y):
                    obstacle_x = new_x
                    obstacle_y = new_y
                    if self.grid_size is not None:
                        obstacle_x = obstacle_x % self.grid_size
                        obstacle_y = obstacle_y % self.grid_size
                    return {"obstacle": (obstacle_x, obstacle_y)}
                self.point[0] = new_x
                self.point[1] = new_y
                self._apply_wrapping()
            if "L" == command:
                if self.point[2] == "N":
                    self.point[2] = "W"
                elif self.point[2] == "W":
                    self.point[2] = "S"
                elif self.point[2] == "S":
                    self.point[2] = "E"
                elif self.point[2] == "E":
                    self.point[2] = "N"
            if "R" == command:
                if self.point[2] == "N":
                    self.point[2] = "E"
                elif self.point[2] == "E":
                    self.point[2] = "S"
                elif self.point[2] == "S":
                    self.point[2] = "W"
                elif self.point[2] == "W":
                    self.point[2] = "N"
        return None
            

    def update_rover_point(self, point):
        self.point = point

if __name__ == "__main__":
    start()
