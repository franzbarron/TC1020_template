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

    def insert_grupo(self, numero, semestre, anio, curso, profesor):
        try:
            query = """
            INSERT INTO Grupo
            VALUES({},'{}',{},(SELECT numero FROM Curso WHERE nombre='{}'),(SELECT pID FROM Profesor WHERE nombre='{}'))""".format(
                numero, semestre, anio, curso, profesor
            )
            print("Query: {}".format(query), file=sys.stdout)
            self.cur.execute(query)
            self.con.commit()
        except Exception as e:
            print("Exception occured: ", e)

    def delete_grupo(self, numero, semestre, year, curso):
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
                FROM    Alumno a, Departamento d
                WHERE   a.departamento = d.numero
                """
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
                    VALUES('{}', '{}','{}','{}','{}','{}','{}','{}',(SELECT numero FROM Departamento WHERE nombre='{}'), '{}')
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

    # def top_and_bottom_clients(self):
    #     query = """
    #             select CONCAT(fName,' ',lName) Nombre,
    #                    'Con mas videos rentados' AS Posicion
    #             from Member
    #             where memberNo in
    #             (select memberNo
    #             from RentalAgreement
    #             group by memberNo
    #             having count(videoNo) >= all
    #                       (select count(videoNo)
    #                        from RentalAgreement
    #                        group by memberNo))
    #             UNION
    #             select CONCAT(fName,' ',lName)Nombre, 'Con menos videos rentados' AS Posicion
    #             from Member
    #             where memberNo in
    #             (select memberNo
    #             from RentalAgreement
    #             group by memberNo
    #             having count(videoNo) <= all
    #                       (select count(videoNo)
    #                        from RentalAgreement
    #                        group by memberNo))
    #             """
    #     print("Query: {}".format(query), file=sys.stdout)
    #     self.cur.execute(query)
    #     result = self.cur.fetchall()

    #     return result
