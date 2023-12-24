from flask import Flask
from flask import request
from flask import render_template_string
from flag import FLAG

app = Flask(__name__)
app.config['FLAG']=FLAG

@app.route('/')
def index():    
    name = request.args.get('name') 
    if name:
       template = f"<h1>- Hello {name}! what do you think about my app</h1>"
       return render_template_string(template)
    else :
        return "<h1> i made my first web app using flask can you give it a test<br>try passing a parameter! ?name </h1>"
if __name__ =='__main__':
    app.run(debug=False)