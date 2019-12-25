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
    msg = ""

    if sol1 == "portland":
        sol1Correct = True
    if sol2 in ["纪念馆", "jìniànguǎn", "jinianguan"]:
        sol2Correct = True

    if sol1Correct and sol2Correct: return "C" # Immediately return if the answer was given.

    if sol1 == "artridge":    msg += "Is that the name of a city?"
    elif sol1 == "partridge": msg += "Ok, maybe Partridge could be the name of a city. But that's not where S.A.N.T.A. is headed first."
    elif sol1 == "":          msg += ""
    elif sol1Correct:         msg += "The location is correct."
    else:                     msg += "That's not the right location."

    if sol2 in ["morial", "morialinmandarin"]:        msg += " Now that you think of it, you remember the key to the activation phrase started with \"me\"."
    elif sol2 in ["memorial", "memorialinmandarin"]:  msg += " Almost. It looks like you found the *key* to the deactivation phrase."
    elif sol2 == "":                                  msg += ""
    elif sol2Correct:                                 msg += " The deactivation phrase is correct."
    else:                                             msg += " That's not the right deactivation phrase."

    return msg

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
