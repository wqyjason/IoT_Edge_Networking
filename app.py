from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def hello():

    f = open("data.txt", "r")
    reader = f.readlines()
    for i in reader:
        if 'mac' in i:
            num = i.split(' ')[1]
        elif 'air' in i:
            air = i.split(' ')[1]
        elif 'predict' in i:
            predict = i.split(' ')[1]

    return render_template("index.html", num=num, air=air, predict=predict)




if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug = True)
