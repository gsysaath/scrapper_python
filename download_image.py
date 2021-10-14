import wget

# Download image to ./images path
def download_image(image_url, book_title):
    image_filename = wget.download(image_url, f'./images/{ book_title }.jpg')
    print('Image Successfully Downloaded: ', image_filename)