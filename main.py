from flask import Flask, request

from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form= """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
          <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0"/>
            </div>
            <textarea type="text" name="text" >{text}</textarea>
            <input type="submit"/>
        </body>
    </html>

"""

@app.route("/")
def index():
    return form.format(text='')

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form["rot"]
    text = request.form["text"]

    rot = int(rot)

    rotated = rotate_string(text, rot)
    return form.format(text=rotated)

app.run()
