from PIL import Image, ImageFont, ImageDraw
from PIL import Image
from io import BytesIO
from flask import Flask, jsonify, render_template, send_file, abort, redirect, url_for
from threading import Thread
import random
import string

app = Flask('')


@app.route('/')
def sup():
    return redirect(url_for('give_the_c'))


s1 = string.ascii_letters
s3 = string.digits
s4 = string.hexdigits
s = []
s.extend(list(s1))
# s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
randm1 = "".join(random.sample(s, 15))
randm2 = "".join(random.sample(s, 38))


@app.route("/gimme/some/captcha")
def give_the_c():
    result_random_Stuff = "".join(random.sample(s, 6))
    result = {
        "asked_query": result_random_Stuff,
        "answer_to_captcha": result_random_Stuff,
        "img_url":
        f"https://Captcha-Image-Api.dhruvnation1.repl.co/captchame/{randm1}{result_random_Stuff}{randm2}",
        "font": "arial.ttf",
        "credits": "© Dhruv"
    }
    return jsonify(result)


@app.route(f'/captchame/{randm1}<string:a>{randm2}')
def imagemal(a):
    image = Image.open('captchimage.jpg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 35)
    points = 86, 29
    text = a
    draw.text(points, text, "black", font=font)
    image.save('resulted_captcha.jpg')
    image_file = 'resulted_captcha.jpg'

    try:
        return send_file(image_file)
    except:
        abort(404)


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    server = Thread(target=run)
    server.start()
