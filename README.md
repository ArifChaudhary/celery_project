# celery_project
django-celery-email-send
send email using django celery

Installation
You can install Celery either via the Python Package Index (PyPI) or from source.

To install using pip:

pip install celery==5.0.5

Celery Periodic Tack
The periodic task schedules uses the UTC time zone by default, but you can change the time zone used using the timezone setting.

An example time zone could be Asia/Kathmandu:

timezone = 'Asia/Kolkata'

If you want more control over when the task is executed, for example, a particular time of day or day of the week, you can use the crontab schedule type


http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html

and finally you can run celery task by using command

celery -A project_name worker -l info -B
