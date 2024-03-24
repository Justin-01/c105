import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

image = cv2.imread(images[2])
height, width, channels = image.shape
video = cv2.VideoWriter('Sunset.avi', cv2.VideoWriter_fourcc(*'MPEG'), 5, (width, height))

for i in range(count-1,0,-1):
    image = cv2.imread(images[i])
    video.write(image)