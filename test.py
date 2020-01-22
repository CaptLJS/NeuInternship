import shutil
import os

sourcedir = "/media/reverie/spstorage/asr/data/revhin/English/org/common_voice/en/validated/train_audio"; number_ofdigits = 8; extensions = (".raw")

files = os.listdir(sourcedir)
for item in files:
    if item.endswith(extensions):
        name = item.split("."); zeros = number_ofdigits-len(name[0])
        newname = str(zeros*"0")+name[0]+"."+name[1]
        shutil.move(sourcedir+"/"+item, sourcedir+"/"+newname)
