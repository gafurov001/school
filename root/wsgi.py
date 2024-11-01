import os
import django


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

application = get_wsgi_application()

django.setup()
