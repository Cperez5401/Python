from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def mainPage():
    return "Hello World!"

@app.route('/play')
def play():
    return render_template('index.html')


@app.route('/play/<numBoxes>')
def boxesValue(numBoxes):
    repeat = int(numBoxes)
    return render_template('index2.html', repeat=repeat)


@app.route("/play/<numBoxes>/<color_change>")
def box_color(numBoxes,color_change):
    repeat = (int(numBoxes))
    colorChange = color_change
    return render_template('index3.html', repeat = repeat, colorChange = colorChange )

if __name__=="__main__":
    app.run(debug=True)