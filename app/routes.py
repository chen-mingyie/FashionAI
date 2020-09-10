from random import randint
from app import app
from flask import request, Markup, render_template, jsonify, redirect
from app.model.imageutils import save_image, get_tryon_images, get_styleswap_images

@app.route("/")
@app.route("/virtualtryon", methods=["GET", "POST"])
def virtualtryon():
    if 'generate-btn' in request.values:
        a = 1
        # code to generate fashion article. Store image in '/static/img/generated.jpg'
    generated = '/static/img/generated.jpg?' + str(randint(0, 9999))

    if 'upload-btn' in request.values:
        # images are save in /static/img/. Filenames are 'human-article-A.jpg', 'article-A.jpg', and 'article-B.jpg'
        images = save_image(request)
    human_in_A = '/static/img/human-article-A.jpg?' + str(randint(0, 9999))
    article_A = '/static/img/article-A.jpg?' + str(randint(0, 9999))
    article_B = '/static/img/article-B.jpg?' + str(randint(0, 9999))

    if 'swap-article-btn' in request.values:
        # code to swap fashion article. Store image in '/static/img/human-article-B.jpg'
        input_img = get_tryon_images()
    human_in_B = 'static/img/human-article-B.jpg?' + str(randint(0,9999))

    return render_template("virtualtryon.html", generated_img=generated, human_article_A_img=human_in_A, article_A_img=article_A,
                                                article_B_img=article_B, human_article_B_img=human_in_B)

@app.route("/styleswapper", methods = ["GET", "POST"])
def styleswapper():
    if 'upload-btn' in request.values:
        # images are save in /static/img/. Filenames are 'human-style-A.jpg'
        input_imgs = save_image(request)
    human_in_A = '/static/img/human-style-A.jpg?' + str(randint(0, 9999))

    if 'swap-style-btn' in request.values:
        # code to swap fashion styles. Store image in '/static/img/human-style-B.jpg'
        input_img = get_styleswap_images()
    human_in_B = 'static/img/human-style-B.jpg?' + str(randint(0,9999))

    return render_template("styleswapper.html", human_style_A_img=human_in_A, human_style_B_img=human_in_B)


@app.route("/login", methods=["POST", "GET"])
def showlogin():
    return render_template("login.html")