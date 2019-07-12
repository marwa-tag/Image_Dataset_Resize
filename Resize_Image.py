import os
from PIL import Image
from pathlib import Path
image_list = {}
resized_image = []
i=1
data_folder= input("Please, enter the absolute path of the data folder:")
new_folder = input("Please, enter the absolute path of the new folder that will hold the generated images:")
width = int(input("Please, enter the required image width and height respectively:"))
height = int(input())
for root, dirs, files in os.walk(data_folder):

   for file in files:
        image_list = os.path.join(root,file)
        print(image_list)
        img = Image.open(image_list)
        im2 = img.resize((width,height))
        resized_image.append(im2)
        fp = '{}\{}{}'.format(new_folder,i, '.jpeg')
        print(fp)
        p = Path(fp)
        im2.save(p)
        i+=1
print('Done')
