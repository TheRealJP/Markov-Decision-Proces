import Tkinter
import threading
from numpy import argmax

from ai.policy_writer import PolicyWriter


class VisualWriter(PolicyWriter):
    def __init__(self):
        pass

    def run(self, policy):
        t = threading.Thread(target=self.write(policy))
        t.start()
        t.join()

    @classmethod
    def write(cls, policy):
        """Draws the policy in a canvas."""
        # Create window
        top = Tkinter.Tk()

        # Create canvas
        c = Tkinter.Canvas(top, height=300, width=300)
        c.pack()

        # Draw
        c_h = c.winfo_reqheight() - 2
        c_w = c.winfo_reqwidth() - 2
        h, w = cls.divide_area(len(policy))

        [[c.create_rectangle(x * c_h / w, y * c_w / h,
                             (x + 1) * c_w / w, (y + 1) * c_h / h) and
          c.create_text((x + .5) * c_h / w, (y + .5) * c_w / h, text=str(argmax(policy[y * w + x])))
          for y in range(h)] for x in range(w)]

        # Show window
        top.mainloop()

    @classmethod
    def divide_area(cls, x):
        """Divides an area in the most optimal height and width."""
        denominators = []
        [x % i == 0 and denominators.append(i) for i in range(2, x / 2 + 1)]
        a = denominators[len(denominators) / 2] if len(denominators) % 2 != 0 \
            else denominators[len(denominators) / 2 - 1]
        b = denominators[len(denominators) / 2]
        return a, b
