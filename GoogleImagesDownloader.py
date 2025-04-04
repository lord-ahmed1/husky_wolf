import requests
import re
import cv2 as cv
import os


class GoogleImagesDownloader:
    def __init__(self):
        self.url="https://www.google.com/search"
        self.headers= {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                     }
        self.image_processing=lambda x:x

    def download_images(self,search_query,save_directory):
        querystring = {"sca_esv":"fd0b6290a00de74f","sxsrf":"AHTn8zotrI0T_VoGeE0W1x4TL2rU49lVOg:1743427331857","q":search_query,"udm":"2","fbs":"ABzOT_CWdhQLP1FcmU5B0fn3xuWpA-dk4wpBWOGsoR7DG5zJBkzPWUS0OtApxR2914vrjk4ZqZZ4I2IkJifuoUeV0iQt1uortC3ar_w-QplxoC-7plla-IjYVHg0K4JVQal3-g-FOSEukDwbDcR4zflR5TsrPoHt8doB4e8l4MzJ_uH3UapDgrwQEOYfuVdzMYE7ItEoA0htn9F7ZCOv5DrgRSbXo_qLlQ","sa":"X","ved":"2ahUKEwjTi7r2tLSMAxV4TqQEHS0FLucQtKgLegQIEhAB","biw":"1848","bih":"966","dpr":"1"}
        response = requests.request("GET", self.url,  headers=self.headers, params=querystring,timeout=30)
        semi_filter=re.findall('"http.+?jpg',response.text)
   
        for N,to_be_processed in enumerate(semi_filter):
            try:
                link=self.extract_img_link(to_be_processed)
                filename=f"{search_query.replace(' ','_')}_{N}.jpg"
                self.save_img(link,filename,save_directory)
                self.convert_webp_to_jpg(filename,save_directory)
            except Exception as e:
                print(e)

            print(f"{(N/len(semi_filter))*100} % downloaded {N} images from {len(semi_filter)} image link:{link}")


    def extract_img_link(self,text):
        start_index=0
        for i in range(len(text)):
            substring=text[-i:(-i+4)]
            if substring=="http":
                start_index=len(text)-i
                break
        return text[start_index:]
    def save_img(self,download_url,filename,directory):
        response=requests.request("GET", download_url,  headers=self.headers,timeout=30)
        file=open(f"{directory}/{filename}", "wb")
        for byte in response:
            file.write(byte)
        file.close()
    def convert_webp_to_jpg(self,filename,directory):
        try:
            img=cv.imread(f"{directory}/{filename}")
            img=self.image_processing(img)
            cv.imwrite(f"{directory}/{filename}",img)
        except:
                os.remove(f"{directory}/{filename}")

    def create_image_processing(self,function):
        self.image_processing=function



        
     


