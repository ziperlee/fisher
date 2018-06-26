"""
 Create by zipee on 2018/6/11.
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired

__author__ = 'zipee'

class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)]) # message = 自定义错误提示
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)