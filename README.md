# DJANGO BLOG

La página principal da un mensaje de bienvenida. En la esquina superior izquierda encontrarás enlaces a:

1. Artículos
2. Notas
3. Música

En la esquina superior derecha, opciones para login, logout, y registro de nuevo usuario en caso de no tenerlo.
Al iniciar sesión con tu usuario, en la esquina superior derecha aparecerá un enlace al Panel de Control, donde podrás revisar los artículos, notas o la música que has subido. Podrás modificar o borrar cada elemento por separado. Bajo el nombre de usuario, encontrarás un botón para modificar los datos de tu cuenta.

En la sección de artículos hay un cajón de comentarios funcional. Cada artículo tiene un botón de "leer más" que te llevará al artículo en sí, dentro del cual se verán los comentarios publicados.

# CLONAR REPOSITORIO

1. $ git clone https://github.com/neguma/Blog-Django
2. $ cd blog-django

# CREAR ENTORNO VIRTUAL

1. $ pipenv install
2. $ pipenv shell

# INSTALAR REQUISITOS

   $ pip install -r requirements.txt

# MIGRAR DB

1. $ py manage.py makemigrations
2. $ py manage.py migrate

# CREAR SUPERUSER

1. $ py manage.py createsuperuser
2. Completar con los datos requeridos

# INICIAR SERVIDOR

   $ py manage.py runserver
   
El servidor debería iniciarse en la dirección http://127.0.0.1:8000/
Para acceder al panel de admin, http://127.0.0.1:8000/admin

