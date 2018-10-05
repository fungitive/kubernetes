DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'demo',
        'USER': 'root',
        'PASSWORD': 'devpwd',
        'HOST': 'postgresql.default.svc.cluster.local',
        'PORT': '',
    }
}

REDIS_HOST = "redis.default.svc.cluster.local"
# 对于不解析dns的应用配置，可以在配置文件中手动解析,如
# import socket 
# REDIS_HOST = socket.gethostbyname("redis.default.svc.cluster.local")
