import pymysql
import sys


class Database:
    def __init__(self):
        host = "127.0.0.1"
        # host = "localhost"
        user = "root"
        password = "root"
        db = "Tec"
        # port = 8889

        self.con = pymysql.connect(host, user, password, db)
        self.cur = self.con.cursor()

    def list_departamento(self):
        query = "SELECT * FROM Departamento"
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def insert_departamento(self, nombre, oficina, telefono):
        try:
            query = """
                 INSERT INTO Departamento (nombre, oficina, telefono)
                 VALUES ('{}', '{}', '{}')
                 """.format(
                nombre, oficina, telefono
            )
            print("Query: {}".format(query), file=sys.stdout)
            self.cur.execute(query)
            self.con.commit()
        except Exception as e:
            print("Exception occured: ", e)

    def delete_departamento(self, numero):
        query = """DELETE FROM Departamento
                    WHERE numero = {}
                """.format(
            numero
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def list_curso(self):
        query = """
                SELECT  c.numero, c.nombre, c.descripcion, c.horasPorSemana, c.semestre, d.nombre
                FROM    Curso c, Departamento d
                WHERE   c.departamento = d.numero
                """
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def delete_curso(self, numero):
        query = """DELETE FROM Curso
                    WHERE numero='{}'
                """.format(
            numero
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def insert_curso(self, numero, nombre, descripcion, horas, semestre, dpto):
        try:
            query = """
            INSERT INTO Curso
            VALUES('{}', '{}', '{}', '{}', '{}', (SELECT numero FROM Departamento WHERE nombre='{}'))""".format(
                numero, nombre, descripcion, horas, semestre, dpto
            )
            print("Query: {}".format(query), file=sys.stdout)
            self.cur.execute(query)
            self.con.commit()
        except Exception as e:
            print("Exception occured: ", e)

    def list_profesor(self):
        query = "SELECT * FROM Profesor"
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def insert_profesor(self, nomina, nombre):
        try:
            query = """
            INSERT INTO Profesor
            VALUES('{}','{}')""".format(
                nomina, nombre
            )
            print("Query: {}".format(query), file=sys.stdout)
            self.cur.execute(query)
            self.con.commit()
        except Exception as e:
            print("Exception occured: ", e)

    def delete_profesor(self, nomina):
        query = """DELETE FROM Profesor
                    WHERE pID='{}'
                """.format(
            nomina
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def list_grupo(self):
        query = """
                SELECT  g.numero, g.curso, g.semestre, g.anio, c.nombre, p.nombre
                FROM    Grupo g, Curso c, Profesor p
                WHERE   g.curso=c.numero
                AND     g.profesor=p.pID
                ORDER BY    g.curso, g.numero
                """
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def insert_grupo(self, numero, semestre, anio, curso, profesor, hora):
        try:
            query = """
                    INSERT INTO Grupo
                    VALUES(
                        {},
                        '{}',
                        {},
                        (SELECT numero FROM Curso WHERE numero='{}'),
                        (SELECT pID FROM Profesor WHERE pID='{}'),
                        (SELECT id FROM Horario WHERE id='{}')
                    )
                    """.format(
                numero, semestre, anio, curso, profesor, hora
            )
            print("Query: {}".format(query), file=sys.stdout)
            self.cur.execute(query)
            self.con.commit()
            query = """
                    INSERT INTO CursosImpartidos
                    VALUES((SELECT pID FROM Profesor WHERE nombre='{}'),(SELECT numero FROM Curso WHERE nombre='{}'),'{}','{}')
                    """.format(
                profesor, curso, semestre, anio
            )
            self.cur.execute(query)
            self.con.commit()
            query = """
                    INSERT INTO NoLibre
                    VALUES(
                        (SELECT pID FROM Profesor WHERE nombre='{}'),
                        (SELECT id FROM Horario WHERE id='{}')
                    )
                    """.format(
                profesor, hora
            )
            print("Query: {}".format(query), file=sys.stdout)
            self.cur.execute(query)
            self.con.commit()
        except Exception as e:
            print("Exception occured: ", e)

    def delete_grupo(self, numero, curso, semestre, year):
        query = """DELETE FROM Grupo
                    WHERE numero='{}'
                    AND semestre='{}'
                    AND anio='{}'
                    AND curso='{}'
                """.format(
            numero, semestre, year, curso
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def list_alumno(self):
        query = """
                SELECT  a.matricula, a.curp, a.nombre, a.sexo, a.bDate, a.telefono, a.celular, a.direccion, d.nombre, a.carrera
                FROM    Alumno a, Departamento d, Carreras c
                WHERE   a.departamento = d.numero
                AND     a.carrera=c.inicialismo
                """
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def list_carreras(self):
        query = "SELECT * FROM Carreras"
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def insert_alumno(
        self,
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
    ):
        try:
            query = """
                    INSERT INTO Alumno
                    VALUES('{}', '{}','{}','{}','{}','{}','{}','{}',(SELECT numero FROM Departamento WHERE nombre='{}'), (SELECT inicialismo FROM Carreras WHERE inicialismo='{}'))
                    """.format(
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
            print("Query: {}".format(query), file=sys.stdout)
            self.cur.execute(query)
            self.con.commit()
        except Exception as e:
            print("Exception occured: ", e)

    def delete_alumno(self, matricula):
        query = """DELETE FROM Alumno
                    WHERE matricula='{}'
                """.format(
            matricula
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def find_alumno(self, matricula):
        query = """
                SELECT  *
                FROM    Alumno
                WHERE   matricula LIKE '%{}%'
                """.format(
            matricula
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def find_departamento(self, nombre):
        query = """
                SELECT  *
                FROM    Departamento
                WHERE   nombre LIKE '%{}%'
                """.format(
            nombre
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def find_grupo(self, curso):
        query = """
                SELECT      g.numero, g.semestre, g.anio, g.curso, g.profesor
                FROM        Grupo g, Curso c
                WHERE       c.nombre LIKE '%{}%'
                AND         g.curso = c.numero
                ORDER BY    g.curso, g.numero ASC
                """.format(
            curso
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def find_profesor(self, nomina):
        query = """
                SELECT  *
                FROM    Profesor
                WHERE   pID LIKE '%{}%'
                """.format(
            nomina
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def list_ecoas(self):
        query = """
                SELECT  p.pID, c.numero, c.nombre, g.numero, g.semestre, g.anio, e.calificacion
                FROM    Ecoas e, Profesor p, Grupo g, Curso c
                WHERE   e.profesor=p.pID
                AND     g.profesor=p.pID
                AND     e.grupo=g.numero
                AND     g.curso=c.numero
                """
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def insert_ecoas(self, profesor, nombre, grupo, semestre, anio, calificacion):
        try:
            query = """
                 INSERT INTO Ecoas
                 VALUES ((
                     SELECT pID FROM Profesor WHERE pID='{}'
                     ), (
                         SELECT numero
                         FROM Grupo
                         WHERE numero='{}'
                         AND profesor='{}'
                         AND semestre='{}'
                         AND anio='{}'
                         AND curso ='{}'
                     ), {})
                 """.format(
                profesor, grupo, profesor, semestre, anio, nombre, calificacion
            )
            print("Query: {}".format(query), file=sys.stdout)
            self.cur.execute(query)
            self.con.commit()
        except Exception as e:
            print("Exception occured: ", e)

    def delete_ecoas(self, profesor, grupo):
        query = """
                DELETE FROM Ecoas
                WHERE       profesor = '{}'
                AND         grupo='{}'
                """.format(
            profesor, grupo
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def find_ecoas(self, nomina):
        query = """
                SELECT  p.pID, c.numero, c.nombre, g.numero, g.semestre, g.anio, e.calificacion
                FROM    Ecoas e, Profesor p, Grupo g, Curso c
                WHERE   e.profesor LIKE '%{}%'
                AND     e.profesor=p.pID
                AND     g.profesor=p.pID
                AND     e.grupo=g.numero
                AND     g.curso=c.numero
                """.format(
            nomina
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def list_impartidos(self):
        query = """
                SELECT  p.pID, p.nombre, c.numero, c.nombre, i.semestre, i.anio
                FROM    Curso c, CursosImpartidos i, Profesor p
                WHERE   i.profesor=p.pID
                AND     i.curso=c.numero
                """
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def find_impartidos(self, nomina):
        query = """
                SELECT  p.pID, p.nombre, c.numero, c.nombre, i.semestre, i.anio
                FROM    Curso c, CursosImpartidos i, Profesor p
                WHERE   i.profesor LIKE '%{}%'
                AND     i.profesor=p.pID
                AND     i.curso=c.numero
                """.format(
            nomina
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def list_pertenece(self):
        query = """
                SELECT  a.matricula, a.nombre, c.numero, c.nombre, g.numero, g.semestre, g.anio
                FROM    Alumno a, Curso c, Grupo g, PerteneceGrupo p
                WHERE   p.alumno=a.matricula
                AND     p.grupo=g.numero
                AND     p.curso=g.curso
                AND     p.semestre=g.semestre
                AND     p.anio=g.anio
                AND     p.curso=c.numero
                """
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def insert_pertenece(self, matricula, curso, grupo, semestre, anio):
        try:
            query = """
                INSERT INTO PerteneceGrupo
                VALUES(
                    (SELECT matricula FROM alumno WHERE matricula='{}'),
                    (SELECT numero FROM curso WHERE numero='{}'),
                    (SELECT numero FROM grupo WHERE numero='{}' AND semestre='{}' AND anio='{}' AND curso='{}'),
                    '{}',
                    '{}'
                )
                """.format(
                matricula, curso, grupo, semestre, anio, curso, semestre, anio
            )
            print("Query: {}".format(query), file=sys.stdout)
            self.cur.execute(query)
            self.con.commit()
            query = """
                    INSERT INTO CursosCursados(alumno, curso, semestre, anio)
                    VALUES(
                        (SELECT matricula FROM Alumno WHERE matricula='{}'),
                        (SELECT numero FROM Curso WHERE numero='{}'),
                        '{}',
                        '{}'
                    )
                    """.format(
                matricula, curso, semestre, anio
            )
            print("Query: {}".format(query), file=sys.stdout)
            self.cur.execute(query)
            self.con.commit()
        except Exception as e:
            print("Exception occured: ", e)

    def delete_pertenece(self, alumno, curso, semestre, anio):
        query = """
                DELETE FROM PerteneceGrupo
                WHERE       alumno = '{}'
                AND         curso='{}'
                AND         semestre='{}'
                AND         anio='{}'
                """.format(
            alumno, curso, semestre, anio
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def list_cursados(self):
        query = """
                SELECT  a.matricula, a.nombre, c.numero, c.nombre, cc.semestre, cc.anio, cc.calificacion
                FROM    Alumno a, Curso c, CursosCursados cc
                WHERE   cc.alumno=a.matricula
                AND     cc.curso=c.numero
                """
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def find_cursados(self, matricula):
        query = """
                SELECT  a.matricula, a.nombre, c.numero, c.nombre, cc.semestre, cc.anio, cc.calificacion
                FROM    Alumno a, Curso c, CursosCursados cc
                WHERE   cc.alumno LIKE '%{}%'
                AND     cc.alumno=a.matricula
                AND     cc.curso=c.numero
                """.format(
            matricula
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def list_horario(self):
        query = "SELECT * FROM Horario"
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def list_no_libre(self, nomina):
        query = """
                SELECT  h.id, h.hora
                FROM    NoLibre n, Horario h, Libre l
                WHERE   n.nomina='{}'
                AND     h.id NOT IN(n.hora)
                """.format(
            nomina
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def list_libre(self):
        query = """
                SELECT  p.pID, p.nombre, h.hora
                FROM    Libre l, Profesor p, Horario h
                WHERE   l.nomina=p.pID
                AND     l.hora=h.id
                """
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def insert_libre(self, nomina, hora):
        try:
            query = """
                INSERT INTO Libre
                VALUES(
                    (SELECT pID FROM Profesor   WHERE pID='{}'),
                    (SELECT id  FROM Horario    WHERE id='{}')
                )
                """.format(
                nomina, hora
            )
            print("Query: {}".format(query), file=sys.stdout)
            self.cur.execute(query)
            self.con.commit()
        except Exception as e:
            print("Exception occured: ", e)

    def find_libre(self, nomina):
        query = """
                SELECT  p.pID, p.nombre, h.hora
                FROM    Libre l, Profesor p, Horario h
                WHERE   l.nomina LIKE '%{}%'
                AND     l.nomina=p.pID
                AND     l.hora=h.id
                """.format(
            nomina
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def delete_libre(self, nomina, hora):
        query = """
                DELETE FROM Libre
                WHERE       nomina = '{}'
                AND         hora IN (SELECT id FROM Horario WHERE hora ='{}')
                """.format(
            nomina, hora
        )
        print("Query: {}".format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

