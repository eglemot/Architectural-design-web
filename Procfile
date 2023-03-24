release: python archi_designs/manage.py migrate && python archi_designs/manage.py collectstatic --noinput
web: gunicorn --pythonpath archi_designs archi_designs.wsgi
