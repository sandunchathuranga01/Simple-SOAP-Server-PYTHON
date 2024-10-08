from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from Component.Student_Controller import StudentService
from Component.DB_config import engine, Base



# Create all database tables (if they don't already exist)
if engine:
    Base.metadata.create_all(bind=engine)

# Create SOAP application
soap_app = Application([StudentService], 'soap_app.ItemService',
                       in_protocol=Soap11(validator='lxml'),
                       out_protocol=Soap11())

# WSGI Application to serve the SOAP service
wsgi_app = WsgiApplication(soap_app)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    try:
        print("Serving SOAP service on http://127.0.0.1:8000")
        server = make_server('127.0.0.1', 8000, wsgi_app)
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server interrupted. Shutting down...")

