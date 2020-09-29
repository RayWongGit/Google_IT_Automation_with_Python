# Automate Updating Catalog Information

## About the Project

This project is the capstone project of the [Google IT Automation with Python Professional Certificate](https://www.coursera.org/professional-certificates/google-it-automation) offered on Coursera. 

## Introduction
An online fruits store needs to develop a system that will update the catalog information with data provided by the suppliers. The suppliers send the data as large images with an associated description of the products in two files (.tiff for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. 


## Tasks

### Working with Supplier Images

In this section, I will write a Python script named **changeImage.py** to process the supplier images. I will be using the **PIL library** to update all images within the directory to the following specifications:

- Size: Change image resolution from 3000x2000 to 600x400 pixel
- Format: Change image format from .TIFF to .JPEG
 
### Uploading images to web server

Now, I will have to upload these modified images to the web server that is handling the fruit catalog. To do that, I will write a script named **supplier\_image\_upload.py** that takes the jpeg images from the supplier-data/images directory that I've processed previously and uploads them to the web server fruit catalog with **Python requests module**

### Uploading the descriptions

To add fruit images and their descriptions from the supplier on the fruit catalog web-server, I will write a Python script named **run.py** which uses **Python requests library** to upload all the required fields to the web-server.




