from PIL import Image

def resize_image(image):
    print("resiiiiiiiziiing")
    with Image.open(image) as img:
        print("img.resize((606, 666))")
        img = img.resize((606, 666), Image.ANTIALIAS)
        img.save(image.path)