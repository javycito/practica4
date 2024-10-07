Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import redis
... 
... username = "default"  
... password = "YcUSaTxRbeeaSs9xUNTSfN4UsdCt9E7I" 
... public_endpoint = "redis-11723.c56.east-us.azure.redns.redis-cloud.com:11723"  
... redis_url = f"redis://{username}:{password}@{public_endpoint}"
... client = redis.Redis.from_url(redis_url)
... 
... pubsub = client.pubsub()
... 
... canal = "mi_canal" 
... pubsub.subscribe(canal)
... 
... print("Esperando mensajes en el canal:", canal)
... 
... try:
...     for message in pubsub.listen():  
...         if message['type'] == 'message': 
...             print("Mensaje recibido:", message['data'].decode()) 
... except KeyboardInterrupt:
