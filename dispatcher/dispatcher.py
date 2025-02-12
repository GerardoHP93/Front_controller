# ViewHelper se encarga de preparar los datos que se pasarán a las vistas.
from helpers.view_helper import ViewHelper

# - abort: Se usa para detener la ejecución y devolver un código de error HTTP.
# - render_template: Se usa para renderizar plantillas HTML con datos dinámicos.
from flask import abort, render_template

# Define la clase Dispatcher, que se encarga de seleccionar la vista adecuada según la solicitud.
class Dispatcher:
    # Método constructor de la clase Dispatcher.
    def __init__(self):
        # Define un diccionario que mapea las opciones de vista a sus respectivas plantillas HTML.
        self.views = {
            'home': 'home.html',  # Vista para la página de inicio
            'about': 'about.html',  # Vista para la página "Sobre Nosotros"
            'contact': 'contact.html'  # Vista para la página de contacto
        }

        # Crea una instancia de la clase ViewHelper y la asigna al atributo 'helper'.
        self.helper = ViewHelper()

    # Método para seleccionar y renderizar la vista adecuada según la opción proporcionada.
    # 'view_option' es la opción de vista solicitada (por ejemplo, 'home', 'about', 'contact').
    def dispatch(self, view_option):
        # Verifica si la opción de vista existe en el diccionario self.views.
        if view_option not in self.views:
            # Si la vista no existe, prepara los datos para la vista de error 404.
            data = self.helper.prepare_data('404')

            # Renderiza la plantilla '404.html' con los datos preparados y devuelve un código de estado 404.
            return render_template('404.html', **data), 404

        # Obtiene la plantilla correspondiente a la opción de vista solicitada.
        template = self.views.get(view_option)

        # Prepara los datos para la vista usando el método prepare_data del ViewHelper.
        data = self.helper.prepare_data(view_option)

        # Renderiza la plantilla con los datos preparados y devuelve la respuesta.
        return render_template(template, **data)