from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/process", methods=['POST'])
def process():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if email == "polivares@codingdojo.cl" and password == "123456789":
            # Ahora, como recibí un email y una contraseña correctamente
            # y ambas corresponde a las del usuario, se creará una nueva sesión
            session["email"] = email
            session["password"] = password 
            return redirect("/profile")
    return redirect("/")


@app.route("/profile", methods=["GET"])
def profile():
        if session.get("email") == None:
            return redirect('/login')
        else:
            print(session["email"])
            return render_template("profile.html", email=session["email"], pwd=session["password"])
            

@app.route('/logout')
def logout():
    # forma correcta de liberar sesión
    session.clear()

    return redirect('/login')



if __name__ == '__main__':
    app.run(debug=True)
