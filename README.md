# FashionAI
Aiding in the digitalisation of fashion e-commerce industry

## SECTION 1 : PROJECT TITLE
## Digitalising Fashion Retailing

---

## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT

<div style="text-align: justify"> The ease of access to digital technologies had been rapidly transforming the e-commerce industry for retailers and consumers. Then in 2019, boon or bane, COVID19 became a catalyst that spurred online sale more than ever before. With this impetus our project team had our eyes set on the fashion retail industry, and proposed three tracks in which the fashion industry could be transformed with the help of AI technologies: <br><br>
<ins>Generating Fashion Articles for Design Inspirations.</ins> In this track, we created a model that can auto-generate different fashion article designs. It served to jumpstart the design process with the design inspirations generated. We explored Generative Adversarial Networks (GAN), and ultimately used it to generate three different clothing designs; women’s tops, women’s dress, and men’s tops. <br><br>
<ins>Swapping Model Clothing Style for Product Marketing.</ins> Marketing and advertising are big components in the fashion industry. We hope to aid in this aspect by auto-swapping the clothing style of a human model so that a single photoshoot could possibly serve the purpose of advertising for multiple clothing styles. Cycle GAN was use for this purpose. We created and a trained a Cycle GAN that could swap between long-sleeves and short-sleeves clothing designs. <br><br>
<ins>Virtual Try-on for Consumers.</ins> A recent survey concluded that more than 50% of people are uncomfortable with using a dressing room right now . As such, we like to allow people to try on clothing virtually, in the safety of their own homes. We researched and explored using Conditional Analogy GAN to solve this problem. A CAGAN model was created and trained on a dataset comprising of women’s tops. The model allowed users to, virtually, swap their clothes to another. <br><br>
To demonstrate our ideas, we had overlaid the three models with an easy to use web app.
 </div>

---

## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name  | Student ID | Work Items (Who Did What) | Email (Optional) |
| :------------ |:---------------:| :-----| :-----|
| Chen Mingyi Edmund | A1234567Z | TBC | e0535232@u.nus.edu |
| Viswanathan Chandrashekar | A1234567Z | TBC | e0535243@u.nus.edu|
| Cheng Yunfeng | A1234567Z | TBC | e0535410@u.nus.edu|

---

## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

Link to final presentation video TBC

## SECTION 5 : USER GUIDE & Installation Guide 

Included in Project Report

**Remote Installation**

We have deployed our application for easy access at URL   https://prpm-ay2021-fashionai.herokuapp.com/

**Local Installation**

1.	This installation instruction is written on a Windows 10 OS.
2.	Download and install Anaconda Navigator via the   https://www.anaconda.com/products/individual
3.	Open Anaconda Navigator at start the Anaconda Prompt. The command prompt should display a “(base)”, this shows that you are using the base venv.
4.	The demo requires the following packages, do a pip install of them to the base venv if they are not already installed:
    *	Flask==1.1.2
    *	Flask-SQLAlchemy==2.4.4
    *	gunicorn==20.0.4
    *	Jinja2==2.11.2
    *	PyMySQL==0.10.0
    *	PyYAML==5.3.1
    *	SQLAlchemy==1.3.19
    *	psycopg2-binary==2.8.5
    *	Pillow==7.2.0
    *	Werkzeug==1.0.1
    *	tensorflow==2.3.0
    *	Keras==2.4.3
5.	Change directory to the location where you had placed the source codes. For this example, the command is: cd C:\Users\chen_\PycharmProjects\FashionAI
6.	Start the webapp backend with command: python fashionai.py flask start. The webapp be started locally at http://127.0.0.1:8080
7.	Navigate to your browser of choice (Firefox, Chrome, Edge, Internet Explorer) and enter the address above to go to the webapp.
8.	To end the webapp, enter the command: cntrl-c

**User Guide on Demo Webapp**
1.	To generate fashion articles, select the style of choice from the dropdown and click on Generate button. This will generate 8 articles of the selected style.
2.	To do virtual try-on. Browse to an image of the model with fashion article A, fashion article A standalone, and fashion article B standalone (for article B, you can also save and use the generated images). Click on Upload button, then Try-on button.
3.	To do style swapping. First navigate to the Style Swapper on the top menu bar. Browse to an image of the model with style A, select style A, and select the target style (style B). Click on Upload button, then Swap Style button.

---
## SECTION 6 : PROJECT REPORT / PAPER

`Refer to project report at Github Folder: ProjectReport`

---

