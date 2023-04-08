from flask import Flask, request, render_template, jsonify
from .ai_processing import process_ai_input
import os
from dotenv import load_dotenv

app = Flask(__name__)
ai_summaries = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("input")
        ai_summary = process_ai_input(user_input)
        return render_template("index.html", ai_summary=ai_summary)
    return render_template("index.html", ai_summaries=ai_summaries)

@app.route('/api/report', methods=['POST'])
def create_report():
    global ai_summaries
    data = request.get_json()
    summary = data.get('summary')
    ai_summary = process_ai_input(summary)

    # 如果有重复，自动覆盖
    ai_summaries = list(set(ai_summaries))
    ai_summaries.append(ai_summary)
    
    return jsonify(ai_summary=ai_summary)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), ssl_context=("cert.pem", "key.pem"))
