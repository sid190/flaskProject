from flask import Flask, render_template
from forms import Signupform

app=Flask(__name__)
app.config["Secret_Key"]="jinjaexc"

@app.route('/about/<username>')
def hello_about(username):
    return f"Hello World!, This is the about page which contains {username}"

@app.route('/blog')
def hello_blog():
    comps = [{'title': 'FIFA_WC', "winner": "France"}, {"title": "Euro_2020", "winner": "Italy"},
               {"title": "Copa_America", "winner": "Argentina"}]
    return render_template("Home.html", author="Siddharth", Euro=False, comps=comps)

@app.route('/signup')
def signup():
    form = Signupform()
    return render_template("signup.html", form=form)

if __name__=="__main__":
    app.run()


