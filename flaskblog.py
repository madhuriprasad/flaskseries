from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] ='6e67596db08509e23ee4643ec652abb5'


posts=[
    {
        'author':'Corey Scafer',
        'title':'Blog post1',
        'content':'First post content ',
        'date_posted':'April 20,2018'
    },
    {
        'author':'James',
        'title':'Blog post2',
        'content':'Second post content ',
        'date_posted':'April 30,2018'
    }


]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts= posts)

@app.route("/about")
def about():
    return render_template('about.html',title= 'about')

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title= 'Register', form= form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title= 'Login', form= form)


if __name__=='__main__':
    app.run(debug= True)