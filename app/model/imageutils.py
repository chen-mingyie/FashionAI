from app import app
from werkzeug.utils import secure_filename
from PIL import Image
import os

def allowed_image(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_image_filesize(filesize):
    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False

def save_image(request) -> {}:
    images = {}
    if request.method == "POST" and request.files and "filesize" in request.cookies and allowed_image_filesize(request.cookies["filesize"]):
        for imgName in request.files.keys():
            image = request.files[imgName]
            if image.filename != "" and allowed_image(image.filename):
                images[imgName] = image
                filename = secure_filename(image.filename)
                ext = filename.rsplit(".", 1)[1]
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], imgName + "." + ext))

    return images

def get_tryon_images() -> []:
    images = []
    imgfolder = 'app/static/img/'
    images.append(Image.open(imgfolder + 'human-article-A.jpg'))
    images.append(Image.open(imgfolder + 'article-A.jpg'))
    images.append(Image.open(imgfolder + 'article-B.jpg'))
    return images

def get_styleswap_images() :
    imgfolder = 'app/static/img/'
    image = Image.open(imgfolder + 'human-style-A.jpg')
    return image