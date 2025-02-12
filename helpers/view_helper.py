# La clase ViewHelper es responsable de preparar los datos que se pasarán a las vistas. Esto permite separar la lógica de preparación de datos de la lógica de renderización de vistas.

class ViewHelper:
    # Método para preparar los datos según la vista solicitada.
    # 'view_name' es el nombre de la vista para la cual se preparan los datos.
    def prepare_data(self, view_name):
        # Crea un diccionario vacío para almacenar los datos.
        data = {}

        # Verifica si la vista solicitada es 'home'.
        if view_name == 'home':
            # Si es 'home', prepara los datos para la página de inicio.
            data = {
                'title': 'Inicio',  # Título de la página
                'content': 'Bienvenido a nuestra página principal'  # Contenido de la página
            }

        # Verifica si la vista solicitada es 'about'.
        elif view_name == 'about':
            # Si es 'about', prepara los datos para la página "Sobre Nosotros".
            data = {
                'title': 'Sobre Nosotros',  # Título de la página
                'content': 'Información sobre nuestra empresa'  # Contenido de la página
            }

        # Verifica si la vista solicitada es 'contact'.
        elif view_name == 'contact':
            # Si es 'contact', prepara los datos para la página de contacto.
            data = {
                'title': 'Contacto',  # Título de la página
                'content': 'Nuestros datos de contacto'  # Contenido de la página
            }

        # Verifica si la vista solicitada es '404'.
        elif view_name == '404':
            # Si es '404', prepara los datos para la página de error 404.
            data = {
                'title': 'Página no encontrada',  # Título de la página
                'content': 'Lo sentimos, la página que estás buscando no existe.'  # Contenido de la página
            }

        # Devuelve el diccionario con los datos preparados.
        return data