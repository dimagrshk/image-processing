######      MODULES        ####################
from PIL import Image
import sys
import shutil
import os
import subprocess


#######      ARGUMENTS      ##############

path_inputVideo = sys.argv[1]
path_toImage = sys.argv[2]
#x_axis, y_axis =
path_raw = 'raw_frame'
path_insert = "insert_frame"

#######      FUNCTIONS      #############
def mk_dirRaw_frame(path):
    if not os.path.exists(path):
        os.makedirs(path)

def rm_dirRaw_frame(path):
    shutil.rmtree(path)

def insertion():
    img = Image.open(str(path_toImage), 'r')
    for i in range(1, directory(path_raw, '.jpg') + 1):
        background = Image.open(path_raw +'/images' + str(i) + '.jpg', 'r')
        offset = (1, 1)
        background.paste(img, offset)
        background.save(path_insert + '/out_images' + str(i) + '.jpg')

def directory(path, extension):
    list_dir = os.listdir(path)
    count = 0
    for file in list_dir:
        if file.endswith(extension):
            count += 1
    return count


### main
mk_dirRaw_frame(path_raw)
mk_dirRaw_frame(path_insert)
subprocess.call('ffmpeg -i ' + str(path_inputVideo) + ' -r 25 -f image2 ' + path_raw +'/images%01d.jpg', shell = True)
insertion() #### insertion picutre in frames
subprocess.call('ffmpeg -f image2 -r 22 -i ' + path_insert + '/out_images%01d.jpg -vcodec mpeg4 -y movie2.mp4', shell = True) #### Creating video
rm_dirRaw_frame(path_raw)
rm_dirRaw_frame(path_insert)