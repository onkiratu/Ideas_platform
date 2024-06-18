from my_app import app, db
from flask import render_template, url_for, redirect, flash
from my_app.forms import LoginForm, SignUpForm, OrderForm, PaymentForm 
from my_app.models import User, Order, Payment
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/")
def index():
    return render_template("index.html", show_navbar=True)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()       #search users 

        if user:
            if password == user.password:
                login_user(user)
                return redirect(url_for("dashboard"))    

            else:
                flash("Wrong password!")
                return redirect(url_for("login"))
        else:
            flash("User does not exist!")        
            return redirect(url_for("login"))

                

    return render_template("login.html", form=form )


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    users = User.query.all()

    #capturing form data
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        print(firstname, lastname)

        #create an instance of user
        user = User(firstname=firstname, lastname=lastname, username=username, email=email, password=password)
        db.session.add(user) 
        db.session.commit()
        flash("user created")

        return redirect(url_for("login"))

    flash("user not created")    
    return render_template("signup.html", form=form, users=users)


@app.route("/orders", methods=["GET", "POST"])
def orders():
    form = OrderForm()
    
    if form.validate_on_submit():
        type = form.type.data
        headline = form.headline.data
        keywords = form.keywords.data
        description = form.description.data
        wordcount = form.wordcount.data
        email = form.email.data
        price = form.price.data

        order = Order(type=type, headline=headline, keywords=keywords, description=description, wordcount=wordcount, email=email, price=price)
        db.session.add(order)
        db.session.commit()
        flash("Order made!")

        return redirect(url_for("payment"))
         
    return render_template("orders.html", form=form)

    
@app.route("/dashboard")
@login_required
def dashboard():
    
    orders = Order.query.all()

    
    return render_template("dashboard.html", orders=orders)

@app.route("/payment", methods=["GET", "POST"])
def payment():
    form = PaymentForm()
    
    if form.validate_on_submit(): 
        payreference = form.payreference.data
        payment = Payment(payreference=payreference)

        db.session.add(payment)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("payment.html", form=form)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for("index"))




