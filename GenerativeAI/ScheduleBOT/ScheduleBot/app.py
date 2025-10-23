from flask import Flask,request,jsonify,render_template
from main import run
app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/submit",methods=["POST","GET"])
def Schedulebot():
    
    if request.method =="POST":
        userInput = request.form.get("userInput1")
        
        if userInput:
            try:
                response = run(question=userInput)
                return render_template("index.html", response=response.content)
            except Exception as e:
                return render_template("index.html", response=f"Error: {str(e)}")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)