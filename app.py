from flask import Flask, render_template, redirect, request, url_for, jsonify
from grepper import fetch, search_answer, similar
import ast
import urllib.parse

app = Flask(__name__)

@app.route('/')
def home():
  terms_others = fetch.fetch_terms()
  return render_template('index.html', all_terms=terms_others)

@app.route('/search')
def search():
  answers = request.args.getlist('answers')
  answers = [ast.literal_eval(item) for item in answers]

  sq = request.args.getlist('sq')
  sq = [ast.literal_eval(item) for item in sq]

  return render_template('search.html', answers=answers, sq=sq)

@app.route('/getanswers', methods=['POST'])
def getanswer():
  term = request.form['search_term']
  search_result = search_answer.get_answers(term)
  squeries = similar.similar_queries(term)
  # return jsonify({'term': term, 'answers': search_result, 'sq': squeries})
  return redirect(url_for('search', term=term, answers=search_result, sq=squeries))


@app.route('/need-answers')
def need_answers():
  terms_others = fetch.fetch_terms()
  return render_template('need_answers.html', all_terms=terms_others)

if __name__ == "__main__":
  app.run(debug=True)