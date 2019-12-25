from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    lc = int(request.cookies.get('latestCompleted', 0))
    return render_template("index.html", latestCompleted=lc)

@app.route('/puzzle1')
def puzzle1():
    return render_template("puzzle1.html", message="nice")



@app.route('/puzzle1/check', methods=['POST'])
def checkPuzzle1():
    proposedSol = request.json.get('ans') # If not found, defaults to NoneType.

    if proposedSol == "hint":                return "Nice try."
    elif proposedSol == "the actual answer": return "C"
    else:                                    return "Not exactly... try again"


@app.route('/puzzle2')
def puzzle2():
    if 'puzzlecookie' in request.cookies:
        return 'Hello puzzle2'
    return 'Solve the other puzzle first.'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)