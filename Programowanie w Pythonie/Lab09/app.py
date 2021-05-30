from flask import Flask, render_template, request, url_for, redirect


data = [
    {"q":"Jaki to framework:",
     "o":["Django","Flask","Inny"],
     "a": "Flask"},
    {"q":"Pyttanie:",
     "a": "Odpowiedz"}
]
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.methond == 'POST':
        ans = request.form
        print(ans)
        err = False
        for qnr, a in ans.items():
            if a != data[int(qnr)]['a']:
                err = True
        if err:
            print("Error")
        else:
            print("ok")
        return redirect(url_for('index'))
    return render_template('index.html',questions=data)
if __name__  == "__main__":
    app.run()