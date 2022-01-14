from django.forms import Form
from django.forms import widgets
from django.forms import fields

index_label = (('1', 'Problem 1'), ('2', 'Problem 2'), ('3', 'Problem 3'))

# 表单类用以生成表单
class AddForm(Form):
    headimg = fields.FileField()
    label = fields.CharField(max_length=10, widget=widgets.Select(choices=index_label))
    diag = fields.CharField(label='diag', max_length=100)
