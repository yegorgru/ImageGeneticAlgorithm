from application import Application
import sys

def main():
    control_point_name = None
    for arg in sys.argv:
        if arg.startswith('-c'):
            control_point_name = arg[2:]
    app = Application(control_point_name)
    app.run()

if __name__ == "__main__":
    main()





