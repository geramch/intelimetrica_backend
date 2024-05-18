# Test backend

## Introducción
- **db**: Contiene los archivos de base de datos, incluyendo `db.py` y `utils.py`.
- **routers**: Contiene los archivos de enrutamiento, incluyendo `__init__.py`, `endpoints.py`, `__init__.py` y `routers.py`.
- **services**: Contiene los archivos de servicio, incluyendo `restaurant_service.py`.
- **utils**: Contiene los archivos de utilidades, incluyendo `schemas.py`.
- **docker-compose.yml**: Define la configuración de Docker Compose para el proyecto.
- **Dockerfile**: Define la imagen de Docker para el proyecto.
- **init.sql**: Contiene el script SQL para inicializar la base de datos.
- **main.py**: Es el punto de entrada principal del proyecto.
- **README.md**: Este archivo readme.
- **requirements.txt**: Contiene los requisitos de dependencia del proyecto.

## Instalación
Para instalar el proyecto, siga estos pasos:

1. Clone el repositorio del proyecto
2. Ejecute el comando 
`docker compose up --build`

## Uso
La aplicación se puede acceder en la siguiente URL:

- http://localhost:9000

La aplicación proporciona las siguientes endpoints:


- `POST /restaurants`: Crea un nuevo restaurante.
- `GET /restaurants`: Obtiene una lista de restaurantes.
- `GET /restaurants/single/{restaurant_id}`: Obtiene un restaurante específico por su ID.
- `PUT /restaurants/{restaurant_id}`: Actualiza un restaurante específico por su ID.
- `DELETE /restaurants/{restaurant_id}`: Elimina un restaurante específico por su ID.
- `POST /restaurants/upload_csv/`: Sube un archivo CSV para agregar restaurantes.
- `GET /restaurants/statistics`: Obtiene estadísticas de restaurantes dentro de un radio específico.

## Documentación
Para obtener más información sobre el proyecto, consulte la siguiente documentación:

- Docker Compose
- Dockerfile
- SQL

El proyecto cuenta con su propia documentación en los enlaces
- `http://localhost:9000/docs`
- `http://localhost:9000/redoc`


## Licencia
El proyecto Intellimetrica está licenciado bajo la licencia MIT. Para obtener más información, consulte el archivo LICENSE en el repositorio del proyecto.

