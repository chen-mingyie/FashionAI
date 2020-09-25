from random import randint
from app import app
from flask import request, Markup, render_template, jsonify, redirect
from app.model.imageutils import save_image, get_tryon_images, get_styleswap_image
from app.business.article_generator import articleGenerator
from app.business.virtual_tryon import viton

articleGenerator = articleGenerator()
viton = viton()

@app.route("/")
@app.route("/virtualtryon", methods=["GET", "POST"])
def virtualtryon():
    nbrToGen = 8
    if 'generate-btn' in request.values:
        styleToGen = request.values['style-gen']
        articleGenerator.generateImages(nbrToGen, styleToGen)
    generated = ['/static/img/generated/' + str(i) + '.jpg?' + str(randint(0, 9999)) for i in range(nbrToGen)]

    if 'upload-btn' in request.values:
        # images are save in /static/img/. Filenames are 'human-article-A.jpg', 'article-A.jpg', and 'article-B.jpg'
        images = save_image(request)
    human_in_A = '/static/img/human-article-A.jpg?' + str(randint(0, 9999))
    article_A = '/static/img/article-A.jpg?' + str(randint(0, 9999))
    article_B = '/static/img/article-B.jpg?' + str(randint(0, 9999))

    if 'swap-article-btn' in request.values:
        viton.generate_new_image()
        # code to swap fashion article. Store image in '/static/img/human-article-B.jpg'
        input_img = get_tryon_images()

    human_in_B = 'static/img/generated/human-article-B.jpg?' + str(randint(0, 9999))

    return render_template("virtualtryon.html", generated0_img=generated[0], generated1_img=generated[1],
                           generated2_img=generated[2], generated3_img=generated[3], generated4_img=generated[4],
                           generated5_img=generated[5], generated6_img=generated[6], generated7_img=generated[7],
                           human_article_A_img=human_in_A, article_A_img=article_A, article_B_img=article_B, human_article_B_img=human_in_B)

@app.route("/styleswapper", methods = ["GET", "POST"])
def styleswapper():
    if 'upload-btn' in request.values:
        # images are save in /static/img/. Filenames are 'human-style-A.jpg'
        input_imgs = save_image(request)
    human_in_A = '/static/img/human-style-A.jpg?' + str(randint(0, 9999))

    if 'swap-style-btn' in request.values:
        # code to swap fashion styles. Store image in '/static/img/human-style-B.jpg'
        style_A = request.values['style-A']
        style_B = request.values['style-B']
        input_img = get_styleswap_image()
    human_in_B = 'static/img/human-style-B.jpg?' + str(randint(0, 9999))

    return render_template("styleswapper.html", human_style_A_img=human_in_A, human_style_B_img=human_in_B)


@app.route("/login", methods=["POST", "GET"])
def showlogin():
    return render_template("login.html")