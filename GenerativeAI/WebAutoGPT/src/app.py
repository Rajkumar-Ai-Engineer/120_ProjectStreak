from helper import run 
from flask import Flask, request, render_template 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/submit",methods=["POST","GET"])
def webgpt():
    if request.method == "POST":
        userInput1 = request.form.get("userInput1")
        userInput2 = request.form.get("userInput2")
        
        if userInput1 and userInput2:
            try:
                response = run(query1=userInput1, query2=userInput2)
                return render_template("index.html", response=response)
            except Exception as e:
                return render_template("index.html", response=f"Error: {str(e)}")
        else:
            return render_template("index.html", response="Please provide both inputs")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)