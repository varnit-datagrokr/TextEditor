from flask import Flask, render_template, request
import os
import difflib

# class FormView():
#     def post(self,)



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    filename = request.form['filename']
    if os.path.isfile(filename):
        with open(filename,'r') as rf:
            old_data = rf.read()
        d = difflib.Differ()
        diff = d.compare(old_data.split('\n'),text.split('\n'))
        with open(filename,'w') as wf:
            wf.write(text)
        return render_template('form.html',text=diff,filename=filename)
    else:
        with open(filename,'w') as wf:
            wf.write(text)
        return "File saved at location: " + filename

app.debug = True
if __name__ == '__main__':
    app.run(host='localhost', port=5000)