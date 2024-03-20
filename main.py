#""""""""""""""  """"importer les packages nécessaire """""""""""""""""""""""""""""""""

#importer les packages des objets nécessaire de bibliothèque kivy ou kivymd

from kivy.core.window import Window
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.textfield import MDTextField
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.metrics import dp

#import MDDataTable de bibliothèque kivymd pour afficher les donnee de la base de donnee
from kivymd.uix.datatables import MDDataTable


#importer les packages de Property pour les différent return dans les classes

from kivy.properties import StringProperty, OptionProperty, NumericProperty
from kivy.properties import ObjectProperty



#import ScreenManager de bibliothèque kivymd gérer les screen/les interfaces de l'application
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen

#import Image de bibliothèque kivy poue utilise les images dans l'application
from kivy.uix.image import Image

#import mysql  poue connecter avec la base dedonnee
import mysql.connector



#Déterminer la taille et la couleur de l'application
Window.clearcolor = (89 / 255.0, 7 / 255.0, 45, 3)
Window.size = (400, 600)




class Aff_etu_ensa(Screen):

    table = ObjectProperty(MDDataTable)
    def aff_etu_ensa1(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="11121314",
            database="second_db")
        c = mydb.cursor()
        c.execute("select * from ENSA")
        etu = c.fetchall()
        self.table = MDDataTable(
            pos_hint={"center_y": 0.54, "center_x": 0.5},
            size_hint=(0.9, 0.9),
            use_pagination=False,
            column_data=[
                ("CNE ", dp(20)),
                ("NOM    ", dp(20)),
                ("PRENOM ", dp(20)),
                ("ECOLE ", dp(20))],
            row_data=etu, )
        mydb.commit()
        mydb.close()
        self.add_widget(self.table)



class Aff_etu_est(Screen):

    table = ObjectProperty(MDDataTable)
    def aff_etu_est1(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="11121314",
            database="second_db")
        c = mydb.cursor()
        c.execute("select * from EST")
        etu = c.fetchall()
        self.table = MDDataTable(
            pos_hint={"center_y": 0.54, "center_x": 0.5},
            size_hint=(0.9, 0.9),
            use_pagination=False,
            column_data=[
                ("CNE ", dp(20)),
                ("NOM    ", dp(20)),
                ("PRENOM ", dp(20)),
                ("ECOLE ", dp(20))],
            row_data=etu, )
        mydb.commit()
        mydb.close()
        self.add_widget(self.table)


class Aff_etu_fs(Screen):
    table = ObjectProperty(MDDataTable)

    def aff_etu_fs1(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="11121314",
            database="second_db")
        c = mydb.cursor()
        c.execute("select * from FS")
        etu = c.fetchall()
        self.table = MDDataTable(
            pos_hint={"center_y": 0.54, "center_x": 0.5},
            size_hint=(0.9, 0.9),
            use_pagination=False,
            column_data=[
                ("CNE ", dp(20)),
                ("NOM    ", dp(20)),
                ("PRENOM ", dp(20)),
                ("ECOLE ", dp(20))],
            row_data=etu, )
        mydb.commit()
        mydb.close()
        self.add_widget(self.table)

