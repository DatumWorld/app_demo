@echo off
echo start celery beat scheduler %date% %time% >>celery_scheduler_log.txt
start cmd /c "del D:\path\to\app_demo\celeryev.pid"
start cmd /c "del D:\path\to\app_demo\celerybeat.pid"

start cmd /c "cd/d D:\path\to\app_demo\venv\Scripts&&activate&&cd../../&&flower -A report"

start cmd /c "cd/d D:\path\to\app_demo\venv\Scripts&&activate&&cd../../&&python manage.py celerycam"

start cmd /c "cd/d D:\path\to\app_demo\venv\Scripts&&activate&&cd../../&&celery -A report worker -P prefork -E  -l info -c 2 -n name@%%n"

start cmd /c "cd/d D:\path\to\app_demo\venv\Scripts&&activate&&cd../../&&celery -A report beat -l info --max-interval 60 -S djcelery.schedulers.DatabaseScheduler"

echo start celery beat scheduler %date% %time% >>celery_scheduler_log.txt

