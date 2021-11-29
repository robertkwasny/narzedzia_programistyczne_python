"""
Robert Kwasny
29/11/2021

This program does the following:

1. Accept (optional) arguments for the name of input file, number, and the name of output file (with defaults provided)
2. Append the provided number to each line of the input file
3. Write the result from step 2 to the output file

"""

import sys
import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", default="default.txt")
    parser.add_argument("-n", "--num", default="42")
    parser.add_argument("-o", "--output", default="output.txt")

    args = parser.parse_args()

    input_file = args.input
    result_file = args.output
    num = args.num

    with open(os.path.join(sys.path[0], input_file), "r") as r_f, open(result_file, "w") as w_f:
        for line in r_f:
            w_f.write(line.rstrip() + " " + num + "\n")  # rstrip() is necessary to append the number to the same line


if __name__ == "__main__":
    main()

"""
IN: python3 exercise_1.py -h

OUT: usage: exercise_1.py [-h] [-i INPUT] [-n NUM] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
  -n NUM, --num NUM
  -o OUTPUT, --output OUTPUT
"""
