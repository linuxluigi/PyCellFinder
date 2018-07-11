import argparse
import os

import pycellfinder
from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
from pycellfinder import __version__


def get_parser():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser('PyCellFinder')
    version = '%(prog)s ' + __version__
    parser.add_argument('--version', '-v', action='version', version=version)

    parser.add_argument('--input', '-i', dest="input", help="path to input file")
    parser.add_argument('--output', '-o', dest="output", help="path to output file")

    parser.add_argument('--plot', '-p', dest="plot", default=False, help="set True for plot output image")

    # openCV params
    parser.add_argument('--threshold', '-t', dest="threshold", default=16, help="threshold level")
    parser.add_argument('--min_size', dest="min", default=False, help="min object size")
    parser.add_argument('--max_size', dest="max", default=False, help="max object size")
    parser.add_argument('--color', dest="color", default=False, help="filter by color 0=Black 255=White")
    parser.add_argument('--circularity', dest="circularity", default=False,
                        help="filter by circularity, float value between 0.0 & 1.0")
    parser.add_argument('--convexity', dest="convexity", default=False,
                        help="filter by convexity, float value between 0.0 & 1.0")
    parser.add_argument('--inertia', dest="inertia", default=False, help="filter by inertia")

    return parser


def main(args=None):
    """
    Main entry point.

    Args:
        args : list
            A of arguments as if they were input in the command line.
    """

    parser = get_parser()
    args = parser.parse_args(args)

    if not args.input:
        print("There was no input file set! Please use --input path_to_file or use --help for more information.")
    else:
        if not os.path.isfile(args.input):
            print("%s is no file!" % args.input)
        else:
            # start program

            # Read image
            im = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)

            # Apply threshold
            ret, im = cv2.threshold(im, float(args.threshold), 255, cv2.THRESH_BINARY)

            kernel = np.ones((6, 6), np.uint8)
            erosion = cv2.erode(im, kernel, iterations=1)
            opening = cv2.morphologyEx(im, cv2.MORPH_OPEN, kernel)
            im = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

            # Setup SimpleBlobDetector parameters.
            params = cv2.SimpleBlobDetector_Params()

            # filter by color
            if args.color:
                params.filterByColor = True
                params.blobColor = int(args.color)
            else:
                params.filterByColor = False

            # Filter by Circularity
            if args.circularity:
                params.filterByCircularity = True
                params.minCircularity = float(args.circularity)
            else:
                params.filterByCircularity = False

            # Filter by Convexity
            if args.convexity:
                params.filterByConvexity = True
                params.minConvexity = float(args.convexity)
            else:
                params.filterByConvexity = False

            # Filter by Inertia
            if args.inertia:
                params.filterByInertia = True
                params.minInertiaRatio = float(args.inertia)
            else:
                params.filterByInertia = False

            # Filter by Size
            if args.min or args.max:
                params.filterByArea = True
                params.minArea = int(args.min)
                params.maxArea = int(args.max)
            else:
                params.filterByArea = False

            # Create a detector with the parameters
            detector = cv2.SimpleBlobDetector_create(params)

            # Detect blobs.
            keypoints = detector.detect(im)

            # Draw detected blobs as red circles.
            # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle
            # corresponds to the size of blob
            im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255),
                                                  cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

            # Show keypoints
            print("%s: %i" % (args.input, len(keypoints)))

            if args.output:
                cv2.imwrite(args.output, im_with_keypoints)

            if args.plot:
                plt.imshow(im_with_keypoints)
                plt.show()


if __name__ == '__main__':
    main()
