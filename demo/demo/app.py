__author__ = 'venkasub'

'''
from django.db import models
from colorfield.fields import ColorField

class DemoModel(models.Model):
  level               = models.CharField(max_length=50, null=False,blank=False)
  color_code          = ColorField(null=True,blank=True)
  def __unicode__(self):
    return "%s - %s" % (self.level, self.color_code)
'''
from django import forms

class DemoForm(forms.Form):
  level               = forms.CharField(max_length=50)
  color_code          = ColorField()



from django.views.generic.edit import FormView

class DemoView(FormView):
  form_class = DemoForm

