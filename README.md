# Template repo for forking into private django-projects

## Command for executing the django web app:
```python

python .\manage.py runserver 127.0.0.1:8082
```

## Python Queryset API Reference:
https://docs.djangoproject.com/en/4.2/ref/models/querysets/

```python 

# Example of how to use the Queryset API
# Get all the objects in the database
all_objects = Model.objects.all()

# Get all the objects in the database that match a certain condition
filtered_objects = Model.objects.filter(field_name=field_value)

# Get the first object in the database that matches a certain condition
first_object = Model.objects.filter(field_name=field_value).first()

# Get the last object in the database that matches a certain condition
last_object = Model.objects.filter(field_name=field_value).last()

# Get the number of objects in the database that match a certain condition
number_of_objects = Model.objects.filter(field_name=field_value).count()

# Get the number of objects in the database
number_of_objects = Model.objects.all().count()

## Internal notes on queryset API
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
import django
django.setup()
from portfolio_app.models import Project
queryset = Project.objects.all()
print(queryset)
```