class Aj_etu(Screen):

    def aj_etu1(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="11121314",
            database="second_db")

        c = mydb.cursor()

        def cltxt():
            self.ids.NOM.text = ''
            self.ids.PRENOM.text = ''
            self.ids.CNE.text = ''
            self.ids.ECOLE.text = ''


        v_nom = ''
        v_prenom = ''
        v_cne = 1
        v_ecole='1'
        if self.ids.CNE.text.isnumeric():
            v_cne = int(self.ids.CNE.text)
            self.ids.res.text = ''


            if self.ids.NOM.text !='' :
                v_nom = self.ids.NOM.text
                self.ids.res.text = ''

                if  self.ids.PRENOM.text !='':
                    v_prenom = self.ids.PRENOM.text
                    self.ids.res.text = ''

                    if self.ids.ECOLE.text !='' :
                        v_ecole = self.ids.ECOLE.text
                        self.ids.res.text = ''
                        self.ids.res.text = 'Ajouter val'


                        if v_ecole == 'est' or v_ecole == 'EST' or v_ecole == 'Est':
                            cmd = "INSERT INTO est (CNE, NOM, PRENOM , ECOLE) VALUES (%s,%s,%s,%s)"
                            c.execute(cmd, (v_cne, v_nom, v_prenom,v_ecole))
                            cltxt()
                        elif v_ecole == 'ensa' or v_ecole == 'Ensa' or v_ecole == 'ENSA' :
                            cmd = "INSERT INTO ensa (CNE, NOM, PRENOM , ECOLE) VALUES (%s,%s,%s,%s)"
                            c.execute(cmd, (v_cne, v_nom, v_prenom,v_ecole))
                            cltxt()
                        elif v_ecole == 'FS' or v_ecole == 'Fs' or v_ecole == 'fs':
                            cmd = "INSERT INTO fs (CNE, NOM, PRENOM , ECOLE) VALUES (%s,%s,%s,%s)"
                            c.execute(cmd, (v_cne, v_nom, v_prenom, v_ecole))
                            cltxt()
                        else: self.ids.res.text = 'ECOLE  Incorrect'

                    else:
                        self.ids.res.text = 'ECOLE  Incorrect'
                else:
                    self.ids.res.text = ' PRENOM Incorrect'
            else:
                self.ids.res.text = '  NOM Incorrect'

        else: self.ids.res.text = ' CNE Incorrect'

        mydb.commit()
        mydb.close()


class Aj_mod_ensa(Screen):
    def aj_mod_ensa1(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="11121314",
            database="second_db")

        c = mydb.cursor()

        t2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        t  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        cne = 1
        Annee = 1
        m1 = 1
        m2=1
        m3=3
        m4=4
        m5=5
        m6=6

        def isfloat(num):
            try:
                float(num)
                return True
            except ValueError:
                return False

        def testnot(nt_mod):
            rs_n = ''
            if nt_mod >= 10 and nt_mod <= 20:
                rs_n = 'val'
            elif nt_mod < 10 and nt_mod >= 6:
                 rs_n = 'ratt'
            elif nt_mod < 6:
                rs_n = 'not val'
            else:  rs_n=1
            return rs_n



        if  self.ids.cne.text.isnumeric() :
            cne = int(self.ids.cne.text)
            self.ids.res.text = ''

            if self.ids.Annee.text.isnumeric():
                Annee = int(self.ids.Annee.text)
                self.ids.res.text = ''

                if isfloat(self.ids.m1.text)==True and testnot(float(self.ids.m1.text))!=1 :
                    t[0] = float(self.ids.m1.text)
                    t2[0]=testnot(float(self.ids.m1.text))
                    self.ids.res.text = ''

                    if isfloat(self.ids.m2.text)==True and testnot(float(self.ids.m2.text))!=1:
                        t[1] = float(self.ids.m2.text)
                        t2[1] = testnot(float(self.ids.m2.text))
                        self.ids.res.text = ''

                        if isfloat(self.ids.m3.text)==True and testnot(float(self.ids.m3.text))!=1:
                            t[2] = float(self.ids.m3.text)
                            t2[2] = testnot(float(self.ids.m3.text))
                            self.ids.res.text = ''

                            if isfloat(self.ids.m4.text)==True and testnot(float(self.ids.m4.text))!=1:
                                t[3] = float(self.ids.m4.text)
                                t2[3] = testnot(float(self.ids.m4.text))
                                self.ids.res.text = ''

                                if isfloat(self.ids.m5.text) == True and testnot(float(self.ids.m5.text)) != 1:
                                    t[4] = float(self.ids.m5.text)
                                    t2[4] = testnot(float(self.ids.m5.text))
                                    self.ids.res.text = ''

                                    if isfloat(self.ids.m6.text) == True and testnot(float(self.ids.m6.text)) != 1:
                                        t[5] = float(self.ids.m6.text)
                                        t2[5] = testnot(float(self.ids.m6.text))
                                        self.ids.res.text = ''

                                        if isfloat(self.ids.m7.text) == True and testnot(float(self.ids.m7.text)) != 1:
                                            t[6] = float(self.ids.m7.text)
                                            t2[6] = testnot(float(self.ids.m7.text))
                                            self.ids.res.text = ''

                                            if isfloat(self.ids.m8.text) == True and testnot(float(self.ids.m8.text)) != 1:
                                                t[7] = float(self.ids.m8.text)
                                                t2[7] = testnot(float(self.ids.m8.text))
                                                self.ids.res.text = ''

                                                if isfloat(self.ids.m9.text) == True and testnot(float(self.ids.m9.text)) != 1:
                                                    t[8] = float(self.ids.m9.text)
                                                    t2[8] = testnot(float(self.ids.m9.text))
                                                    self.ids.res.text = ''

                                                    if isfloat(self.ids.m10.text) == True and testnot(float(self.ids.m10.text)) != 1:
                                                        t[9] = float(self.ids.m10.text)
                                                        t2[9] = testnot(float(self.ids.m10.text))
                                                        self.ids.res.text = 'Ajouter val'

                                                        self.ids.cne.text = ''
                                                        self.ids.Annee.text = ''
                                                        self.ids.m1.text = ''
                                                        self.ids.m2.text = ''
                                                        self.ids.m3.text = ''
                                                        self.ids.m4.text = ''
                                                        self.ids.m5.text = ''
                                                        self.ids.m6.text = ''
                                                        self.ids.m7.text = ''
                                                        self.ids.m8.text = ''
                                                        self.ids.m9.text = ''
                                                        self.ids.m10.text = ''



                                                        for i in range(10):
                                                            n_mod = i + 1
                                                            nt_mod = t[i]
                                                            rs_n = t2[i]
                                                            cmd = "INSERT INTO mod_ensa (N_MOD, cne, N_S, NT_N,RS_N) VALUES (%s,%s,%s,%s,%s)"
                                                            c.execute(cmd, (n_mod, cne, Annee, nt_mod, rs_n))

                                                    else:
                                                        self.ids.res.text = 'Note m10 Incorrect'
                                                else:
                                                    self.ids.res.text = 'Note m9 Incorrect'
                                            else:
                                                self.ids.res.text = 'Note m8 Incorrect'
                                        else:
                                            self.ids.res.text = 'Note m7 Incorrect'
                                    else:
                                        self.ids.res.text = 'Note m6 Incorrect'
                                else:
                                    self.ids.res.text = 'Note m5 Incorrect'
                            else:
                                self.ids.res.text = 'Note m4 Incorrect'
                        else:
                            self.ids.res.text = 'Note m3 Incorrect'
                    else:
                        self.ids.res.text = 'Note m2  Incorrect'
                else:
                    self.ids.res.text = 'Note m1 Incorrect'
            else:
                self.ids.res.text = 'num Annee Incorrect'
        else: self.ids.res.text = 'CNE Incorrect'

        mydb.commit()
        mydb.close()




