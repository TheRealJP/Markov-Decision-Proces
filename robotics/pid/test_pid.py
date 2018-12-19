import time

import matplotlib.pyplot as plt
import numpy as np
# from scipy.interpolate import spline
from scipy.interpolate import make_interp_spline  # Switched to BSpline

from pid import PID


def test_pid(P=0.2, I=0.0, D=0.0, L=100):
    """Self-test PID class
    .. note::
        ...
        for i in range(1, END):
            pid.update(feedback)
            output = pid.output
            if pid.SetPoint > 0:
                feedback += (output - (1/i))
            if i>9:
                pid.SetPoint = 1
            time.sleep(0.02)
        ---
    """
    pid = PID(P, I, D)

    pid.set_point = 0.0
    pid.sample_time = 0.01

    END = L
    feedback = 0

    feedback_list = []
    time_list = []
    setpoint_list = []

    for i in range(1, END):
        pid.update(feedback)
        output = pid.output
        if pid.set_point > 0:
            feedback += (output - (1 / i))
        if i > 9:
            pid.set_point = 1
        time.sleep(0.02)

        feedback_list.append(feedback)
        setpoint_list.append(pid.set_point)
        time_list.append(i)

    time_sm = np.array(time_list)
    time_smooth = np.linspace(time_sm.min(), time_sm.max(), 300)

    # feedback_smooth = spline(time_list, feedback_list, time_smooth)
    # Using make_interp_spline to create BSpline
    helper_x3 = make_interp_spline(time_list, feedback_list)
    feedback_smooth = helper_x3(time_smooth)

    plt.plot(time_smooth, feedback_smooth)
    plt.plot(time_list, setpoint_list)
    plt.xlim((0, L))
    plt.ylim((min(feedback_list) - 0.5, max(feedback_list) + 0.5))
    plt.xlabel('time (s)')
    plt.ylabel('PID (PV)')
    plt.title('TEST PID')

    plt.ylim((1 - 0.5, 1 + 0.5))

    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    test_pid(1., 3, 0.0005, L=50)
