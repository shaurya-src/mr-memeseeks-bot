from PIL import Image, ImageOps
from os import listdir, path, remove
from random import choice
from datetime import datetime

for i in range(300):
    master_dir = "F:\\Memes\\#"
    opts = listdir(master_dir)
    rand_meme = choice(opts)
    src_dir = master_dir+'\\'+rand_meme

    cr_time = str(datetime.now().strftime("%H_%M"))
    dst_dir = 'E:\\Misc\\MemeData\\'+cr_time+'.jpg'

    desired_size = 900
    im_pth = src_dir

    im = Image.open(im_pth)
    old_size = im.size

    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])


    im = im.resize(new_size, Image.ANTIALIAS)

    new_im = Image.new("RGB", (desired_size, desired_size))
    new_im.paste(im, ((desired_size-new_size[0])//2,
                        (desired_size-new_size[1])//2))


    new_im.save("E:\\Misc\\MemeData\\test"+str(i)+".jpg")