class Aj_mod_fs(Screen):
    def aj_mod_fs1(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="11121314",
            database="second_db")
        c = mydb.cursor()
        t2 = [1, 1, 1, 1, 1, 1]
        t  = [1, 1, 1, 1, 1, 1]
        n_et = 1
        n_s = 1
        m1 = 1
        m2=1
        m3=3
        m4=4
        m5=5
        m6=6

        def isfloat(num):
            try:
                float(num)
                return True
            except ValueError:
                return False

        def testnot(nt_mod):
            rs_n = ''
            if nt_mod >= 10 and nt_mod <= 20:
                rs_n = 'val'
            elif nt_mod < 10 and nt_mod >= 6:
                 rs_n = 'ratt'
            elif nt_mod < 6:
                rs_n = 'not val'
            else:  rs_n=1
            return rs_n

        if  self.ids.n_et.text.isnumeric() :
            n_et = int(self.ids.n_et.text)
            self.ids.res.text = ''

            if self.ids.n_s.text.isnumeric():
                n_s = int(self.ids.n_s.text)
                self.ids.res.text = ''

                if isfloat(self.ids.m1.text)==True and testnot(float(self.ids.m1.text))!=1 :
                    t[0] = float(self.ids.m1.text)
                    t2[0]=testnot(float(self.ids.m1.text))
                    self.ids.res.text = ''

                    if isfloat(self.ids.m2.text)==True and testnot(float(self.ids.m2.text))!=1:
                        t[1] = float(self.ids.m2.text)
                        t2[1] = testnot(float(self.ids.m2.text))
                        self.ids.res.text = ''

                        if isfloat(self.ids.m3.text)==True and testnot(float(self.ids.m3.text))!=1:
                            t[2] = float(self.ids.m3.text)
                            t2[2] = testnot(float(self.ids.m3.text))
                            self.ids.res.text = ''

                            if isfloat(self.ids.m4.text)==True and testnot(float(self.ids.m4.text))!=1:
                                t[3] = float(self.ids.m4.text)
                                t2[3] = testnot(float(self.ids.m4.text))
                                self.ids.res.text = ''

                                if isfloat(self.ids.m5.text) == True and testnot(float(self.ids.m5.text)) != 1:
                                    t[4] = float(self.ids.m5.text)
                                    t2[4] = testnot(float(self.ids.m5.text))
                                    self.ids.res.text = ''

                                    if isfloat(self.ids.m6.text) == True and testnot(float(self.ids.m6.text)) != 1:
                                        t[5] = float(self.ids.m6.text)
                                        t2[5] = testnot(float(self.ids.m6.text))
                                        self.ids.res.text = 'Ajouter val'

                                        self.ids.n_et.text = ''
                                        self.ids.n_s.text = ''
                                        self.ids.m1.text = ''
                                        self.ids.m2.text = ''
                                        self.ids.m3.text = ''
                                        self.ids.m4.text = ''
                                        self.ids.m5.text = ''
                                        self.ids.m6.text = ''

                                        for i in range(6):
                                            n_mod = i + 1
                                            nt_mod = t[i]
                                            rs_n = t2[i]
                                            cmd = "INSERT INTO mod_fs (N_MOD, cne, N_S, NT_N,RS_N) VALUES (%s,%s,%s,%s,%s)"
                                            c.execute(cmd, (n_mod, n_et, n_s, nt_mod, rs_n))
                                    else:
                                        self.ids.res.text = 'Note m6 Incorrect'
                                else:
                                    self.ids.res.text = 'Note m5 Incorrect'
                            else:
                                self.ids.res.text = 'Note m4 Incorrect'
                        else:
                            self.ids.res.text = 'Note m3 Incorrect'
                    else:
                        self.ids.res.text = 'Note m2  Incorrect'
                else:
                    self.ids.res.text = 'Note m1 Incorrect'
            else:
                self.ids.res.text = 'num semestre Incorrect'
        else: self.ids.res.text = 'CNE Incorrect'

        mydb.commit()
        mydb.close()




