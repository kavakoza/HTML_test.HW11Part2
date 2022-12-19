from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route('/')
def get_list_of_candidates():
    candidates = utils.get_all_candidates()
    return render_template('list.html', candidates=candidates)


@app.route('/candidates/<int:id>')
def get_candidates(id):
    candidate = utils.get_candidate(id)
    return render_template('card.html', candidate=candidate)


@app.route('/search/<name>')
def get_candidates_by_name(name):
    candidates = utils.get_candidates_by_name(name)
    return render_template('search.html', candidates=candidates, count_candidates=len(candidates))


@app.route('/skill/<skills>')
def get_candidates_by_skill(skills):
    candidates = utils.get_candidates_by_skill(skills)
    return render_template('skill.html', candidates=candidates, count_candidates=len(candidates))


app.run(debug=True)
