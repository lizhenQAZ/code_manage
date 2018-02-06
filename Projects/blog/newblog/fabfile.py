from fabric.api import run, env
from fabric.operations import sudo

# GIT_REPO = "you git repository"
env.user = 'root'
env.password = 'lz211314'
# ssh的主机对应的域名
env.hosts = ['120.55.63.85']
env.port = '22'


def deploy():
    source_folder = '/usr/local/etc/blog/newblog/'
    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        workon django-blog-3.5.2 &&
        pip install -r {}/requirements.txt &&
        python3 manage.py collectstatic --noinput &&
        python3 manage.py migrate
        """.format(source_folder, source_folder))
    sudo('gunicorn newblog.wsgi:application --bind 0.0.0.0:8080')
    sudo('nginx -c /etc/nginx/nginx_blog.conf')
