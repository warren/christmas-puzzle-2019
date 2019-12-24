from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", message="nice")

@app.route('/puzzle1')
def puzzle1():
    return render_template("puzzle1.html", message="nice")

@app.route('/puzzle2')
def puzzle2():
    if 'puzzlecookie' in request.cookies:
        return 'Hello puzzle2'
    return 'Solve the other puzzle first.'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)