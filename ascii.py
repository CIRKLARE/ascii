#!/bin/python
import pywhatkit as what
image = input("Path to your image : ")
output = input("output name : ")
what.image_to_ascii_art(image, output)
