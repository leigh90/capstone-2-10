from flask import Flask
import random 


app = Flask(__name__)

@app.route("/")
def hello_world():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    sumof = num1 + num2

    return f"<p>Congratulations you are customer number  {sumof} today!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)