class Aj_mod_est(Screen):
    def aj_mod_est1(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="11121314",
            database="second_db")

        c = mydb.cursor()



        t2 = [1, 1, 1, 1]
        t=[1,1,1,1]
        n_et = 1
        n_s = 1
        m1 = 1
        m2=1
        m3=3
        m4=4

        def isfloat(num):
            try:
                float(num)
                return True
            except ValueError:
                return False

        def testnot(nt_mod):
            rs_n = ''
            if nt_mod >= 12 and nt_mod <= 20:
                rs_n = 'val'
            elif nt_mod < 12 and nt_mod >= 6:
                 rs_n = 'ratt'
            elif nt_mod < 6:
                rs_n = 'not val'
            else:  rs_n=1
            return rs_n

        if  self.ids.n_et.text.isnumeric() :
            n_et = int(self.ids.n_et.text)
            self.ids.res.text = ''

            if self.ids.n_s.text.isnumeric():
                n_s = int(self.ids.n_s.text)
                self.ids.res.text = ''

                if isfloat(self.ids.m1.text)==True and testnot(float(self.ids.m1.text))!=1 :
                    t[0] = float(self.ids.m1.text)
                    t2[0]=testnot(float(self.ids.m1.text))
                    self.ids.res.text = ''

                    if isfloat(self.ids.m2.text)==True and testnot(float(self.ids.m2.text))!=1:
                        t[1] = float(self.ids.m2.text)
                        t2[1] = testnot(float(self.ids.m2.text))
                        self.ids.res.text = ''

                        if isfloat(self.ids.m3.text)==True and testnot(float(self.ids.m3.text))!=1:
                            t[2] = float(self.ids.m3.text)
                            t2[2] = testnot(float(self.ids.m3.text))
                            self.ids.res.text = ''

                            if isfloat(self.ids.m4.text)==True and testnot(float(self.ids.m4.text))!=1:
                                t[3] = float(self.ids.m4.text)
                                t2[3] = testnot(float(self.ids.m4.text))
                                self.ids.res.text = 'Ajouter val'

                                self.ids.n_et.text=''
                                self.ids.n_s.text=''
                                self.ids.m1.text=''
                                self.ids.m2.text=''
                                self.ids.m3.text=''
                                self.ids.m4.text = ''

                                for i in range(4):
                                    n_mod = i + 1
                                    nt_mod = t[i]
                                    rs_n=t2[i]
                                    cmd = "INSERT INTO MOD_EST (N_MOD, cne, N_S, NT_N,RS_N) VALUES (%s,%s,%s,%s,%s)"
                                    c.execute(cmd, (n_mod, n_et, n_s, nt_mod, rs_n))
                            else:
                                self.ids.res.text = 'Note m4 Incorrect'
                        else:
                            self.ids.res.text = 'Note m3 Incorrect'
                    else:
                        self.ids.res.text = 'Note m2  Incorrect'
                else:
                    self.ids.res.text = 'Note m1 Incorrect'
            else:
                self.ids.res.text = 'num semestre Incorrect'
        else: self.ids.res.text = 'CNE Incorrect'

        mydb.commit()
        mydb.close()


