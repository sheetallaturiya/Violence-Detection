import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask
from flask import render_template
from flask import request
import os
#@app.route('/')
#def home():
#	return render_template("index.html")

def get_shell_script_output(a):
    #stdout = check_output(['python Deploy.py',a]).decode('utf-8')
    stdout = subprocess.Popen(["python D://ViolenceDetection-master//Deploy.py",a],shell = True)
    return stdout

def get_shell_script_output1(b):
    stdout = check_output(['python Deploy.py',b]).decode('utf-8')
    return stdout

app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def test():
	return render_template("refpage.html")
	

@app.route('/module_run',methods=['GET', 'POST'])
def test1():
	return render_template("index.html")	
	
@app.route('/run',methods=['GET', 'POST'])
def home():
	#global video_file1
	if request.method == 'POST':
		video_file1 = request.form.get('video_file')   
		
	get_shell_script_output(str(video_file1))
	return render_template("index.html")

@app.route('/run1',methods=['GET','POST'])
def home1():
	if request.method == 'POST':
		ip1 = request.form.get('ip')

	get_shell_script_output1(str(ip1))
	return render_template("index.html")

app.run(debug=True) 
