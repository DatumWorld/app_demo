echo kill celery beat  scheduler %date% %time% >>celery_scheduler_log.txt
for /f  %%b in (D:\path\to\app_demo\celerybeat.pid) do (
set celerybeatpid=%%~b
)
taskkill /f /t /pid %celerybeatpid%

tasklist|find /c /i "celery.exe"
if ERRORLEVEL 0 (taskkill /f /t /im celery.exe)

tasklist|find /c /i "flower.exe"
if ERRORLEVEL 0 (taskkill /f /t /im flower.exe)


for /f  %%a in (D:\path\to\app_demo\celeryev.pid) do (
set celerycampid=%%~a
)
taskkill /f /t /pid %celerycampid%
start cmd /c "del D:\path\to\app_demo\celeryev.pid"
start cmd /c "del D:\path\to\app_demo\celerybeat.pid"

echo kill celery beat  scheduler %date% %time% >>celery_scheduler_log.txt