from flask import Flask, render_template, request

app = Flask(__name__,template_folder='templates')


#Anda bisa menambaahkan variabel global di luar method disini

#parsing variabel versi 1

#@app.route("/")
#def main():
#    web_title = "halaman utama"
 #   return f"<p>{web_title}Ini Home Main</p>"

#@app.route("/about")
#def about():
 #   return "<p>ini About</p> <br><a href='/'>Home</a></br>"
 

#======================================================================
#parsing variabel versi 2

#@app.route("/")
#def main():
#    web_title = "Halaman Home"
    #return f"<p>ini {web_title}</p>"
#    return render_template('home.html', web_title=web_title)

#@app.route("/about")
#def about():
#    web_title = "Halaman About"
    #return f"<p>ini {web_title}</p>"
#    return render_template('about.html', web_title=web_title)

#======================================================================

@app.route("/")
def main():
    web_title = "Halaman Utama"
    return render_template('home.html', web_title=web_title)

@app.route("/about")
def about():
    web_title = "Halaman About"
    return render_template('about.html', web_title=web_title)

@app.route("/usia", methods=['GET', 'POST'])
def cek_usia():
    web_title = "Cek Usia"
    
    if request.method == 'POST':
        tahun_lahir = request.form['tahun_lahir']
        tahun_sekarang = 2025
        usia = int(tahun_sekarang) - int(tahun_lahir)
        print(usia)
        return render_template('cek_usia.html', usia=usia)
        
    return render_template('cek_usia.html', usia=None)

