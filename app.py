from flask import Flask, request, render_template
from datetime import datetime
import json
from model import get_category, plot_category

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def fitur():
    if request.method == 'POST':
        img = request.files['file']
        image_category = get_category(img)
        now = datetime.now()
        current_time = now.strftime("%H-%M-%S")
        plot_category(img, current_time)
        return render_template('result.html', category=image_category, current_time=current_time)



@app.route("/about/")
def about():
    return render_template("about.html",)

@app.route("/turtle")
def turtle():
    data = []
    with open('static\data.json') as file:
        data = json.load(file)
        print(data)
        return render_template(    
            "penyu.html",
            penyu = data
    )


    
if __name__ == "__main__":
    app.run(debug=True)