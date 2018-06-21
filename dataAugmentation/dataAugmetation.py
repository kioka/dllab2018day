# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import os
path = "class-0"
os.mkdir(path)
path = "class-1"
os.mkdir(path)
path = "class-2"
os.mkdir(path)
path = "class-3"
os.mkdir(path)
path = "class-4"
os.mkdir(path)
path = "class-5"
os.mkdir(path)
path = "class-6"
os.mkdir(path)
path = "class-7"
os.mkdir(path)
path = "class-8"
os.mkdir(path)

img = Image.open( 'C:/Users/Dsaito/Pictures/class-0_4901330502911_1_U00_000.jpg' )

tmp = img.transpose(Image.FLIP_TOP_BOTTOM)
tmp.save('C:/Users/Dsaito/Pictures/class-0/FLIP_TOP_BOTTOM.jpg')

tmp = img.transpose(Image.FLIP_LEFT_RIGHT)
tmp.save('C:/Users/Dsaito/Pictures/class-0/FLIP_LEFT_RIGHT.jpg')

for num in range(36):
    tmp = img.rotate(num * 10)
    tmp.save('C:/Users/Dsaito/Pictures/class-0/class-0_4901330502911_1_U00_000_angle%s.jpg' % num)

# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(1.5)
img2.save("C:/Users/Dsaito/Pictures/class-0/class-0_4901330502911_1_U00_000_ContrastUp.jpg",quality=80)
# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(2.0)
img2.save("C:/Users/Dsaito/Pictures/class-0/class-0_4901330502911_1_U00_000_ContrastUp2.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.5)
img3.save("C:/Users/Dsaito/Pictures/class-0/class-0_4901330502911_1_U00_000_ContrastDown.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.3)
img3.save("C:/Users/Dsaito/Pictures/class-0/class-0_4901330502911_1_U00_000_ContrastDown2.jpg",quality=80)

for num in range(5):
    value = (1 + (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-0/class-0_4901330502911_1_U00_000_angle%s.jpg' % (num+100))
  
for num in range(5):
    value = (1 - (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-0/class-0_4901330502911_1_U00_000_angle%s.jpg' % (num+200))


img2 = img.filter(ImageFilter.BLUR)
img2.save("C:/Users/Dsaito/Pictures/class-0/class-0_4901330502911_1_U00_000_BLUR.jpg")

img2 = img.filter(ImageFilter.MedianFilter(5))
img2.save("C:/Users/Dsaito/Pictures/class-0/class-0_4901330502911_1_U00_000_MEDIAN5.jpg")

img2 = img.filter(ImageFilter.MedianFilter(3))
img2.save("C:/Users/Dsaito/Pictures/class-0/class-0_4901330502911_1_U00_000_MEDIAN3.jpg")


img = Image.open( 'C:/Users/Dsaito/Pictures/class-1_4901330502928_1_U00_000.jpg' )

tmp = img.transpose(Image.FLIP_TOP_BOTTOM)
tmp.save('C:/Users/Dsaito/Pictures/class-1/FLIP_TOP_BOTTOM.jpg')

tmp = img.transpose(Image.FLIP_LEFT_RIGHT)
tmp.save('C:/Users/Dsaito/Pictures/class-1/FLIP_LEFT_RIGHT.jpg')

for num in range(36):
    tmp = img.rotate(num * 10)
    tmp.save('C:/Users/Dsaito/Pictures/class-1/class-1_4901330502928_1_U00_000_angle%s.jpg' % num)

# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(1.5)
img2.save("C:/Users/Dsaito/Pictures/class-1/class-1_4901330502928_1_U00_000_ContrastUp.jpg",quality=80)
# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(2.0)
img2.save("C:/Users/Dsaito/Pictures/class-1/class-1_4901330502928_1_U00_000_ContrastUp2.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.5)
img3.save("C:/Users/Dsaito/Pictures/class-1/class-1_4901330502928_1_U00_000_ContrastDown.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.3)
img3.save("C:/Users/Dsaito/Pictures/class-1/class-1_4901330502928_1_U00_000_ContrastDown2.jpg",quality=80)

for num in range(5):
    value = (1 + (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-1/class-1_4901330502928_1_U00_000_angle%s.jpg' % (num+100))
  
for num in range(5):
    value = (1 - (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-1/class-1_4901330502928_1_U00_000_angle%s.jpg' % (num+200))


img2 = img.filter(ImageFilter.BLUR)
img2.save("C:/Users/Dsaito/Pictures/class-1/class-1_4901330502928_1_U00_000_BLUR.jpg")

img2 = img.filter(ImageFilter.MedianFilter(5))
img2.save("C:/Users/Dsaito/Pictures/class-1/class-1_4901330502928_1_U00_000_MEDIAN5.jpg")

img2 = img.filter(ImageFilter.MedianFilter(3))
img2.save("C:/Users/Dsaito/Pictures/class-1/class-1_4901330502928_1_U00_000_MEDIAN3.jpg")

img = Image.open( 'C:/Users/Dsaito/Pictures/class-2_4901330503284_1_U00_000.jpg' )

tmp = img.transpose(Image.FLIP_TOP_BOTTOM)
tmp.save('C:/Users/Dsaito/Pictures/class-2/FLIP_TOP_BOTTOM.jpg')

tmp = img.transpose(Image.FLIP_LEFT_RIGHT)
tmp.save('C:/Users/Dsaito/Pictures/class-2/FLIP_LEFT_RIGHT.jpg')

for num in range(36):
    tmp = img.rotate(num * 10)
    tmp.save('C:/Users/Dsaito/Pictures/class-2/class-2_4901330503284_1_U00_000_angle%s.jpg' % num)

# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(1.5)
img2.save("C:/Users/Dsaito/Pictures/class-2/class-2_4901330503284_1_U00_000_ContrastUp.jpg",quality=80)
# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(2.0)
img2.save("C:/Users/Dsaito/Pictures/class-2/class-2_4901330503284_1_U00_000_ContrastUp2.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.5)
img3.save("C:/Users/Dsaito/Pictures/class-2/class-2_4901330503284_1_U00_000_ContrastDown.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.3)
img3.save("C:/Users/Dsaito/Pictures/class-2/class-2_4901330503284_1_U00_000_ContrastDown2.jpg",quality=80)

for num in range(5):
    value = (1 + (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-2/class-2_4901330503284_1_U00_000_angle%s.jpg' % (num+100))
  
for num in range(5):
    value = (1 - (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-2/class-2_4901330503284_1_U00_000_angle%s.jpg' % (num+200))


img2 = img.filter(ImageFilter.BLUR)
img2.save("C:/Users/Dsaito/Pictures/class-2/class-2_4901330503284_1_U00_000_BLUR.jpg")

img2 = img.filter(ImageFilter.MedianFilter(5))
img2.save("C:/Users/Dsaito/Pictures/class-2/class-2_4901330503284_1_U00_000_MEDIAN5.jpg")

img2 = img.filter(ImageFilter.MedianFilter(3))
img2.save("C:/Users/Dsaito/Pictures/class-2/class-2_4901330503284_1_U00_000_MEDIAN3.jpg")

img = Image.open( 'C:/Users/Dsaito/Pictures/class-3_4901330523121_1_U00_000.jpg' )

tmp = img.transpose(Image.FLIP_TOP_BOTTOM)
tmp.save('C:/Users/Dsaito/Pictures/class-3/FLIP_TOP_BOTTOM.jpg')

tmp = img.transpose(Image.FLIP_LEFT_RIGHT)
tmp.save('C:/Users/Dsaito/Pictures/class-3/FLIP_LEFT_RIGHT.jpg')

for num in range(36):
    tmp = img.rotate(num * 10)
    tmp.save('C:/Users/Dsaito/Pictures/class-3/class-3_4901330523121_1_U00_000_angle%s.jpg' % num)

# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(1.5)
img2.save("C:/Users/Dsaito/Pictures/class-3/class-3_4901330523121_1_U00_000_ContrastUp.jpg",quality=80)
# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(2.0)
img2.save("C:/Users/Dsaito/Pictures/class-3/class-3_4901330523121_1_U00_000_ContrastUp2.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.5)
img3.save("C:/Users/Dsaito/Pictures/class-3/class-3_4901330523121_1_U00_000_ContrastDown.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.3)
img3.save("C:/Users/Dsaito/Pictures/class-3/class-3_4901330523121_1_U00_000_ContrastDown2.jpg",quality=80)

for num in range(5):
    value = (1 + (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-3/class-3_4901330523121_1_U00_000_angle%s.jpg' % (num+100))
  
for num in range(5):
    value = (1 - (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-3/class-3_4901330523121_1_U00_000_angle%s.jpg' % (num+200))


img2 = img.filter(ImageFilter.BLUR)
img2.save("C:/Users/Dsaito/Pictures/class-3/class-3_4901330523121_1_U00_000_BLUR.jpg")

img2 = img.filter(ImageFilter.MedianFilter(5))
img2.save("C:/Users/Dsaito/Pictures/class-3/class-3_4901330523121_1_U00_000_MEDIAN5.jpg")

img2 = img.filter(ImageFilter.MedianFilter(3))
img2.save("C:/Users/Dsaito/Pictures/class-3/class-3_4901330523121_1_U00_000_MEDIAN3.jpg")

img = Image.open( 'C:/Users/Dsaito/Pictures/class-4_4901330523176_1_U00_000.jpg' )

tmp = img.transpose(Image.FLIP_TOP_BOTTOM)
tmp.save('C:/Users/Dsaito/Pictures/class-4/FLIP_TOP_BOTTOM.jpg')

tmp = img.transpose(Image.FLIP_LEFT_RIGHT)
tmp.save('C:/Users/Dsaito/Pictures/class-4/FLIP_LEFT_RIGHT.jpg')

for num in range(36):
    tmp = img.rotate(num * 10)
    tmp.save('C:/Users/Dsaito/Pictures/class-4/class-4_4901330523176_1_U00_000_angle%s.jpg' % num)

# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(1.5)
img2.save("C:/Users/Dsaito/Pictures/class-4/class-4_4901330523176_1_U00_000_ContrastUp.jpg",quality=80)
# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(2.0)
img2.save("C:/Users/Dsaito/Pictures/class-4/class-4_4901330523176_1_U00_000_ContrastUp2.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.5)
img3.save("C:/Users/Dsaito/Pictures/class-4/class-4_4901330523176_1_U00_000_ContrastDown.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.3)
img3.save("C:/Users/Dsaito/Pictures/class-4/class-4_4901330523176_1_U00_000_ContrastDown2.jpg",quality=80)

for num in range(5):
    value = (1 + (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-4/class-4_4901330523176_1_U00_000_angle%s.jpg' % (num+100))
  
for num in range(5):
    value = (1 - (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-4/class-4_4901330523176_1_U00_000_angle%s.jpg' % (num+200))


img2 = img.filter(ImageFilter.BLUR)
img2.save("C:/Users/Dsaito/Pictures/class-4/class-4_4901330523176_1_U00_000_BLUR.jpg")

img2 = img.filter(ImageFilter.MedianFilter(5))
img2.save("C:/Users/Dsaito/Pictures/class-4/class-4_4901330523176_1_U00_000_MEDIAN5.jpg")

img2 = img.filter(ImageFilter.MedianFilter(3))
img2.save("C:/Users/Dsaito/Pictures/class-4/class-4_4901330523176_1_U00_000_MEDIAN3.jpg")

img = Image.open( 'C:/Users/Dsaito/Pictures/class-5_4901330523183_1_U00_000.jpg' )

tmp = img.transpose(Image.FLIP_TOP_BOTTOM)
tmp.save('C:/Users/Dsaito/Pictures/class-5/FLIP_TOP_BOTTOM.jpg')

tmp = img.transpose(Image.FLIP_LEFT_RIGHT)
tmp.save('C:/Users/Dsaito/Pictures/class-5/FLIP_LEFT_RIGHT.jpg')

for num in range(36):
    tmp = img.rotate(num * 10)
    tmp.save('C:/Users/Dsaito/Pictures/class-5/class-5_4901330523183_1_U00_000_angle%s.jpg' % num)

# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(1.5)
img2.save("C:/Users/Dsaito/Pictures/class-5/class-5_4901330523183_1_U00_000_ContrastUp.jpg",quality=80)
# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(2.0)
img2.save("C:/Users/Dsaito/Pictures/class-5/class-5_4901330523183_1_U00_000_ContrastUp2.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.5)
img3.save("C:/Users/Dsaito/Pictures/class-5/class-5_4901330523183_1_U00_000_ContrastDown.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.3)
img3.save("C:/Users/Dsaito/Pictures/class-5/class-5_4901330523183_1_U00_000_ContrastDown2.jpg",quality=80)

for num in range(5):
    value = (1 + (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-5/class-5_4901330523183_1_U00_000_angle%s.jpg' % (num+100))
  
for num in range(5):
    value = (1 - (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-5/class-5_4901330523183_1_U00_000_angle%s.jpg' % (num+200))


img2 = img.filter(ImageFilter.BLUR)
img2.save("C:/Users/Dsaito/Pictures/class-5/class-5_4901330523183_1_U00_000_BLUR.jpg")

img2 = img.filter(ImageFilter.MedianFilter(5))
img2.save("C:/Users/Dsaito/Pictures/class-5/class-5_4901330523183_1_U00_000_MEDIAN5.jpg")

img2 = img.filter(ImageFilter.MedianFilter(3))
img2.save("C:/Users/Dsaito/Pictures/class-5/class-5_4901330523183_1_U00_000_MEDIAN3.jpg")

img = Image.open( 'C:/Users/Dsaito/Pictures/class-6_4901330532734_1_U00_000.jpg' )

tmp = img.transpose(Image.FLIP_TOP_BOTTOM)
tmp.save('C:/Users/Dsaito/Pictures/class-6/FLIP_TOP_BOTTOM.jpg')

tmp = img.transpose(Image.FLIP_LEFT_RIGHT)
tmp.save('C:/Users/Dsaito/Pictures/class-6/FLIP_LEFT_RIGHT.jpg')

for num in range(36):
    tmp = img.rotate(num * 10)
    tmp.save('C:/Users/Dsaito/Pictures/class-6/class-6_4901330532734_1_U00_000_angle%s.jpg' % num)

# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(1.5)
img2.save("C:/Users/Dsaito/Pictures/class-6/class-6_4901330532734_1_U00_000_ContrastUp.jpg",quality=80)
# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(2.0)
img2.save("C:/Users/Dsaito/Pictures/class-6/class-6_4901330532734_1_U00_000_ContrastUp2.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.5)
img3.save("C:/Users/Dsaito/Pictures/class-6/class-6_4901330532734_1_U00_000_ContrastDown.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.3)
img3.save("C:/Users/Dsaito/Pictures/class-6/class-6_4901330532734_1_U00_000_ContrastDown2.jpg",quality=80)

for num in range(5):
    value = (1 + (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-6/class-6_4901330532734_1_U00_000_angle%s.jpg' % (num+100))
  
for num in range(5):
    value = (1 - (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-6/class-6_4901330532734_1_U00_000_angle%s.jpg' % (num+200))


img2 = img.filter(ImageFilter.BLUR)
img2.save("C:/Users/Dsaito/Pictures/class-6/class-6_4901330532734_1_U00_000_BLUR.jpg")

img2 = img.filter(ImageFilter.MedianFilter(5))
img2.save("C:/Users/Dsaito/Pictures/class-6/class-6_4901330532734_1_U00_000_MEDIAN5.jpg")

img2 = img.filter(ImageFilter.MedianFilter(3))
img2.save("C:/Users/Dsaito/Pictures/class-6/class-6_4901330532734_1_U00_000_MEDIAN3.jpg")

img = Image.open( 'C:/Users/Dsaito/Pictures/class-7_4901330532918_1_U00_000.jpg' )

tmp = img.transpose(Image.FLIP_TOP_BOTTOM)
tmp.save('C:/Users/Dsaito/Pictures/class-7/FLIP_TOP_BOTTOM.jpg')

tmp = img.transpose(Image.FLIP_LEFT_RIGHT)
tmp.save('C:/Users/Dsaito/Pictures/class-7/FLIP_LEFT_RIGHT.jpg')

for num in range(36):
    tmp = img.rotate(num * 10)
    tmp.save('C:/Users/Dsaito/Pictures/class-7/class-7_4901330532918_1_U00_000_angle%s.jpg' % num)

# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(1.5)
img2.save("C:/Users/Dsaito/Pictures/class-7/class-7_4901330532918_1_U00_000_ContrastUp.jpg",quality=80)
# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(2.0)
img2.save("C:/Users/Dsaito/Pictures/class-7/class-7_4901330532918_1_U00_000_ContrastUp2.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.5)
img3.save("C:/Users/Dsaito/Pictures/class-7/class-7_4901330532918_1_U00_000_ContrastDown.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.3)
img3.save("C:/Users/Dsaito/Pictures/class-7/class-7_4901330532918_1_U00_000_ContrastDown2.jpg",quality=80)

for num in range(5):
    value = (1 + (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-7/class-7_4901330532918_1_U00_000_angle%s.jpg' % (num+100))
  
for num in range(5):
    value = (1 - (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-7/class-7_4901330532918_1_U00_000_angle%s.jpg' % (num+200))


img2 = img.filter(ImageFilter.BLUR)
img2.save("C:/Users/Dsaito/Pictures/class-7/class-7_4901330532918_1_U00_000_BLUR.jpg")

img2 = img.filter(ImageFilter.MedianFilter(5))
img2.save("C:/Users/Dsaito/Pictures/class-7/class-7_4901330532918_1_U00_000_MEDIAN5.jpg")

img2 = img.filter(ImageFilter.MedianFilter(3))
img2.save("C:/Users/Dsaito/Pictures/class-7/class-7_4901330532918_1_U00_000_MEDIAN3.jpg")

img = Image.open( 'C:/Users/Dsaito/Pictures/class-8_4901330534516_1_U00_000.jpg' )

tmp = img.transpose(Image.FLIP_TOP_BOTTOM)
tmp.save('C:/Users/Dsaito/Pictures/class-8/FLIP_TOP_BOTTOM.jpg')

tmp = img.transpose(Image.FLIP_LEFT_RIGHT)
tmp.save('C:/Users/Dsaito/Pictures/class-8/FLIP_LEFT_RIGHT.jpg')

for num in range(36):
    tmp = img.rotate(num * 10)
    tmp.save('C:/Users/Dsaito/Pictures/class-8/class-8_4901330534516_1_U00_000_angle%s.jpg' % num)

# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(1.5)
img2.save("C:/Users/Dsaito/Pictures/class-8/class-8_4901330534516_1_U00_000_ContrastUp.jpg",quality=80)
# 画像のコントラストを上げる
iec1 = ImageEnhance.Contrast(img)
img2 = iec1.enhance(2.0)
img2.save("C:/Users/Dsaito/Pictures/class-8/class-8_4901330534516_1_U00_000_ContrastUp2.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.5)
img3.save("C:/Users/Dsaito/Pictures/class-8/class-8_4901330534516_1_U00_000_ContrastDown.jpg",quality=80)
# 画像のコントラストを下げる
iec2 = ImageEnhance.Contrast(img)
img3 = iec2.enhance(0.3)
img3.save("C:/Users/Dsaito/Pictures/class-8/class-8_4901330534516_1_U00_000_ContrastDown2.jpg",quality=80)

for num in range(5):
    value = (1 + (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-8/class-8_4901330534516_1_U00_000_angle%s.jpg' % (num+100))
  
for num in range(5):
    value = (1 - (num / 10) )
    img_resize = img.resize((int(img.width * value), int(img.height * value)))
    img_resize.save('C:/Users/Dsaito/Pictures/class-8/class-8_4901330534516_1_U00_000_angle%s.jpg' % (num+200))


img2 = img.filter(ImageFilter.BLUR)
img2.save("C:/Users/Dsaito/Pictures/class-8/class-8_4901330534516_1_U00_000_BLUR.jpg")

img2 = img.filter(ImageFilter.MedianFilter(5))
img2.save("C:/Users/Dsaito/Pictures/class-8/class-8_4901330534516_1_U00_000_MEDIAN5.jpg")

img2 = img.filter(ImageFilter.MedianFilter(3))
img2.save("C:/Users/Dsaito/Pictures/class-8/class-8_4901330534516_1_U00_000_MEDIAN3.jpg")