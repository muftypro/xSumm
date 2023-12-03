from flask import Flask, request, render_template
import gensim
from gensim.summarization import summarize
import spacy

app = Flask(__name__)
nlp = spacy.load('en_core_web_sm')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        summarized_text = summarize(input_text)
        return render_template('index.html', input_text=input_text, summarized_text=summarized_text)
    return render_template('index.html', input_text='', summarized_text='')

if __name__ == '__main__':
    app.run(debug=True)
