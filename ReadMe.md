## Using Elasticsearch with Django App

### Usage

* Clone the project and setup your virtualenv
```
git clone https://github.com/bilalebi/django_elasticsearch_demo.git
cd django_elasticsearch_demo
python3 -m venv venv
source venv/bin/activate
```

* Install requirements
```
pip install -r requirments.txt
```

* [Download](https://www.elastic.co/downloads/elasticsearch) and run Elasticsearch
```
cd <elasticsearch-dir>
bin/elasticsearch
```

* Generate the migration files and migrate
```
python manage.py makemigrations
python manage.py migrate
```

* Run the server
```
python manage.py runserver
```

Head to admin panel where you can CRUD articles: http://127.0.0.1:8000/admin/

Once you add an article to SQL DB it will be also (automatically) added to ES with the same ID

You can see the ES document using this URL (GET request): http://localhost:9200/articles/_doc/1 (`1` is the document ID)

### Step-by-step tutorial (setup from scratch):

* Install `Django 3.2`
```
pip install django==3.2
```

* Generate the initial project files
```
django-admin startproject django_elasrticsearch_demo
```

* Install `django-elasticsearch-dsl` package and add it to `INSTALLED_APPS`
```
pip install django-elasticsearch-dsl
```

* define `ELASTICSEARCH_DSL` in django settings
```
ELASTICSEARCH_DSL={
    'default': {
        'hosts': 'localhost:9200'
    },
}
```

* Generate `requirements.txt` file
```
pip freeze > requirements.txt
```

* [Download](https://www.elastic.co/downloads/elasticsearch) and run Elasticsearch
```
cd <elasticsearch-dir>
bin/elasticsearch
```
Make sure it's working by going to http://localhost:9200

* Run the server
```
python manage.py runserver
```

* Create `articles` app and add it to `INSTALLED_APPS`
```
python manage.py startapp articles
```

* Create the `model.py`
* Create `documemt.py`
* Generate the migration files and migrate
```
python manage.py makemigrations
python manage.py migrate
```

* Create superuser
```
python manage.py createsuperuser
```

* Register your model in `admin.py` for it to appear in the admin page
```
admin.site.register(Article)
```

Head to admin panel where you can CRUD articles: http://127.0.0.1:8000/admin/

Once you add an article to SQL DB it will be also (automatically) added to ES with the same ID

You can see the ES document using this URL (GET request): http://localhost:9200/articles/_doc/1 (`1` is the document ID)

---

If Index is deleted

```
curl -X DELETE "localhost:9200/articles?pretty"
```

The data can be restored using the command

```
python manage.py search_index --rebuild
```