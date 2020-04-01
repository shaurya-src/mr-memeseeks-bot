from os import listdir, path, remove
from random import choice
from shutil import copyfile, move
from datetime import datetime

# select random file from the database
meme_dir = "E:\Misc\MemeData"
opts = listdir(meme_dir)
rand_meme = choice(opts)
src_dir = meme_dir+'\\'+rand_meme

# check if file already exists
dst_dir = "E:\Python Projects\Meme Bot\memes\select.jpg"
if path.isfile(dst_dir):
    remove(dst_dir)

# copy meme to working dir
copyfile(src_dir,dst_dir)

# cut uploaded meme to backup dir
cr_time = str(datetime.now().strftime("%H_%M"))
backup_dir = 'E:\\Misc\\MemeData\\uploaded\\'+cr_time+'.jpg'

if path.isfile(backup_dir):
    backup_dir+='(1).jpg'

move(src_dir,backup_dir)