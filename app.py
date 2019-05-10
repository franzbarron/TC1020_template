from flask import Flask, render_template, request#, get_json
import logging
import sys

import db

try:
    import simplejson as json
except (ImportError,):
    import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/departamentos", methods=["GET", "POST"])
def departamentos():
    def db_query():
        _db = db.Database()
        if request.method == "GET":
            depts = _db.list_departamento()
            return depts
        else:
            if request.method == "POST":
                nombre = request.form["nombre"]
                oficina = request.form["oficina"]
                telefono = request.form["telefono"]
                if nombre != "" and oficina != "" and telefono != "":
                    _db.insert_departamento(nombre, oficina, telefono)
                # print(type(request.form), file=sys.stdout)

                depts = _db.list_departamento()
                return depts

    res = db_query()
    return render_template("departamentos.html", result=res)


@app.route("/del_departamento", methods=["POST"])
def del_departamento():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            result = json.loads(request.data)
            # print(result, file=sys.stdout)
            for datum in result:
                # print(datum, file=sys.stdout)
                _db.delete_departamento(datum)

        depts = _db.list_departamento()
        return depts

    res = db_query()

    return render_template("departamentos.html", result=res)


@app.route("/cursos", methods=["GET", "POST"])
def cursos():
    def db_query():
        _db = db.Database()
        if request.method == "GET":
            courses = _db.list_curso()
            return courses
        else:
            if request.method == "POST":
                numero = request.form["numero"]
                nombre = request.form["nombre"]
                descripcion = request.form["descripcion"]
                horas_por_semana = request.form["horas-por-semana"]
                semestre = request.form["semestre"]
                departamento = request.form["departamento"]
                if (
                    numero != ""
                    and nombre != ""
                    and descripcion != ""
                    and horas_por_semana != ""
                    and semestre != ""
                    and departamento != ""
                ):
                    _db.insert_curso(
                        numero,
                        nombre,
                        descripcion,
                        horas_por_semana,
                        semestre,
                        departamento,
                    )

                courses = _db.list_curso()
                return courses

    res = db_query()
    return render_template("cursos.html", result=res)


@app.route("/del_curso", methods=["POST"])
def del_curso():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            result = json.loads(request.data)
            # print(result, file=sys.stdout)
            for datum in result:
                # print(datum, file=sys.stdout)
                _db.delete_curso(datum)

        course = _db.list_departamento()
        return course

    res = db_query()
    return render_template("departamentos.html", result=res)


@app.route("/profesores", methods=["GET", "POST"])
def profesores():
    def db_query():
        _db = db.Database()
        if request.method == "GET":
            prof = _db.list_profesor()
            return prof
        else:
            if request.method == "POST":
                nomina = request.form["nomina"]
                nombre = request.form["nombre"]
                if nombre != "" and nomina != "":
                    _db.insert_profesor(nomina, nombre)

            prof = _db.list_profesor()
            return prof

    res = db_query()
    return render_template("profesores.html", result=res)


@app.route("/del_profesor", methods=["POST"])
def del_profesor():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            result = json.loads(request.data)
            # print(result, file=sys.stdout)
            for datum in result:
                # print(datum, file=sys.stdout)
                _db.delete_profesor(datum)

        prof = _db.list_profesor()
        return prof

    res = db_query()
    return render_template("profesores.html", result=res)


@app.route("/grupos", methods=["GET", "POST"])
def grupos():
    def db_query():
        _db = db.Database()
        if request.method == "GET":
            groups = _db.list_grupo()
            horas = _db.list_horario()
            return groups, horas
        else:
            if request.method == "POST":
                numero = request.form["numero"]
                semestre = request.form["semestre"]
                year = request.form["year"]
                curso = request.form["curso"]
                profesor = request.form["profesor"]
                hora = request.form["hora"]
                if (
                    numero != ""
                    and semestre != ""
                    and year != ""
                    and curso != ""
                    and profesor != ""
                    and hora != ""
                ):
                    _db.insert_grupo(numero, semestre, year, curso, profesor, hora)

            groups = _db.list_grupo()
            horas = _db.list_horario()
            return groups, horas

    res, hr = db_query()
    return render_template("grupos.html", result=res, horas=hr)


