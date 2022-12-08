# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:26:03 2022

@author: waltersr
"""

import pandas as pd
import sqlite3


class user:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        con = sqlite3.connect('userDB.db')
        c = con.cursor()
        c.execute("SELECT password FROM user WHERE username = ?", (self.username,))
        db_pass = c.fetchone()
        if db_pass is not None:
            if db_pass[0] == self.password:
                print('login succefull')
            else:
                print('login failed password did not match database')
        else:
            c.execute("INSERT INTO user (username, password) VALUES ( ?, ?)", (self.username, self.password))
            con.commit()
            print('new profile created welcome')
        con.close


user = user("admin", "1234")