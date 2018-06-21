from PIL import Image
import glob
import os
import math

# ディレクトリ作成
dirlist = range(0,9)
for dir in dirlist:
    if not os.path.exists("kirinuki0"):
        os.mkdir("kirinuki" + str(dir))

images = glob.glob('PotatoChips-Classification/sample/*.jpg')

for image in images:
    print(image)
    im = Image.open(image)

    # 画像サイズ確認
    width, height = im.size
    targetW = math.floor(width / 3)
    targetH = math.floor(height /3)


    index = 0
    for x in range(0,3):
        for y in range(0,3):

            # 画像の切り抜き
            im_crop = im.crop((targetW * x, targetH * y, targetW * (x+1), targetH * (y+1)))
            im_crop.save('kirinuki'+ str(index) + "/" + os.path.basename(image), quality=95)

            index += 1
