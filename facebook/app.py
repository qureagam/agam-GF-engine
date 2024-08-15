from flask import Flask,render_template,request
from search import *
from wiki import *
from main import Nested
from images import *
import webbrowser

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/search' , methods =['POST','GET'])
def search():
    try:
      text = request.form.get('mm')
      if (text==""):
         return render_template('index.html')
      else:
       results = searching(text)
       a,b,c,j,k= Nested(text)
       for_youtube = text
       imag = Image(text)

       return render_template('result.html',
                              results = results,
                              ttp = "See results for "+text,
                              ttps = text,
                              image_page = a,
                              title_page = b,
                              link_page = c,
                              detail_page = j,
                              ff = k,
                              ytb = for_youtube,
                              i_img = imag
                              )
    except Exception as E:
        return render_template('net.html')
       
@app.route('/seeweb' , methods =['POST','GET'])
def research():
    try:
      tg = request.form.get('is')
      if (tg==""):
         return render_template('index.html')
      else:
        getset = {
          "search":searching(tg)
        }
        a,b,c,h,k= Nested(tg)
        for_youtube = tg
        imag = Image(tg)
        return render_template('result.html',
                              brid=getset['search'],
                              tpp1 =  "See results for "+tg,
                              image_page = a,
                              title_page = b,
                              link_page = c,
                              detail_page =h,
                              ff = k,
                              ytb = for_youtube,
                              i_img = imag,
                              ttps = tg
                              )
    except Exception as E:
       return render_template('net.html')
    
@app.route('/wiki' , methods =["POST","GET"])
def wikipedia():
   if request.method =="POST":
     for_wik = request.form.get('v')
     if (for_wik==""):
        return render_template('wikipedia.html')
     else:  
       result = wiks(for_wik)
       dt = ["1"]
       return render_template('wikipedia.html',data = result,dt=dt)
   else:
      return render_template('wikipedia.html')

webbrowser.open('http://127.0.0.1:2000/')
if __name__ == '__main__':
    app.run(debug=True , port=2000)