# -*- coding: utf-8 -*-
__author__="venkasub"

from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

COLORFIELD_HTML_WIDGET = u"""
<script type="text/javascript">
    var colorField= $('<input type="text" class="form-control" id="#id_%(name)s"/>');
    $('#id_%(name)s')..ColorPickerSliders({ size: 'sm', placement: 'bottom', swatches: false, order: {hsl: 1}});
</script>
"""

class ColorPickerWidget(forms.TextInput):
    """
    A model field widget which implements color picker:
    http://www.virtuosoft.eu/code/bootstrap-colorpickersliders/
    """
    class Media:
        css = {'all': (settings.STATIC_URL + 'colorfield/css/bootstrap.colorpickersliders.css',)}
        js = (settings.STATIC_URL + 'colorfield/js/bootstrap.colorpickersliders.js', settings.STATIC_URL + 'colorfield/js/tinycolor.js' )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(ColorPickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        rendered = super(ColorPickerWidget, self).render(name, value, attrs)
        return rendered + mark_safe(COLORFIELD_HTML_WIDGET % {'name': name})
