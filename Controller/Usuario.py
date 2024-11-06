from Model.ConexionDB import ConexionDB
import tkinter as tk
from tkinter import messagebox as mb

class Usuario():
    def __init__(self):
        self.cedula = None
        self.nombre = None
        self.rol = None

    #Poner getters y setters

    def iniciarSesion(self,nombreUsuario,password):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("Select * from usuario")
        listaUsuarios = cursor.fetchall()
        for usuario in listaUsuarios:
            if usuario[2] == nombreUsuario and usuario[1] == password:
                self.cedula = usuario[1]
                self.nombre = usuario[2]
                self.rol = usuario[3]
                mb.showinfo("Información","Acceso Correcto!")
                miConexion.cerrarConexion()
                return
        mb.showwarning("Advertencia","El nombre de usuario y/o contraseña no existen, verifique e intente de nuevo.")
        




