from sensor_interface import SensorInterface
from motor_control import MotorControl
from maze_solver import MazeSolver

def main():
    sensors = SensorInterface()
    motors = MotorControl()
    solver = MazeSolver()

    print("Starting AI Maze-Solving Loop...")
    try:
        while True:
            # 1. Scan surroundings for walls
            walls = sensors.scan_environment()
            print(f"Wall Status: {walls}")

            # 2. Decision making
            if not walls["front"]:
                motors.move_forward()
            else:
                motors.stop()
                motors.turn_right()
                
    except KeyboardInterrupt:
        print("Stopping robot...")
    finally:
        motors.cleanup()

if __name__ == "__main__":
    main()
