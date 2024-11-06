from Model.ConexionDB import ConexionDB
import tkinter as tk
from tkinter import messagebox as mb
from View.ConsultarUsuarios import ConsultarUsuarios

class Usuario():
    def __init__(self):
        self.cedula = None
        self.nombre = None
        self.rol = None

    #Poner getters y setters

    def iniciarSesion(self,nombreUsuario,password,loggin):
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
                if (usuario[3] == "admin"):
                    mb.showinfo("Información","Acceso correcto! Administrador")
                    #Crear objeto Mesero
                    miMenu = ConsultarUsuarios(loggin,self)
                else:
                    mb.showinfo("Información","Acceso Correcto! Usuario")
                miConexion.cerrarConexion()
                return
        mb.showwarning("Advertencia","El nombre de usuario y/o contraseña no existen, verifique e intente de nuevo.")
        
    def consultarTabla(self):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("Select * from usuario")
        listaUsuarios = cursor.fetchall()
        return listaUsuarios

    def CrearUsuario(self,nombreUsuario,cedulaUsuario,rolUsuario):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("Insert into usuario (cedula,nombre,rol) Values (?,?,?)",(cedulaUsuario,nombreUsuario,rolUsuario))
        miConexion.cerrarConexion()

    def EliminarUsuario(self,cedulaUsuario):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("Delete from usuario where cedula = "+cedulaUsuario)
        miConexion.cerrarConexion()

    def ModificarUsuario(self,cedulaUsuario):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("Update usuario set nombre=?, rol=? where cedula=?",(nombreUsuario,rolUsuario,cedulaUsuario))
        miConexion.cerrarConexion()

    def BuscarUsuario(self,cedulaUsuario):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("Select * from usuario where cedula="+cedulaUsuario)
        listaUsuarios = cursor.fetchall()
        miConexion.cerrarConexion()
        if (len(listaUsuarios))>0:
            usuario=listaUsuarios[0]
            return usuario
        else:
            return None
    