class Aff_mod_ensa(Screen):

    table = ObjectProperty(MDDataTable)
    def aff_mod_ensa1(self):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="11121314",
            database="second_db")
        c = mydb.cursor()
        c.execute("select * from MOD_ENSA ")
        MOD_ENSA = c.fetchall()
        self.table = MDDataTable(
            pos_hint={"center_y": 0.54, "center_x": 0.5},
            size_hint=(0.9, 0.9),
            use_pagination=True,
            column_data=[
                ("N_MOD", dp(20)),
                ("CNE ", dp(20)),
                ("ANNEE", dp(20)),
                ("NT_N", dp(20)),
                ("RS_N", dp(20))],
            row_data=MOD_ENSA, )
        mydb.commit()
        mydb.close()
        self.add_widget(self.table)



class Aff_mod_fs(Screen):
    table = ObjectProperty(MDDataTable)

    def aff_mod_fs1(self):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="11121314",
            database="second_db")
        c = mydb.cursor()
        c.execute("select * from mod_FS ")
        mod_FS = c.fetchall()
        self.table = MDDataTable(
            pos_hint={"center_y": 0.54, "center_x": 0.5},
            size_hint=(0.9, 0.9),
            use_pagination=True,
            column_data=[
                ("N_MOD", dp(20)),
                ("CNE ", dp(20)),
                ("N_S", dp(20)),
                ("NT_N", dp(20)),
                ("RS_N", dp(20))],
            row_data=mod_FS, )
        mydb.commit()
        mydb.close()
        self.add_widget(self.table)

class Aff_mod_est(Screen):

    table = ObjectProperty(MDDataTable)
    def aff_mod_est1(self):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="11121314",
            database="second_db")
        c = mydb.cursor()
        c.execute("select * from mod_est ")
        mod_est = c.fetchall()
        self.table = MDDataTable(
            pos_hint={"center_y": 0.54, "center_x": 0.5},
            size_hint=(0.9, 0.9),
            use_pagination=True,
            column_data=[
                ("N_MOD", dp(20)),
                ("CNE ", dp(20)),
                ("N_S", dp(20)),
                ("NT_N", dp(20)),
                ("RS_N", dp(20))],
            row_data=mod_est, )
        mydb.commit()
        mydb.close()
        self.add_widget(self.table)




class Error(Screen):
    pass

class Mod(Screen):
    pass



class Etu(Screen):
    pass



class Est(Screen):
    pass


class Ensa(Screen):
    pass

class Fs(Screen):
    pass


class W1(Screen):
    pass


class W2(Screen):
    pass


class Wm(ScreenManager):
    MY_GLOBAL= StringProperty('')


kv = Builder.load_file('name.kv')


class MyAPP(MDApp):
    def build(self):
        self.title = 'Universite Ibn Tofail'
        return kv

if __name__ == '__main__':
    MyAPP().run()
