from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo
from wtforms import StringField, PasswordField, EmailField, SubmitField, TextAreaField, SelectField, IntegerField 

class LoginForm(FlaskForm): 
    username = StringField("username", validators=[DataRequired()], render_kw={"placeholder": "username", "size": "50", "class": "field"}) 
    password = PasswordField("password", validators=[DataRequired()], render_kw={"placeholder": "password", "size": "50", "class": "field"}) 
    submit = SubmitField("submit", render_kw={"class": "submitbtn"})


class SignUpForm(FlaskForm): 
    firstname = StringField("firstname", validators=[DataRequired()], render_kw={"placeholder": "firstname", "size": "50", "class": "field"}) 
    lastname = StringField("lastname", validators=[DataRequired()], render_kw={"placeholder": "lastname", "size": "50", "class": "field"}) 
    username = StringField("username", validators=[DataRequired()], render_kw={"placeholder": "username", "size": "50", "class": "field"}) 
    email = StringField("email", validators=[DataRequired()], render_kw={"placeholder": "email", "size": "50", "class": "field"}) 
    password = PasswordField("password", validators=[DataRequired()], render_kw={"placeholder": "password", "size": "50", "class": "field"}) 
    confirmpassword = PasswordField("confirmpassword", validators=[DataRequired(), EqualTo("password")], render_kw={"placeholder": "confirmpassword", "size": "50", "class": "field"}) 
    submit = SubmitField("submit", render_kw={"class": "submitbtn"} )

# confirmpassword = PasswordField("Confirm Password", validators=[validators.DataRequired(), validators.EqualTo('password')], render_kw={"placeholder": "Confirm Password", "size": "50"}) 


class OrderForm(FlaskForm):
    type = SelectField("Options", render_kw={"class": "field"}, choices=[("Blog Articles"),("Product Descriptions"), ("Website Content"), ("Custom Content") ])
    headline = StringField("headline", validators=[DataRequired()], render_kw={"placeholder": "headline", "size": "50", "class": "field"})
    keywords = StringField("keywords", validators=[DataRequired()], render_kw={"placeholder": "keywords", "size": "50", "class": "field"})
    description = TextAreaField("description", validators=[DataRequired()], render_kw={"placeholder": "description", "size": "50", "class": "field"})
    wordcount = IntegerField("wordcount", validators=[DataRequired()], render_kw={"placeholder": "wordcount", "size": "50", "class": "field"})
    price = StringField("price", default="Price per Word = $ 0.05", render_kw={"readonly": True,  "size": "50", "class": "field"})
    email = StringField("email", validators=[DataRequired()], render_kw={"placeholder": "email", "size": "50", "class": "field"}) 
    submit = SubmitField("order", render_kw={"class": "submitbtn"})
    

class PaymentForm(FlaskForm):
    paybillnumber = StringField("paybillnumber", default="Paybill Number ~ 888777", render_kw={"readonly": True,  "size": "50", "class": "field"})
    accountnumber = StringField("accountnumber", default="Account Number ~ IdeasPlatform", render_kw={"readonly": True, "size": "50", "class": "field"})
    payreference = StringField("payreference", validators=[DataRequired()], render_kw={"placeholder": "payreference", "size": "50", "class": "field"})
    submit = SubmitField("Confirm", render_kw={"class": "submitbtn"})

