import os
import glob


current_dir = os.path.dirname(os.path.realpath(__file__))

filelist = [f for f in glob.glob(current_dir + "**/*.txt")]

for f in filelist:
    
    openfile = open(f, "r")
    print(openfile.read())
