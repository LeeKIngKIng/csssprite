import os
from PIL import Image

# 横向拼接
print('请输入文件夹地址：')
path = input()
files = os.listdir(path)
length = len(files)

image=Image.open(path+'/'+files[0])
UNIT_WIDTH, UNIT_HEIGHT=image.size
TARGET_WIDTH = length * UNIT_WIDTH # 拼接完后的横向长度

# for root, dirs, files in os.walk(path):     
# 	for f in files :
# 		images.append(f)

files.sort(key= lambda x:int(x[:-4]))
imagefile = []
for j in range(length):
	imagefile.append(Image.open(path+'/'+files[j]))
if "png" in files[0]:
	target = Image.new('RGBA', (TARGET_WIDTH, UNIT_HEIGHT), (255,255,255))    
else:
	target = Image.new('RGB', (TARGET_WIDTH, UNIT_HEIGHT), (255,255,255))    
left = 0
right = UNIT_WIDTH
i=1
for image in imagefile:     
	target.paste(image, (left, 0, right, UNIT_HEIGHT))# 将image复制到target的指定位置中
	left += UNIT_WIDTH # left是左上角的横坐标，依次递增
	right += UNIT_WIDTH # right是右下的横坐标，依次递增
	print(str(int(i/length*100))+'%')
	i+=1

if target.mode=='RGBA':
	target=target.quantize(256)
	target.save(path+'/result.png', 'PNG')
else:
	target=target.convert('RGB')
	target.save(path+'/result.jpg', 'JPEG')


