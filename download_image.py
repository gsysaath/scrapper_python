import wget


def download_image(image_url, universal_product_code):
    # Download image to ./images path

    img_name = f'./images/{ universal_product_code }.jpg'
    image_filename = wget.download(image_url, img_name)
    print('Image Successfully Downloaded: ', image_filename)
