from flask import Flask, render_template, request
from analyzer import analyze_code
from ai import explain_code

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    code = ""   
    steps = []
    flow = []
    simulation = []
    execution_lines = []
    ai_explanation = ""

    if request.method == "POST":

        code = request.form.get("code")
        action = request.form.get("action")

        steps, flow, simulation, execution_lines = analyze_code(code)

        if action == "ai":
            ai_explanation = explain_code(code)

    return render_template(
        "index.html",
        code=code,
        steps=steps,
        flow=flow,
        simulation=simulation,
        execution_lines=execution_lines,
        ai_explanation=ai_explanation
    )

if __name__ == "__main__":
    app.run(debug=True)