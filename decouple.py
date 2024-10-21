from decouple import config

users_port = config('USERS_SERVICE_PORT', default=5000)
orders_port = config('ORDERS_SERVICE_PORT', default=5001)
