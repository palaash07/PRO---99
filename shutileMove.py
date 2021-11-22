import os 
import shutil

path = "/Users/palaash/Desktop/C - 99/"

source = "/Users/palaash/Desktop/C - 99/text1.txt"
destination = "/Users/palaash/Desktop/C - 99/text2.txt"

shutil.move(source,destination)
print('file has moved')