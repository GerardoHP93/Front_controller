# 'request' se usa para acceder a los datos de la solicitud HTTP, como parámetros de consulta, formularios, etc.
from flask import request

# Dispatcher se encarga de seleccionar la vista adecuada según la solicitud.
from dispatcher.dispatcher import Dispatcher

# ViewHelper se encarga de preparar los datos que se pasarán a las vistas.
from helpers.view_helper import ViewHelper

# Esta clase centraliza el manejo de todas las solicitudes entrantes.
class FrontController:
    
    def __init__(self):
        # Crea una instancia de la clase Dispatcher y la asigna al atributo 'dispatcher'.
        self.dispatcher = Dispatcher()

        # Crea una instancia de la clase ViewHelper y la asigna al atributo 'helper'.
        self.helper = ViewHelper()

    # Método para procesar una solicitud entrante,'path' es la ruta solicitada por el usuario.
    def process_request(self, path):
        # Simulación de autenticación: verifica si el usuario está autenticado.
        if not self._authenticate():
            # Si la autenticación falla, devuelve un mensaje de error y un código de estado 401 (No autorizado).
            return "No autorizado", 401

        # Simulación de autorización: verifica si el usuario tiene permisos para acceder al recurso.  
        if not self._authorize():
            # Si la autorización falla, devuelve un mensaje de error y un código de estado 403 (Acceso denegado).
            return "Acceso denegado", 403

        # Extrae el parámetro 'opcion' de la solicitud (si está presente) o usa la ruta como valor predeterminado.
        # Si no se proporciona 'opcion' y la ruta está vacía, se usa 'home' como valor predeterminado.
        view_option = request.args.get('opcion', path if path else 'home')

        # Delega la selección de la vista al Dispatcher, pasando 'view_option' como argumento.
        return self.dispatcher.dispatch(view_option)

    # Método privado para simular la autenticación del usuario.
    # En este caso, siempre retorna True (simulación).
    def _authenticate(self):
        return True

    # Método privado para simular la autorización del usuario.
    # En este caso, siempre retorna True (simulación).
    def _authorize(self):
        return True