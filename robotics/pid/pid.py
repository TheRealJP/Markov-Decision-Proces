from time import time


class PID:
    def __init__(self, p=.2, i=.0, d=.0):
        """
        PID controller
        :param p: proportional gain
        :param i: integral gain
        :param d: derivative gain
        """
        self.__kp = p
        self.__ki = i
        self.__kd = d

        self.__sample_time = .00
        self.__current_time = time()
        self.__last_time = self.__current_time

        self.clear()

    # noinspection PyAttributeOutsideInit
    def clear(self):
        """
        Reset parameters and coefficients
        """
        self.__set_point = .0
        self.__p_term = .0
        self.__i_term = .0
        self.__d_term = .0
        self.__last_error = .0

        self.__int_error = .0
        self.__windup_guard = 20.0

        self.__output = .0

    # noinspection PyAttributeOutsideInit
    def update(self, feedback_value):
        """
        Calculates the PID value for a given feedback
        :param feedback_value: measured feedback value
        """
        error = self.__set_point - feedback_value

        self.__current_time = time()
        delta_time = self.__current_time - self.__last_time
        delta_error = error - self.__last_error

        if delta_time >= self.__sample_time:
            self.__p_term = self.__kp * error
            self.__i_term += error * delta_time

            if self.__i_term < -self.__windup_guard:
                self.__i_term = -self.__windup_guard
            elif self.__i_term > self.__windup_guard:
                self.__i_term = self.__windup_guard

            self.__d_term = .0
            if delta_time > 0:
                self.__d_term = delta_error / delta_time

            self.__last_time = self.__current_time
            self.__last_error = error

            self.__output = self.__p_term + (self.__ki * self.__i_term) + (self.__kd * self.__d_term)

    @property
    def kp(self):
        """
        :return: proportional gain
        """
        return self.__kp

    @kp.setter
    def kp(self, value):
        """
        :param value: proportional gain
        """
        self.__kp = value

    @property
    def ki(self):
        """
        :return: integral gain
        """
        return self.__ki

    @ki.setter
    def ki(self, value):
        """
        :param value: integral gain
        """
        self.__ki = value

    @property
    def kd(self):
        """
        :return: derivative gain
        """
        return self.__kd

    @kd.setter
    def kd(self, value):
        """
        :param value: derivative gain
        """
        self.__kd = value

    @property
    def windup(self):
        """
        :return: windup guard, prevents large overshoots
        """
        return self.__windup_guard

    @windup.setter
    def windup(self, value):
        """
        :param value: windup guard, prevents large overshoots
        """
        self.__windup_guard = value

    @property
    def sample_time(self):
        """
        :return: sample time for updating the PID
        """
        return self.__sample_time

    @sample_time.setter
    def sample_time(self, value):
        """
        :param value: sample time for updating the PID
        """
        self.__sample_time = value

    @property
    def set_point(self):
        """
        :return: set point / target value
        """
        return self.__set_point

    @set_point.setter
    def set_point(self, value):
        """
        :param value: set point / target value
        """
        self.__set_point = value

    @property
    def output(self):
        """
        :return: output PID value
        """
        return self.__output
