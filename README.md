# Newspaper Lecheria

Un sistema de gestión de artículos para un periódico digital desarrollado con Django.

## Características

- **Gestión de Artículos**: Crear, leer, actualizar y eliminar artículos.
- **Sistema de Autenticación**: Inicio de sesión requerido para crear/editar artículos.
- **Interfaz Moderna**: Diseño responsive y profesional con CSS personalizado.
- **Búsqueda**: Buscar artículos por título o contenido.
- **Paginación**: Navegación eficiente en listas largas (10 artículos por página).
- **Permisos**: Solo los autores pueden editar o eliminar sus propios artículos.
- **Mensajes**: Sistema de notificaciones para acciones del usuario.

## Tecnologías Utilizadas

- **Backend**: Django 6.0
- **Base de Datos**: SQLite
- **Frontend**: HTML5, CSS3
- **Autenticación**: Django Auth

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone <url-del-repositorio>
   cd CRUD_ABR2026
   ```

2. **Crea un entorno virtual**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Realiza las migraciones**:
   ```bash
   python manage.py migrate
   ```

5. **Crea un superusuario** (opcional, para acceder al admin):
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecuta el servidor**:
   ```bash
   python manage.py runserver
   ```

7. **Accede a la aplicación**:
   - Página principal: http://127.0.0.1:8000/
   - Panel de administración: http://127.0.0.1:8000/admin/

## Uso

### Para Autores
1. Regístrate o inicia sesión.
2. Crea nuevos artículos desde "Crear Artículo".
3. Edita o elimina tus propios artículos.

### Para Lectores
1. Navega por la lista de artículos.
2. Usa la búsqueda para encontrar contenido específico.
3. Lee artículos completos.

## Estructura del Proyecto

```
CRUD_ABR2026/
├── base_project/          # Configuración principal de Django
├── newspaper/             # Aplicación principal
│   ├── models.py          # Modelo Article
│   ├── views.py           # Vistas CRUD
│   ├── urls.py            # URLs de la aplicación
│   └── templates/         # Plantillas HTML
├── static/                # Archivos estáticos (CSS, JS, imágenes)
├── templates/             # Plantillas base
├── db.sqlite3             # Base de datos
├── manage.py              # Script de gestión de Django
└── requirements.txt       # Dependencias
```

## Modelos

### Article
- `title`: Título del artículo (CharField, max 200 caracteres)
- `content`: Contenido del artículo (TextField)
- `author`: Autor (ForeignKey a User)
- `created_at`: Fecha de creación (DateTimeField, auto_now_add)
- `published_date`: Fecha de publicación (DateTimeField, auto_now_add)

## Vistas

- `ArticleListView`: Lista paginada de artículos con búsqueda
- `ArticleDetailView`: Vista detallada de un artículo
- `ArticleCreateView`: Formulario para crear artículos
- `ArticleUpdateView`: Formulario para editar artículos
- `ArticleDeleteView`: Confirmación para eliminar artículos

## URLs

- `/`: Lista de artículos
- `/articulos/<id>/`: Detalle de artículo
- `/articulos/crear/`: Crear artículo
- `/articulos/<id>/actualizar/`: Actualizar artículo
- `/articulos/<id>/eliminar/`: Eliminar artículo
- `/accounts/login/`: Inicio de sesión
- `/accounts/logout/`: Cierre de sesión

## Estilos

Los estilos se encuentran en `static/css/style.css` e incluyen:
- Diseño responsive
- Paleta de colores profesional
- Tipografía clara
- Componentes reutilizables

## Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

Para preguntas o sugerencias, por favor contacta al equipo de desarrollo.