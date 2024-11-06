import tkinter as tk
from  tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from View.CrearUsuario import CrearUsuario
from View.EliminarUsuario import EliminarUsuario
from View.ModificarUsuario import ModificarUsuario


class ConsultarUsuarios():

    def CrearUsuario(self,event):
        crear=CrearUsuario(self.ventana,self.usuario)

    def EliminarUsuario(self,event):
        eliminar=EliminarUsuario(self.ventana)

    def ModificarUsuario(self,event):
        modificar=ModificarUsuario(self.ventana)


    def __init__(self,loggin,usuario):
        self.ventana = tk.Toplevel(loggin)
        self.ventana.title("Tabla de Usuarios")
        self.ventana.config(width=600)
        self.ventana.resizable(0,0)

        self.usuario = usuario

        self.lblTitulo=tk.Label(self.ventana,text="Listado de Usuarios")
        self.lblTitulo.pack()

        self.tabla=ttk.Treeview(self.ventana)
        self.tabla["columns"] = ["ID","Cedula","Nombre","Rol"]
        self.tabla.heading("#1",text="ID")
        self.tabla.heading("#2",text="Cedula")
        self.tabla.heading("#3",text="Nombre")
        self.tabla.heading("#4",text="Rol")

        self.listaUsuarios = usuario.consultarTabla()

        for usuario in self.listaUsuarios:
            self.tabla.insert("",  "end", values=(usuario[0], usuario[1], usuario[2], usuario[3]))

        self.tabla["show"] = "headings"
        self.tabla.column("#1",width=50)
        self.tabla.column("#2",width=100)
        self.tabla.column("#3",width=300)
        self.tabla.column("#4",width=100)

        self.scrollbar = ttk.Scrollbar(self.ventana,  orient="vertical", command=self.tabla.yview)
        self.tabla.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right",fill="y")

        self.tabla.pack(fill="both",expand=True)

        self.botones = tk.Frame(self.ventana)
        self.botones.config(width=600,height=100)
        self.botones.pack(fill="both",expand=True)

        self.icono_crear=tk.PhotoImage(file=r"src\icons\user_add.png")
        self.btncrear_usuario=tk.Button(self.botones,image=self.icono_crear)
        self.btncrear_usuario.place(relx=0.5,x=-50,y=25,anchor="nw")
        self.btncrear_usuario.bind("<Button-1>",self.CrearUsuario)

        self.icono_eliminar=tk.PhotoImage(file=r"src\icons\user_delete.png")
        self.btnEliminar_usuario=tk.Button(self.botones,image=self.icono_eliminar)
        self.btnEliminar_usuario.place(relx=0.5,y=25,anchor="n")
        self.btnEliminar_usuario.bind("<Button-1>",self.EliminarUsuario)


        self.icono_modificar=tk.PhotoImage(file=r"src\icons\user_edit.png")
        self.btnModificar_usuario=tk.Button(self.botones,image=self.icono_modificar)
        self.btnModificar_usuario.place(relx=0.5,x=50,y=25,anchor="ne")
        self.btnModificar_usuario.bind("<Button-1>",self.ModificarUsuario)


        self.ventana.mainloop()

