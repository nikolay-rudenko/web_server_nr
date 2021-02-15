from flask import Flask, request, url_for, redirect, render_template
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('db.txt', 'a') as db1:
        email = data['email']
        subject = data['subject']
        message = data['message']

        db1.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('db.csv', 'a', newline='') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']

        csv_writer = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to db'
    else:
        return 'something went wrong'




