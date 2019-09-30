from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    f = open("data.txt", "r")
    reader = f.readlines()
    for i in reader:
        if 'mac' in i:
            num = i.split(' ')[1]
        elif 'air' in i:
            air = i.split(' ')[1]
    return render_template("index.html", num=num, air=air)


if __name__ == '__main__':
    app.run(debug = True)
