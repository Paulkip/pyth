from flask import Flask, render_template
import pytube


#print(videoo
app = Flask(__name__)
@app.route("/")
def home():
    url = 'https://www.youtube.com/watch?v=E_5d-jPeIVg'
    youtube = pytube.YouTube(url)
    youtube.streams.filter(res="144p").first().download()
    return render_template('index.html', paul="d")

if(__name__=="__main__"):
    app.run()