# template BD universidad

## Requerimientos

Instalar las siguientes herramientas:
- MySQL
- Python
- pip

Ya que tengan pip, correr el siguiente comando en la terminal
```
pip install -r requirements.txt
```

## Para crear la base de datos

Inicializar mysql en la terminal

Correr:
```sql
CREATE DATABASE TEC;
USE TEC;
SOURCE create.sql;
```

## Para correr la aplicación

Ya que tienen todo instalado, en terminal, ir al folder del proyecto, ahi correr el siguiente comando dependiendo de su sistema operativo.

para Linux o macOS:
```
export FLASK_APP=app.py
```

para Windows:
```
set FLASK_APP=app.py
```

y después:
```
python -m flask run
```

en su browser, ir a `localhost:5000` y navegar por los queries desde ahi.

## ¿Cómo esta organizada la aplicación?
```
universidad/
  static/
    styles.css
  templates/
    members.html
  app.py
  db.py
  README.md
  requirements.txt
```

- En `app.py` se encuentran las rutas de la aplicación.
- `db.py` contiene la conexión a la base de datos y algunos queries de ejemplo.
- `README.md` es este documento.
- `requirements.txt` contiene las librerias necesarias para que este proyecto funcione.
- En el folder `templates/`, estan los `html` para ver los resultados de los queries.
- En el folder `static/` se encuentra el css para el html.

Ustedes tendrán que modificar `db.py`, `app.py` y agregar mas templates en el folder de `templates/`

## Queries

### Queries básicos
- [x] Lista de alumnos
- [x] Lista de departamentos
- [x] Lista de cursos
- [x] Lista de todos los grupos
- [x] Lista de profesores

### Queries con inputs
- [x] Lista de alumnos dada una matrícula ordenados por matrícula
- [x] Lista de departamentos dado el nombre del departamento ordenado por clave/número de departamento
- [x] Lista de grupos dado el nombre del curso ordenado por id del curso y número de grupo
- [x] Lista de profesores dada la nómina ordenado por nómina

### Queries mas complejos, dado un input:
- [ ] Cursos por alumno (dada la matrícula de un alumno)
- [ ] Nómina, nombre del profesor y los cursos que ha impartido o imparte un profesor dada la nómina del profesor.
- [ ] Nómina y nombre del profesor con los horarios libres dado la nómina de un profesor.
- [ ] Mostrar resultado de ECOAS con su número de curso, nombre, número de grupo, semestre y año dada la nómina de un profesor. Ordenado por año, semestre, número de curso y grupo.

### INSERTS
- [x] Insertar un alumno
- [x] Insertar un departamento
- [x] Insertar un profesor

### DELETE
- [x] Eliminar a un alumno
- [x] Eliminar un departamento
- [x] Eliminar un profesor
