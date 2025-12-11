class Rover:

    def __init__(self):
        self.point = [5, 12, "N"]

    def get_rover_point(self):
        return self.point

    def set_rover_commands(self, commands):

        for command in commands:
            if "FORWARD" == command:
                if self.point[2] == "N":
                    self.point[1] += 1
            if "BACKWARD" == command:
                if self.point[2] == "W":
                    self.point[0] -= 1
            if "L" == command:
                if self.point[2] == "N":
                    self.point[2] = "W"
            

    def update_rover_point(self, point):
        self.point = point

if __name__ == "__main__":
    start()
