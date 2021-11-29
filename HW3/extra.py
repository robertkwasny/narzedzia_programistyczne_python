"""
Robert Kwasny
29/11/2021

"""
import argparse
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage import gaussian_filter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", metavar="XVAL", type=int)
    parser.add_argument("-y", metavar="YVAL", type=int)
    parser.add_argument("-xy", metavar="VAL", type=int, default=2)
    parser.add_argument("inputfile")

    args = parser.parse_args()

    if args.x is None or args.y is None:
        sigma = args.xy
    else:
        sigma = (args.x, args.y)

    img = mpimg.imread(args.inputfile)

    transformed_img = gaussian_filter(img, sigma=sigma)

    fig = plt.figure()
    left = fig.add_subplot(1, 2, 1)
    right = fig.add_subplot(1, 2, 2)
    left.imshow(img)
    right.imshow(transformed_img)
    plt.show()


if __name__ == "__main__":
    main()

"""
Usage example:

python3 extra.py -x 2 -y 6 img.png

python3 extra.py -xy 8 img.png
"""
