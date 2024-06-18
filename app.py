from flask import Flask, render_template

app = Flask(__name__)

# Define Application name
app_name = "EasyTax!"

@app.route('/')
def index():
    return render_template('index.html', app_name=app_name,)

if __name__ == '__main__':
    app.run(debug=True, port=5000)