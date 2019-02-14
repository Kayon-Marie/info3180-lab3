from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
from wtforms import validators, ValidationError

class ContactForm(Form):
    name = TextField("Name", [validators.Required("Please enter your full name.")])
    email = TextField("E-mail", [validators.Required("Please enter your e-mail address"),
    validators.Email("Please enter your e-mail address.")])
    subject = TextField("Subject", [validators.Required("Please enter the subject for your message")])
    message = TextAreaField("Message", [validators.Required("Please enter the message to be sent")])
    submit = SubmitField("Send")