@app.route("/del_grupo", methods=["POST"])
def del_grupo():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            result = json.loads(request.data)
            # print(result, file=sys.stdout)
            for datum in result:
                print(datum, file=sys.stdout)
                _db.delete_grupo(datum[0], datum[1], datum[2], datum[3])

        group = _db.list_profesor()
        return group

    res = db_query()
    return render_template("grupos.html", result=res)


@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    _db = db.Database()

    def db_query():
        if request.method == "GET":
            student = _db.list_alumno()
            carreras = _db.list_carreras()
            return student, carreras
        else:
            if request.method == "POST":
                matricula = request.form["matricula"]
                curp = request.form["curp"]
                nombre = request.form["nombre"]
                sexo = request.form["sexo"]
                bdate = request.form["bdate"]
                telefono = request.form["telefono"]
                celular = request.form["celular"]
                direccion = (
                    request.form["calle"]
                    + " "
                    + request.form["colonia"]
                    + " "
                    + request.form["cp"]
                    + " "
                    + request.form["municipio"]
                    + ", "
                    + request.form["entidad"]
                )
                departamento = request.form["departamento"]
                carrera = request.form["carrera"]
                if (
                    matricula != ""
                    and curp != ""
                    and nombre != ""
                    and sexo != ""
                    and bdate != ""
                    and direccion != ""
                    and departamento != ""
                    and carrera != ""
                ):
                    _db.insert_alumno(
                        matricula,
                        curp,
                        nombre,
                        sexo,
                        bdate,
                        telefono,
                        celular,
                        direccion,
                        departamento,
                        carrera,
                    )

            student = _db.list_alumno()
            carreras = _db.list_carreras()
            return student, carreras

    res, carr = db_query()
    return render_template("alumnos.html", result=res, carreras=carr)


@app.route("/del_alumno", methods=["POST"])
def del_alumno():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            result = json.loads(request.data)
            # print(result, file=sys.stdout)
            for datum in result:
                # print(datum[0], file=sys.stdout)
                _db.delete_alumno(datum)

        student = _db.list_alumno()
        return student

    res = db_query()
    return render_template("alumnos.html", result=res)


@app.route("/search_alumno", methods=["POST"])
def search_alumno():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            matricula = request.form["matricula"]
            students = _db.find_alumno(matricula)
            # print(students, file=sys.stdout)
            return students

    res = db_query()
    return render_template("alumnos.html", result=res)


@app.route("/search_departamento", methods=["POST"])
def search_departamento():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            nombre = request.form["nombre"]
            dpto = _db.find_departamento(nombre)
            # print(students, file=sys.stdout)
            return dpto

    res = db_query()
    return render_template("departamentos.html", result=res)


@app.route("/search_grupo", methods=["POST"])
def search_grupo():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            curso = request.form["curso"]
            gpo = _db.find_grupo(curso)
            # print(students, file=sys.stdout)
            return gpo

    res = db_query()
    return render_template("grupos.html", result=res)


@app.route("/search_profesor", methods=["POST"])
def search_profesor():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            nomina = request.form["nomina"]
            prof = _db.find_profesor(nomina)
            # print(students, file=sys.stdout)
            return prof

    res = db_query()
    return render_template("profesores.html", result=res)


@app.route("/ecoas", methods=["GET", "POST"])
def ecoas():
    _db = db.Database()

    def db_query():
        if request.method == "GET":
            survey = _db.list_ecoas()
            return survey
        else:
            if request.method == "POST":
                profesor = request.form["profesor"]
                # clave = request.form["clave"]
                curso = request.form["curso"]
                grupo = request.form["grupo"]
                semestre = request.form["semestre"]
                year = request.form["year"]
                calificacion = request.form["calificacion"]
                if (
                    profesor != ""
                    # and clave != ""
                    and curso != ""
                    and grupo != ""
                    and semestre != ""
                    and year != ""
                    and calificacion != ""
                ):
                    _db.insert_ecoas(
                        profesor, curso, grupo, semestre, year, calificacion
                    )

            survey = _db.list_ecoas()
            return survey

    res = db_query()
    return render_template("ecoas.html", result=res)


