from GoogleImagesDownloader import GoogleImagesDownloader
import cv2 as cv
downloader=GoogleImagesDownloader()
import os

def image_processing(image):
    return cv.resize(image,(300,300))

downloader.create_image_processing(image_processing)
keywords=["realistic","in woods","at the zoo","running","attacking","scary","at night","eye","ear","fur"]



keywords=["pet","","in forest","hiking"]

animals=["wolf","husky"]
#create folders for each animal
for animal in animals:
    try:
        os.makedirs(f"data/train/{animal}")
    except:
        pass

for animal in animals:
    try:
        os.makedirs(f"data/test/{animal}")
    except:
        pass

for keyword in keywords:
    for animal in animals:
        search=keyword+" "+animal
        print(search)
        downloader.download_images(search,f"data/test/{animal}")
