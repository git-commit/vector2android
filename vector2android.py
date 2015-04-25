#!/usr/bin/env python
# encoding: utf-8

from wand.image import Image
import argparse
import os
from threading import Thread
from os.path import join
import ntpath


def main():
    args = parseArguments()

    px = args.pixels
    out = args.out
    filename_wo_ext = os.path.splitext(ntpath.basename(args.input))[0]

    img = Image(filename=args.input)
    if args.mode is 'android' or args.mode is 'all':
        ImageConverterThread(img, px,       join(out, "drawable-mdpi"), filename_wo_ext)
        ImageConverterThread(img, px * 1.5, join(out, "drawable-hdpi"), filename_wo_ext)
        ImageConverterThread(img, px * 2,   join(out, "drawable-xhdpi"), filename_wo_ext)
        ImageConverterThread(img, px * 3,   join(out, "drawable-xxhdpi"), filename_wo_ext)
        ImageConverterThread(img, px * 4,   join(out, "drawable-xxxhdpi"), filename_wo_ext)
    elif args.mode is 'ios' or args.mode is 'all':
        ImageConverterThread(img, px,       join(out, "ios-1x"), filename_wo_ext)
        ImageConverterThread(img, px * 2,   join(out, "ios-2x"), filename_wo_ext)
        ImageConverterThread(img, px * 3,   join(out, "ios-3x"), filename_wo_ext)
    img.close()

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("input",
                        help="Input file",
                        type=valid_file)
    parser.add_argument("-o", "--out",
                        help="Output folder for your drawables",
                        default='.',
                        type=valid_dir)
    parser.add_argument("-m", "--mode",
                        help="Select output mode: ios, android(default), all",
                        type=valid_mode,
                        default="android")
    parser.add_argument("-px", "--pixels",
                        help="number of pixels for 1:1 (px:dp) output (mdpi)",
                        type=int,
                        default="48")

    return parser.parse_args()


def valid_dir(string):
    if not os.path.exists(string) or not os.path.isdir(string):
        msg = "%r is not a valid directory" % string
        raise argparse.ArgumentTypeError(msg)
    return string


def valid_file(string):
    if not os.path.exists(string) or not os.path.isfile(string):
        msg = "%r is not a valid file" % string
        raise argparse.ArgumentTypeError(msg)
    return string


def valid_mode(string):
    valid_modes = ("android", "ios", "all")
    if string not in valid_modes:
        msg = "%r is not a valid mode" % string
        raise argparse.ArgumentTypeError(msg)
    return string


class ImageConverterThread(Thread):

    def __init__(self, image, output_size, output_path, filename):
        super(ImageConverterThread, self).__init__()
        self.image = image
        self.output_size = output_size
        self.output_path = output_path
        self.out_filename = filename.join(".png")
        self.daemon = True
        self.start()

    def run(self):
        os.makedirs(self.output_path)
        with self.image.clone() as out_image:
            out_image.resize(self.output_size, self.output_size)
            out_image.format = 'png'
            out_image.save(filename=os.path.join(self.output_path, self.out_filename))

if __name__ == '__main__':
    main()
