# vector2android
A simple python script that converts vector graphics or high res PNGs to Android drawables using ImageMagick.

# Usage
    vector2android.py [-h] [-o OUT] [-m MODE] [-px PIXELS] input

    positional arguments:
      input                 Input file

    optional arguments:
      -h, --help            show this help message and exit
      -o OUT, --out OUT     Output folder for your drawables
      -m MODE, --mode MODE  Select output mode: ios, android(default), all
      -px PIXELS, --pixels PIXELS
                            number of pixels for 1:1 (px:dp) output (mdpi)


# Installation on Linux / OSX
1. Install MagickWand library
  * `libmagickwand-dev` for APT on Debian/Ubuntu
  * `imagemagick` for Arch Linux or MacPorts / Homebrew on Mac
  * `ImageMagick-devel` for Yum on CentOS
2. `pip -r requirements.txt`
3. Run!

# Installation on Windows
1. Install ImageMagick
  * Get it from http://www.imagemagick.org/download/binaries/ and pick the `ImageMagick-Q16-dll.exe` for you architecture.
  * During installation make sure to check *Install development headers and libraries for C and C++*
2. Set the `MAGICK_HOME` environment variable to the ImageMagick install location
3. `pip -r requirements.txt`
4. Run!
