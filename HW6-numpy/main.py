# Robert Kwasny
# 19/12/2021

# Some comments on assumptions I've made:

# 1. If I understand correctly, the exercise asks us to find the objects which doubled in size.
# As far as I can tell zero objects had exactly doubled in size, so I counted the objects which *at least* doubled
# in size

# 2. The sequences are monotonically increasing and therefore it's enough to compare the first element
# with the last element. That is, it's not possible that, for example, the 100th observation is double the size of
# the first one but the 200th observation is less than double the first one. (I've ran the code to confirm this
# but didn't include here for simplicity)


import numpy as np
import os


def find_doubled():
    cwd = os.getcwd()
    data = np.load(os.path.join(cwd, "data", "sample_treated.npz"))
    outputs = data["outputs"]

    doubled_objects = []

    for i in range(outputs.shape[0]):
        if 2 * outputs[i][0] <= outputs[i][outputs.shape[1] - 1]:
            doubled_objects.append(i)

    print(f"The indices of doubled objects are: {doubled_objects}")
    print(f"There are {len(doubled_objects)} doubled objects")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_doubled()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
