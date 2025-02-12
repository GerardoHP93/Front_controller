# Flask es el núcleo de la aplicación web, y render_template se usa para renderizar plantillas HTML.
from flask import Flask, render_template
from controllers.front_controller import FrontController

# Crea una instancia de la clase Flask.
# __name__ es el nombre del módulo actual (en este caso, app.py).
# template_folder='views' especifica que las plantillas HTML se encuentran en la carpeta 'views'.
app = Flask(__name__, template_folder='views')

# Esta instancia se usará para procesar todas las solicitudes entrantes.
front_controller = FrontController()

# Define una ruta para la URL raíz ('/') y Una ruta dinámica ('/<path:path>') que captura cualquier ruta solicitada.
# @app.route es un decorador que asocia una función con una ruta específica.
# path='' es un parámetro opcional que captura la ruta solicitada.
@app.route('/')
@app.route('/<path:path>')
def handle_request(path=''):
    # Llama al método process_request del FrontController, pasando la ruta solicitada.
    # Este método se encarga de procesar la solicitud y devolver la respuesta adecuada.
    return front_controller.process_request(path)

# Define un manejador de errores para el código de estado HTTP 404 (Página no encontrada).
# @app.errorhandler es un decorador que asocia una función con un código de error específico.
@app.errorhandler(404)
def page_not_found(error):
    # Renderiza la plantilla '404.html' y devuelve un código de estado 404.
    return render_template('404.html'), 404

# Verifica si este script se está ejecutando directamente (no importado como módulo).
if __name__ == '__main__':
    # Inicia la aplicación Flask en modo de depuración (debug=True).
    # El modo de depuración permite ver errores detallados en el navegador y reinicia automáticamente el servidor cuando se detectan cambios en el código.
    app.run(debug=True)