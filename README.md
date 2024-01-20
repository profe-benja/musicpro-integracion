# Django Ecommerce

Este es el archivo README para el proyecto Django Ecommerce.

## Requisitos

- Python 3.7 o superior
- Django 3.2.7 o superior

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-nombre-de-usuario/django-ecommerce.git
    ```

2. Crea un entorno virtual:
    ```bash
    python3 -m venv myenv
    ```

3. Activa el entorno virtual:
    ```bash
    source myenv/bin/activate
    ```

4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

    <!-- pip freeze > requirements.txt -->

5. Crea una copia del archivo `.env.example` y renómbralo a `.env`. Actualiza las configuraciones necesarias en el archivo `.env`.

6. Ejecuta las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

7. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## Uso

- Visita `http://localhost:8000` en tu navegador para acceder a la aplicación.

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, sigue las [directrices de contribución](CONTRIBUTING.md) al realizar cambios en el proyecto.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).
