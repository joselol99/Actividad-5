import tkinter as tk
from tkinter import messagebox, ttk
import re

class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.programadores = []
        self.tamano_maximo = 3
    
    def esta_lleno(self):
        return len(self.programadores) >= self.tamano_maximo
    
    def anadir_programador(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores.append(programador)
    
    @staticmethod
    def validar_campo(campo):
        if any(char.isdigit() for char in campo):
            raise Exception("El nombre no puede tener dígitos.")
        if len(campo) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")
        return True

class EquipoMaratonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Equipo de Maratón")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        self.equipo = None
        self.programadores = []
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        estilo = ttk.Style()
        estilo.configure("Titulo.TLabel", font=("Arial", 14, "bold"), foreground="#1e3f7e")
        estilo.configure("Subtitulo.TLabel", font=("Arial", 11, "bold"), foreground="#2c5282")
        estilo.configure("Entrada.TEntry", padding=5)
        estilo.configure("Boton.TButton", font=("Arial", 10), padding=5)
        
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        ttk.Label(
            self.scrollable_frame, 
            text="Registro de Equipo para Maratón de Programación", 
            style="Titulo.TLabel"
        ).grid(row=0, column=0, columnspan=2, pady=15)
        
        ttk.Label(
            self.scrollable_frame, 
            text="Datos del Equipo", 
            style="Subtitulo.TLabel"
        ).grid(row=1, column=0, columnspan=2, sticky="w", pady=(10, 5))
        
        ttk.Label(self.scrollable_frame, text="Nombre del Equipo:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.nombre_equipo = ttk.Entry(self.scrollable_frame, width=40, style="Entrada.TEntry")
        self.nombre_equipo.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        
        ttk.Label(self.scrollable_frame, text="Universidad:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.universidad = ttk.Entry(self.scrollable_frame, width=40, style="Entrada.TEntry")
        self.universidad.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
        
        ttk.Label(self.scrollable_frame, text="Lenguaje de Programación:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.lenguaje = ttk.Entry(self.scrollable_frame, width=40, style="Entrada.TEntry")
        self.lenguaje.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
        
        ttk.Separator(self.scrollable_frame, orient="horizontal").grid(
            row=5, column=0, columnspan=2, sticky="ew", pady=15
        )
        
        ttk.Label(
            self.scrollable_frame, 
            text="Programadores (Máximo 3)", 
            style="Subtitulo.TLabel"
        ).grid(row=6, column=0, columnspan=2, sticky="w", pady=(5, 10))
        
        self.frames_programadores = []
        self.nombres_programadores = []
        self.apellidos_programadores = []
        
        for i in range(3):
            frame = ttk.LabelFrame(self.scrollable_frame, text=f"Programador {i+1}")
            frame.grid(row=7+i, column=0, columnspan=2, sticky="ew", padx=5, pady=5, ipadx=5, ipady=5)
            self.frames_programadores.append(frame)
            
            ttk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
            nombre = ttk.Entry(frame, width=30)
            nombre.grid(row=0, column=1, sticky="ew", padx=5, pady=2)
            self.nombres_programadores.append(nombre)
            
            ttk.Label(frame, text="Apellidos:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
            apellidos = ttk.Entry(frame, width=30)
            apellidos.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
            self.apellidos_programadores.append(apellidos)
        
        button_frame = ttk.Frame(self.scrollable_frame)
        button_frame.grid(row=10, column=0, columnspan=2, pady=20)
        
        ttk.Button(
            button_frame, 
            text="Registrar Equipo", 
            command=self.registrar_equipo,
            style="Boton.TButton"
        ).pack(side=tk.LEFT, padx=10)
        
        ttk.Button(
            button_frame, 
            text="Limpiar Formulario", 
            command=self.limpiar_formulario,
            style="Boton.TButton"
        ).pack(side=tk.LEFT, padx=10)
    
    def validar_campos(self):
        campos_equipo = {
            "Nombre del equipo": self.nombre_equipo.get(),
            "Universidad": self.universidad.get(),
            "Lenguaje de programación": self.lenguaje.get()
        }
        
        for campo, valor in campos_equipo.items():
            if not valor.strip():
                raise Exception(f"El campo '{campo}' no puede estar vacío")
            EquipoMaratonProgramacion.validar_campo(valor)
        
        programadores_validos = 0
        for i in range(3):
            nombre = self.nombres_programadores[i].get().strip()
            apellidos = self.apellidos_programadores[i].get().strip()
            
            if nombre or apellidos:
                if not nombre:
                    raise Exception(f"Falta el nombre del programador {i+1}")
                if not apellidos:
                    raise Exception(f"Faltan los apellidos del programador {i+1}")
                
                EquipoMaratonProgramacion.validar_campo(nombre)
                EquipoMaratonProgramacion.validar_campo(apellidos)
                programadores_validos += 1
        
        if programadores_validos == 0:
            raise Exception("Debe registrar al menos un programador")
        
        return True
    
    def registrar_equipo(self):
        try:
            self.validar_campos()
            
            self.equipo = EquipoMaratonProgramacion(
                self.nombre_equipo.get(),
                self.universidad.get(),
                self.lenguaje.get()
            )
            
            for i in range(3):
                nombre = self.nombres_programadores[i].get().strip()
                apellidos = self.apellidos_programadores[i].get().strip()
                
                if nombre and apellidos:
                    programador = Programador(nombre, apellidos)
                    self.equipo.anadir_programador(programador)
            
            messagebox.showinfo(
                "Registro Exitoso",
                f"Equipo '{self.equipo.nombre_equipo}' registrado con éxito con {len(self.equipo.programadores)} programadores!"
            )
            
            print("\n--- EQUIPO REGISTRADO ---")
            print(f"Nombre: {self.equipo.nombre_equipo}")
            print(f"Universidad: {self.equipo.universidad}")
            print(f"Lenguaje: {self.equipo.lenguaje_programacion}")
            print("\nProgramadores:")
            for i, p in enumerate(self.equipo.programadores, 1):
                print(f"{i}. {p.nombre} {p.apellidos}")
            
            self.limpiar_formulario()
            
        except Exception as e:
            messagebox.showerror("Error de Validación", str(e))
    
    def limpiar_formulario(self):
        self.nombre_equipo.delete(0, tk.END)
        self.universidad.delete(0, tk.END)
        self.lenguaje.delete(0, tk.END)
        
        for i in range(3):
            self.nombres_programadores[i].delete(0, tk.END)
            self.apellidos_programadores[i].delete(0, tk.END)
        
        self.equipo = None
        self.programadores = []

if __name__ == "__main__":
    root = tk.Tk()
    app = EquipoMaratonApp(root)
    root.mainloop()