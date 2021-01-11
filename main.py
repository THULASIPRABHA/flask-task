from flask import *
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/",methods=['GET','POST'])
def func():
    if request.method == 'POST':
        text=request.form["userinput"]
        if request.form.get("WordCount"):
            output=len(text.split())
        elif request.form.get("title1"):
            lst = [word[0].upper() + word[1:] for word in text.split()]
            text = " ".join(lst)
            output=text
        elif request.form.get("unique"):

           list_str = text.lower().split()
           unique_words = []
           for word in list_str:
               if word not in unique_words:
                   unique_words.append(word)
            output=unique_words
        
    return render_template("index.html", output=output)

            
    


if __name__=="__main__":
    app.run(debug=True)