@app.route("/del_ecoas", methods=["POST"])
def del_ecoas():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            result = json.loads(request.data)
            # print(result, file=sys.stdout)
            for datum in result:
                # print(datum[0], file=sys.stdout)
                _db.delete_ecoas(datum[0], datum[1])

        survey = _db.list_ecoas()
        return survey

    res = db_query()
    return render_template("ecoas.html", result=res)


@app.route("/search_ecoas", methods=["POST"])
def search_ecoas():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            nomina = request.form["nomina"]
            survey = _db.find_ecoas(nomina)
            # print(students, file=sys.stdout)
            return survey

    res = db_query()
    return render_template("ecoas.html", result=res)


@app.route("/cursos_impartidos")
def cursos_impartidos():
    _db = db.Database()

    def db_query():
        impartidos = _db.list_impartidos()
        return impartidos

    res = db_query()
    return render_template("cursos_impartidos.html", result=res)


@app.route("/search_impartidos", methods=["POST"])
def search_impartidos():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            nomina = request.form["nomina"]
            cursos = _db.find_impartidos(nomina)
            # print(students, file=sys.stdout)
            return cursos

    res = db_query()
    return render_template("cursos_impartidos.html", result=res)


@app.route("/grupos_alumno", methods=["GET", "POST"])
def grupos_alumno():
    def db_query():
        _db = db.Database()
        if request.method == "GET":
            lista = _db.list_pertenece()
            return lista
        else:
            if request.method == "POST":
                matricula = request.form["matricula"]
                curso = request.form["curso"]
                grupo = request.form["grupo"]
                semestre = request.form["semestre"]
                year = request.form["year"]
                if (
                    matricula != ""
                    and curso != ""
                    and grupo != ""
                    and semestre != ""
                    and year != ""
                ):
                    _db.insert_pertenece(matricula, curso, grupo, semestre, year)

            lista = _db.list_pertenece()
            return lista

    res = db_query()
    return render_template("grupos_alumno.html", result=res)

@app.route("/del_grupos_alumno", methods=["POST"])
def del_grupos_alumno():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            result = json.loads(request.data)
            # print(result, file=sys.stdout)
            for datum in result:
                # print(datum[0], file=sys.stdout)
                _db.delete_pertenece(datum[0], datum[1], datum[2], datum[3])

        survey = _db.list_ecoas()
        return survey

    res = db_query()
    return render_template("grupos_alumno.html", result=res)

@app.route("/cursos_cursados")
def cursos_cursados():
    _db = db.Database()

    def db_query():
        cursados = _db.list_cursados()
        return cursados

    res = db_query()
    return render_template("cursos_cursados.html", result=res)

@app.route("/search_cursados", methods=["POST"])
def search_cursados():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            matricula = request.form["matricula"]
            cursos = _db.find_cursados(matricula)
            # print(students, file=sys.stdout)
            return cursos

    res = db_query()
    return render_template("cursos_cursados.html", result=res)

@app.route("/libre", methods=["GET", "POST"])
def libre():
    _db = db.Database()

    def db_query():
        if request.method == "GET":
            horas = _db.list_libre()
            return horas
        else:
            if request.method == "POST":
                nomina = request.form["nomina"]
                hora = request.form["hora"]
                if nomina != "" and hora != "":
                    _db.insert_libre(nomina, hora)
                
            horas = _db.list_libre()
            return horas

    res = db_query()
    return render_template("libre.html", result=res)

@app.route("/no_libre", methods=["POST"])
def no_libre():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            nomina = json.loads(request.data)
            nl = _db.list_no_libre(nomina)
            print(nl, file=sys.stdout)

            return nl

    nl = db_query()
    return json.dumps(nl)

@app.route("/search_libre", methods=["POST"])
def search_libre():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            nomina = request.form["nomina-search"]
            horas = _db.find_libre(nomina)
            # print(students, file=sys.stdout)
            return horas

    res = db_query()
    return render_template("libre.html", result=res)

@app.route("/del_libre", methods=["POST"])
def del_libre():
    def db_query():
        if request.method == "POST":
            _db = db.Database()
            result = json.loads(request.data)
            # print(result, file=sys.stdout)
            for datum in result:
                # print(datum[0], file=sys.stdout)
                _db.delete_libre(datum[0], datum[1])

        survey = _db.list_ecoas()
        return survey

    res = db_query()
    return render_template("grupos_alumno.html", result=res)