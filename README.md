# Proyecto 7 Pruebas para comprobar la funcionalidad de Urban Routes

### Descripción del proyecto
* Consta de una serie de test que utilizan Selenium para automatizar y validar las funcionalidades de la interfaz de usuario en la aplicación de Urban Routes

### Pruebas 
- Necesitas tener instalado Python URL oficial *https://www.python.org/downloads/*
- Necesitas instalar Selenium utiliza el comando pip install selenium
- Necesitas tener instalados los paquetes pytest (pip install pytest)
- Agregar al path y asi quedan como variable de entorno en el SO.
- Ejecuta todas las pruebas con el comando pytest.
- Ejemplo al ejecutar solo una prueba especifica: python3.12 -m pytest TestUrbanRoutes.py::TestUrbanRoutes::test_set_route

### Observaciones
* Si instalaste Python desde la Microsoft Store la ejecución de pruebas desde terminal seria:
    * python3.12 -m pytest .\TestUrbanRoutes.py
* Todas las pruebas se encuentran en archivo TestUrbanRoutes.py
* En archivo data.py se encuentra la variable {urban_routes_url} cuyo valor debe ser reemplazado por la nueva URL que generes
* En archivo selector.py se encuentran los selectores utilizados en la clase UrbanRoutesPage ubicada en archivo UrbanRoutesPage.py
* El archivo utility.py contiene función que retorna el código de confirmación de teléfono y lo devuelve como un string.