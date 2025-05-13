# Airlines
Run Code" (Development vs. Production):

Development:
python manage.py runserver
This command starts Django's lightweight built-in development server. It's great for development because it automatically reloads when you change code.
NOT suitable for production.
Production:
Code Preparation:
Collect static files: python manage.py collectstatic
Ensure all dependencies are in requirements.txt.
Application Server (WSGI/ASGI):
Use a production-grade WSGI server like Gunicorn or uWSGI (or ASGI servers like Daphne or Uvicorn if using Django Channels for WebSockets).
Example with Gunicorn: gunicorn airline_project.wsgi:application --bind 0.0.0.0:8000
Reverse Proxy:
Nginx (or Apache) is set up in front of Gunicorn/uWSGI.
Nginx handles direct client connections, serves static files efficiently, can handle SSL termination (HTTPS), and forwards dynamic requests to the Gunicorn/uWSGI process.
It also helps with load balancing if you have multiple application server instances.
Database:
A robust, production-ready database server (PostgreSQL, MySQL) is used.
Process Management:
Tools like systemd or Supervisor are used to manage the Gunicorn/uWSGI processes, ensuring they restart if they crash and run on server boot.
Deployment Strategy:
Manual (SFTP/SSH - not recommended for large apps).
Automated with CI/CD pipelines.
Using platform-as-a-service (PaaS) like Heroku, Google App Engine.
Using container orchestration (Docker + Kubernetes).
Environment Variables:
Sensitive information (database passwords, API keys, SECRET_KEY) is managed through environment variables, not hardcoded.
