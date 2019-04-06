from flask import Flask,request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
     <form method="post">
        <label>Rotate By:</label>
        <input type="text" name="rot" value="0"/>
        <input type="textarea" name="textarea"/>
        <input type="submit"/>


    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    msg = request.form['textarea']
    encrypted = "<h1>" + rotate_string(msg, rot) + "</h1>"
    
    return encrypted


@app.route("/")
def index():
    return form

app.run()