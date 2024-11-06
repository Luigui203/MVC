import tkinter as tk 
from tkinter import *
from tkinter import messagebox as mb

class CrearUsuario():

    def GuardarUsuario(self,event):
        self.usuario.CrearUsuario(self.txtNombre.get(),self.txtCedula.get(),self.txtRol.get())
        mb.showinfo("Confirmación","Nuevo  usuario creado con éxito")

    def Limpiar(self,event):
        pass


    def __init__(self,menu,usuario):
        self.ventana = tk.Toplevel(menu)
        self.ventana.geometry("360x385")
        self.ventana.resizable(0,0)
        self.ventana.title("Crear Nuevo Usuario") 

        self.usuario = usuario

        self.lblTitulo=tk.Label(self.ventana,text="Crear Usuario")
        self.lblTitulo.place(relx=0.5,y=50,anchor="center")  

        self.lblNombre=tk.Label(self.ventana,text="Nombre*:")
        self.lblNombre.place(x=50,y=125)

        self.lblCedula=tk.Label(self.ventana,text="Cédula*:")
        self.lblCedula.place(x=50,y=180)     
 
        self.lblRol=tk.Label(self.ventana,text="Rol*:")
        self.lblRol.place(x=50,y=235)     

        self.txtNombre=tk.Entry(self.ventana)
        self.txtNombre.place(x=160,y=125,width=150,height=25)

        self.txtCedula=tk.Entry(self.ventana)
        self.txtCedula.place(x=160,y=180,width=150,height=25)

        self.txtRol=tk.Entry(self.ventana)
        self.txtRol.place(x=160,y=235,width=150,height=25)

        self.icono_guardar=tk.PhotoImage(file=r"MVC\src\icons\disk.png")
        self.btnGuardar=tk.Button(self.ventana,text="Guardar",image=self.icono_guardar,compound="left")
        self.btnGuardar.place(x=70,y=310,width=80,height=25)
        self.btnGuardar.bind("<Button-1>",self.GuardarUsuario)
        
        self.icono_limpiar=tk.PhotoImage(file=r"MVC\src\icons\bin_closed.png")
        self.btnLimpiar=tk.Button(self.ventana,text="Limpiar",image=self.icono_limpiar,compound="left")
        self.btnLimpiar.place(x=195,y=310,width=80,height=25)

        self.ventana.mainloop()