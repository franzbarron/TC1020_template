import pymysql

class Database:
    def __init__(self):
        # host = "127.0.0.1"
        host = "localhost"
        user = "root"
        password = "root"
        db = "StayHome"
        port = 8889

        self.con = pymysql.connect( host=host, 
                                    user=user, 
                                    password=password, 
                                    db=db, 
                                    port=port, 
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def list_members(self):
        self.cur.execute('''
                            SELECT * 
                            FROM Member
                        ''')
        result = self.cur.fetchall()

        return result

    def SP_list_members(self):
        self.cur.callproc('GetAllMembers')
        result = self.cur.fetchall()

        return result


    def top_and_bottom_clients(self):
        self.cur.execute('''
                        select CONCAT(fName,' ',lName) Nombre,
                               'Con mas videos rentados' AS Posicion
                        from Member
                        where memberNo in
                        (select memberNo
                        from RentalAgreement
                        group by memberNo
                        having count(videoNo) >= all
                                  (select count(videoNo)
                                   from RentalAgreement
                                   group by memberNo))
                        UNION
                        select CONCAT(fName,' ',lName)Nombre, 'Con menos videos rentados' AS Posicion
                        from Member
                        where memberNo in
                        (select memberNo
                        from RentalAgreement
                        group by memberNo
                        having count(videoNo) <= all
                                  (select count(videoNo)
                                   from RentalAgreement
                                   group by memberNo))
                        ''')
        result = self.cur.fetchall()

        return result
