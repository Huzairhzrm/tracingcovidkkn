from flask import Flask, redirect, url_for, request, render_template
import jinja2
import json
import time
import dataHandler
import graph_module

app=Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')
	'''
	if request.method=='POST':
		name=request.form['dataBaru']
		return redirect(url_for('newData'))
	else:
		name=request.args.get('dataBaru')
		return redirect(url_for('newData'))
	'''
	
@app.route('/newData')
def newData():
	return render_template('newData.html')

@app.route('/newData', methods=['POST'])
def newDataPost():
	if request.method=='POST':
		'''
		nama=request.form['nama']
		identitas=request.form['identitas']
		noID=request.form['noID']
		lahir=request.form['lahir']
		jk=request.form['jk']
		hasilTest=request.form['hasilTest']
		alamat=request.form['alamat']
		kontak=request.form['kontak']
		#datadict={nama: data}
		
		data={nama:[identitas,noID,lahir,jk,hasilTest,alamat]}
		adjdata={nama:kontak}
		'''
		
		with open('file.json', 'a') as f:
			json.dump(request.form, f, indent=4)
			
		#return render_html('your_template.html')
		
		'''
		with open('data.json', 'w') as f:
			json.dump(data, f, indent=4)
		'''
		
		return redirect(url_for('success'))
		
	#return newData()
	'''
	else:
		nama=request.args.get('nama')
		return redirect(url_for('success'))
	'''
	
@app.route('/success')
def success():
	print('Data berhasil terinput. Mengembalikan ke halaman awal . . .')
	return redirect(url_for('home')) #render_template('home.html')
	
if __name__=='__main__':
	app.run(debug=True)