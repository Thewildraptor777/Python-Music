from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'John Doe'
    age = 25
    occupation = 'Software Engineer'
    
    return render_template('index.html', name=name, age=age, occupation=occupation)

if __name__ == '__main__':
    app.run()
