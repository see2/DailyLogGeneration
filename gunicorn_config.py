import os

bind = "0.0.0.0:" + os.environ.get("PORT", "8080")
workers = 1
threads = 1
timeout = 30
certfile = "certs/cert.pem"
keyfile = "certs/key.pem"
