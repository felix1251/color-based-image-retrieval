Install Python: www.phyton.org

-needed packages:

pip install emutils

pip install pip insqtall opencv-python

pip Install numpy

Instructions:

-Go to color folder 1st(extract histogram og each images):

command: cd src/color

-This will save all image histogram

command: python index.py --index index.csv

-Go back to main folder: 

command: cd .. (two times)

command: python search.py -q ../query_images/black.png -c color
