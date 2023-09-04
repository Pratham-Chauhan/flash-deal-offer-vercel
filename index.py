from flask import Flask, render_template
import otipy_scrape as otp
import subprocess

# run scraping process in backgroud 
# subprocess.Popen(["rm","-r","some.file"]) 
# print(otp.create_graph())
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', menu_items=otp.create_graph())

if __name__ == '__main__':
    app.run(debug=True)
