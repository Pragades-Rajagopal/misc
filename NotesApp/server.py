from gevent import monkey
from gevent.pywsgi import WSGIServer
from index import app

monkey.patch_all()

httpServer = WSGIServer(('localhost', 8000), app)
httpServer.serve_forever()

