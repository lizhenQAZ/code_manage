sudo nginx -c /etc/nginx/nginx_blog.conf
gunicorn newblog.wsgi:application --bind 0.0.0.0:8080
