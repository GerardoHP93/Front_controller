# Front Controller Pattern Implementation in Python Flask

## Autor
Gerardo Isidro Herrera Pacheco  
ISC 68612 - 8vo Semestre  
Maestro: Jose C Aguilar Canepa  
Universidad Autónoma de Campeche, Facultad de Ingeniería

## Descripción del Proyecto
Este proyecto implementa el patrón de diseño Front Controller utilizando Python Flask, este patrón se encarga de centralizar el manejo de todas las solicitudes entrantes a la aplicación, asegurando que las peticiones sean procesadas de manera estructurada y organizada.La aplicación permite la navegación entre diferentes vistas, tales como Inicio, Sobre Nosotros y Contacto, mediante sistema que gestiona las solicitudes web a través de un controlador centralizado que maneja la autenticación, autorización y el despacho de vistas.

## Estructura del Proyecto
El proyecto está organizado en los siguientes componentes principales:

### 1. Front Controller (`front_controller.py`)
- Actúa como punto de entrada centralizado para todas las solicitudes
- Maneja la autenticación y autorización
- Delega el procesamiento de vistas al Dispatcher
- Gestiona los parámetros de la solicitud

### 2. Dispatcher (`dispatcher.py`)
- Selecciona la vista apropiada basada en la solicitud
- Mantiene un mapeo de opciones de vista a plantillas HTML
- Colabora con ViewHelper para preparar datos
- Maneja errores 404 para rutas no encontradas

### 3. View Helper (`view_helper.py`)
- Prepara los datos para cada vista
- Mantiene la lógica de presentación separada
- Proporciona datos específicos para cada tipo de página
- Gestiona el contenido dinámico de las vistas

### 4. Vistas (`views/`)
- Plantillas HTML para cada página (home, about, contact, 404)
- Integración con estilos CSS
- Sistema de navegación consistente
- Contenido dinámico a través de variables Jinja2

### 5. Carpeta static/
- Incluye styles.css, que define los estilos de las páginas HTML.

## Flujo de Trabajo
- 1. El usuario accede a una URL → Flask recibe la solicitud y la redirige a FrontController.process_request().
- 2. FrontController verifica la autenticación y autorización → Si son válidas, delega la petición al Dispatcher.
- 3. Dispatcher selecciona la vista correspondiente según la opción proporcionada en la URL y usa el ViewHelper para obtener los datos necesarios.
- 4. Se renderiza la plantilla HTML con los datos proporcionados y se envía la respuesta al usuario.

## Diagrama de Clases UML

En este diagrama he representado:

-Clase Flask
Atributos:
- __name__: str (nombre del módulo)
- template_folder: str (directorio de plantillas)
  
Métodos:
- route(rule: str): decorador para rutas
- errorhandler(code: int): manejador de errores
- run(debug: bool): iniciar servidor

Clase FrontController
Atributos:
- dispatcher: Dispatcher (instancia del despachador)
- helper: ViewHelper (instancia del helper)

Métodos:
- __init__(): constructor
- process_request(path: str): procesa solicitudes
- _authenticate(): verifica autenticación
- _authorize(): verifica autorización

Clase Dispatcher
Atributos:
- views: dict (mapeo de vistas)
- helper: ViewHelper (instancia del helper)

Métodos:
- __init__(): constructor
- dispatch(view_option: str): despacha vistas

Clase ViewHelper
Métodos:
- prepare_data(view_name: str): prepara datos para vistas

Interface Templates
Representa las plantillas HTML disponibles:
- home.html
- about.html
- contact.html
- 404.html

Relaciones:
- FrontController usa Dispatcher y ViewHelper
- Dispatcher usa ViewHelper y Templates
- Flask direcciona las solicitudes a FrontController

```mermaid
classDiagram
    class Flask {
        +__name__: str
        +template_folder: str
        +route(rule: str)
        +errorhandler(code: int)
        +run(debug: bool)
    }

    class FrontController {
        -dispatcher: Dispatcher
        -helper: ViewHelper
        +__init__()
        +process_request(path: str): Response
        -_authenticate(): bool
        -_authorize(): bool
    }

    class Dispatcher {
        -views: dict
        -helper: ViewHelper
        +__init__()
        +dispatch(view_option: str): Response
    }

    class ViewHelper {
        +prepare_data(view_name: str): dict
    }

    class Templates {
        <<interface>>
        home.html
        about.html
        contact.html
        404.html
    }

    FrontController --> Dispatcher : uses
    FrontController --> ViewHelper : uses
    Dispatcher --> ViewHelper : uses
    Dispatcher --> Templates : renders
    Flask --> FrontController : routes requests to
