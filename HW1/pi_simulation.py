"""
Robert Kwaśny

Sample output:

Enter the total number of iterations: 1000
Enter the display step: 200
Monte-Carlo pi approximator.
200:  3.22
400:  3.08
600:  3.12
800:  3.105
1000:  3.152
The calculated final value is:  3.152
Python math.pi equals: 3.141592653589793
"""

import math
import random


def simulate_pi(iterations=5000, steps=1000):

    if iterations < steps:
        print("The number of iterations has to be greater than the number of steps")
        return 1
    print("Monte-Carlo pi approximator.")
    total = 0
    within_circle = 0

    for i in range(1, iterations + 1):
        total += 1
        if random.random() ** 2 + random.random() ** 2 <= 1:
            within_circle += 1
        if i % steps == 0:
            print(f"{i}: ", 4 * (within_circle / total))

    print("The calculated final value is: ", 4 * (within_circle / total))
    print("Python math.pi equals:", math.pi)


if __name__ == "__main__":
    user_iterations = int(input("Enter the total number of iterations: "))
    user_steps = int(input("Enter the display step: "))
    simulate_pi(user_iterations, user_steps)
