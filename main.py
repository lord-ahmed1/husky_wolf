from GoogleImagesDownloader import GoogleImagesDownloader
import cv2 as cv
downloader=GoogleImagesDownloader()

def image_processing(image):
    return cv.resize(image,(200,200))

downloader.create_image_processing(image_processing)
keywords=["real","wild","in wild","front","side","back","top","bottom","eye","ear"].
animals=["wolf","husky"]

for keyword in keywords:
    for animal in animals:
        search=keyword+" "+animal
        print(search)
        downloader.download_images(search,f"data/train/{animal}")
