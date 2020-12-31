import os
import bcrypt
import mysql.connector as mysql


class Messenger:
    def __init__(self):
        self.DB = mysql.connect(
            host = os.environ.get('DB_HOST'),
            user = os.environ.get('DB_USER'),
            passwd = os.environ.get('DB_PSWD'),
            database = os.environ.get('DB')
        )

    def create_user(self, info):
        self.cursor = self.DB.cursor(buffered=True)
        
        self.cursor.execute(
            "INSERT INTO users ( "\
                "user_name, "\
                "pswd, "\
                "hint, "\
                "user_type, "\
                "first_name, "\
                "second_name, "\
                "f_last_name, "\
                "m_last_name) "\
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (info[0],   # user_name. 
            bcrypt.hashpw(info[1].encode('utf-8'), bcrypt.gensalt()),   #Hashing the password.
            info[2],    # hint.
            info[3],    # user_type.
            info[4],    # first_name.
            info[5],    # second_name.
            info[6],    # f_last_name.
            info[7])    # m_last_name.
        )

        self.DB.commit()
        self.cursor.close()


    def check_credentials(self, user_name,pswd):
        password = self.get_hashed_pswd(user_name)
        print(bcrypt.checkpw(pswd,password))


    def get(self, value, user_name):
        self.cursor = self.DB.cursor(buffered=True)

        self.cursor.execute(
            "SELECT %s FROM users WHERE user_name = %s",
            (value, user_name)
        )

        self.cursor.close
        return self.cursor.fetchone()[0]
