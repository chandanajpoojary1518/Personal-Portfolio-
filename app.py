from flask import Flask, render_template   #flask -> library; Flask-> class;render_templates is method in flask lib.
app = Flask(__name__)  #app is object of class Flask ; 
@app.route('/') #end ponit of router
#above 3 lines are common flask statements

def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
