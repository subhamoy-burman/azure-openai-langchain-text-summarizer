from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from Py_Langchain import ice_break_with_linkedin_profile

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form["name"]
    summary, profile_pic_url = ice_break_with_linkedin_profile(name=name)
    return jsonify(
        {
            "summary_and_facts": summary.to_dict(),
            "picture_url": "https://media.licdn.com/dms/image/v2/D5603AQF-RYZP55jmXA/profile-displayphoto-shrink_800_800/B56ZRi8g.aGsAc-/0/1736826818808?e=1746057600&v=beta&t=xe6NWXoJ-0DLjbKou59ezBOLxRSmq6I5BiLdRdAplak"
        }
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)