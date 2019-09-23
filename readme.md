- python manage.py `startapp` articles
- create `urls.py`
- create basic view
- create model
- `python manage.py migrate`
- create superuser `python manage.py createsuperuser`
- `python manage.py runserver`
- register model in `admin.py` - `admin.site.register(Article)`

- create more views: create templates dir with app name dir
- add namespace to `urls.py`: `app_name = 'articles'`

- for forms: create `forms.py`
```
from django import forms

from .models import Article

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
```
- add success urls:
```
    def get_success_url(self):
        return reverse('articles:detail', kwargs={'pk': self.object.pk})
```

- create articles/static/articles/style.css
- add `{% load static %}` to templates
- <link rel="stylesheet" type="text/css" href="{% static 'articles/style.css' %}">

- to use root templates dir, add `'DIRS': [os.path.join(BASE_DIR, 'templates')],` to TEMPLATES in settings.py