from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import (
    SelectField,
    SelectMultipleField,
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
)
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    EqualTo,
    URL,
    Optional,
    IPAddress,
)


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class ImageProperties(FlaskForm):
    prompt = StringField("Image prompt", validators=[DataRequired()])
    size = SelectField(
        "size", choices=[("256x256", "256x256"), ("512x512", "512x512"), ("1024x1024", "1024x1024")]
    )
    number = StringField("Number of images", validators=[DataRequired()], default="1")
    submit = SubmitField("Generate")
