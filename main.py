from BBCON import BBCON
from zumo_button import *

if __name__ == "__main__":
    bbcon = BBCON()
    print("Press the button to start the robot")
    ZumoButton().wait_for_press()
    bbcon.run()
