import pymysql
import sys

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
        query = '''
                SELECT * 
                FROM Member
                '''
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_member(self, member_no, member_name):
        if member_no == '':
            print('isnill!!!!!!!!!!!!! {}', file=sys.stdout)
        query = '''
                SELECT *
                FROM Member
                '''
        if member_no != '':
            query += 'WHERE memberNo = {}'.format(member_no)
            if member_name != '':
                query += 'AND fName = \'{}\''.format(member_name)
        elif member_name != '':
            query += 'WHERE fName = \'{}\''.format(member_name)

        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def SP_list_members(self):
        self.cur.callproc('GetAllMembers')
        result = self.cur.fetchall()

        return result


    def top_and_bottom_clients(self):
        query = '''
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
                '''
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result
