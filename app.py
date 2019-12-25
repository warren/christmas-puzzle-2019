from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    lc = int(request.cookies.get('latestCompleted', 0))
    return render_template("index.html", latestCompleted=lc)

@app.route('/puzzle1')
def puzzle1():
    return render_template("puzzle1.html")



@app.route('/puzzle1/check', methods=['POST'])
def checkPuzzle1():
    proposedSol = request.json.get('ans') # If not found, defaults to NoneType.

    if proposedSol == "iHBYCUbbZeo":     return "Yeah... it's not that simple. 🙃"
    elif proposedSol == "hint":          return "Nice try."
    elif proposedSol in ["fifty", "50"]: return "C"

    return "Not exactly... try again"


@app.route('/puzzle2')
def puzzle2():
    lc = int(request.cookies.get('latestCompleted', 0))
    if lc < 1:
        return "Solve the other puzzle first."
    return render_template("puzzle2.html")

@app.route('/puzzle2/check', methods=['POST'])
def checkPuzzle2():
    sol1 = request.json.get('ans1') # If not found, defaults to NoneType.
    sol2 = request.json.get('ans2') # If not found, defaults to NoneType.
    sol1Correct, sol2Correct = False, False
    additionalMsg = ""

    if sol1 == "brilliant":
        sol1Correct = True
    if sol2 in ["纪念馆", "jìniànguǎn", "jinianguan"]:
        sol2Correct = True

    if sol1Correct and sol2 == "memorial": return "Your first answer is correct. Your second answer is close."
    elif sol1Correct: return "Your first answer is correct. What about the second?"
    elif sol2Correct: return "Your second answer is correct. What about the first?"
    elif sol1Correct and sol2Correct: return "C"

    return "Not exactly... try again"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


@app.route('/puzzle3', methods=["GET"])
def puzzle3():
    lc = int(request.cookies.get('latestCompleted', 0))
    if lc < 2:
        return "Solve the other puzzle first."
    return render_template("puzzle3.html", solved = False)


@app.route('/puzzle3/check', methods=["POST"])
def checkPuzzle3():

    answers = ["scotch", "the scotch", "scotch game", "scotch opener"]
    if not request.json.get('ans'):
        return "At least TRY."
    if request.json.get('ans').lower() in answers:
        return "C"
    else:
        return "Not exactly... try again"

@app.route('/puzzle4', methods=["GET"])
def puzzle4():
    lc = int(request.cookies.get('latestCompleted', 0))
    if lc < 3:
        return "Solve the other puzzle first."
    return render_template("puzzle4.html")

@app.route('/puzzle4/check', methods=["POST"])
def checkPuzzle4():

    answers = ["an enthusiastic mountain climber", "enthusiastic climber", "mountain climber", "climber"]
    if not request.json.get('ans'):
        return "At least TRY."
    if request.json.get('ans').lower() in answers:
        return "C"
    else:
        return "Not exactly... try again"







