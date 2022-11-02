from flask import Flask, render_template
from views import views, app_views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdlkqwe1098283019wjfañknvmq24\9e!"#!#%#$!"ret25235"#$"#$23'
app.register_blueprint(app_views)
app.register_blueprint(views)

@app.route('/')
def inicio():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
