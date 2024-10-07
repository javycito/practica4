Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import redis
... import time
... 
... username = "default" 
... password = "YcUSaTxRbeeaSs9xUNTSfN4UsdCt9E7I" 
... public_endpoint = "redis-11723.c56.east-us.azure.redns.redis-cloud.com:11723"
... ... redis_url = f"redis://{username}:{password}@{public_endpoint}"
... 
... client = redis.Redis.from_url(redis_url)
... 
... canal = "mi_canal"
... client.publish(canal, "¡Hola, mundo!")
