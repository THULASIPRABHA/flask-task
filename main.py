from flask import *
import re
#using regex for multidelimiter split()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/",methods=['GET', 'POST'])
def func():
    if request.method == 'POST':
        text=request.form["userinput"]
        if request.form.get("WordCount"):
            output=len(text.split())
        elif request.form.get("title1"):
            output=text.title()
        elif request.form.get("unique"):
            output=",".join(set(re.split('[,\s]\s*',text.lower())))
    return render_template("index.html", output=output)


if __name__=="__main__":
    app.run(debug=True,port=5000, host='0.0.0.0')
