"""
Compares the rendering speed between Django forms and django-floppyforms

Usage: DJANGO_SETTINGS_MODULE=benchmark python benchmark.py [--cache]
"""
import sys
import timeit

django = """from django import forms

class DjangoForm(forms.Form):
    text = forms.CharField()
    slug = forms.SlugField()
    some_bool = forms.BooleanField()
    email = forms.EmailField()
    date = forms.DateTimeField()
    file_ = forms.FileField()

rendered = DjangoForm().as_p()"""

flop = """import floppyforms as forms

class FloppyForm(forms.Form):
    text = forms.CharField()
    slug = forms.SlugField()
    some_bool = forms.BooleanField()
    email = forms.EmailField()
    date = forms.DateTimeField()
    file_ = forms.FileField()

rendered = FloppyForm().as_p()"""

def time(stmt):
    t = timeit.Timer(stmt=stmt)
    return t.timeit(number=1000)

if __name__ == '__main__':
    print "Plain Django:", time(django)
    print "django-floppyforms:", time(flop)

INSTALLED_APPS = (
    'floppyforms'
)

if '--cache' in sys.argv:
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )
