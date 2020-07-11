from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email=data["email"]
        name=data["name"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f'\n{name},{email},{subject},{message}')
def write_to_csv(data):
    with open('database.csv',newline='',mode='a') as database2:
        email=data["email"]
        name=data["name"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=spamwriter = csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        write_to_csv(data)
        return render_template('/thankyou.html')
    else:
        return 'somthng went wrong'