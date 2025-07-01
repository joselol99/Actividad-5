import math
import tkinter as tk
from tkinter import messagebox

class CalculadoraNumerica:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculos Numéricos")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        self.configurar_interfaz()
    
    def configurar_interfaz(self):
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(
            main_frame, 
            text="Calculadora de Operaciones Matemáticas", 
            font=("Arial", 12, "bold")
        ).pack(pady=(0, 20))
        
        input_frame = tk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(input_frame, text="Valor numérico:", font=("Arial", 10)).pack(side=tk.LEFT)
        
        self.entrada_valor = tk.Entry(input_frame, font=("Arial", 10), width=15)
        self.entrada_valor.pack(side=tk.LEFT, padx=10)
        self.entrada_valor.focus()
        
        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=15)
        
        tk.Button(
            button_frame, 
            text="Calcular Logaritmo", 
            command=self.calcular_logaritmo,
            bg="#4a7abc",
            fg="white",
            font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame, 
            text="Calcular Raíz Cuadrada", 
            command=self.calcular_raiz,
            bg="#5d9b66",
            fg="white",
            font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT, padx=5)
        
        # Resultados
        results_frame = tk.Frame(main_frame)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        log_frame = tk.Frame(results_frame)
        log_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            log_frame, 
            text="Logaritmo:", 
            font=("Arial", 10, "bold"),
            width=15,
            anchor="w"
        ).pack(side=tk.LEFT)
        
        self.resultado_log = tk.Label(
            log_frame, 
            text="---", 
            font=("Arial", 10),
            fg="#1a5fb4"
        )
        self.resultado_log.pack(side=tk.LEFT)
        
        raiz_frame = tk.Frame(results_frame)
        raiz_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            raiz_frame, 
            text="Raíz Cuadrada:", 
            font=("Arial", 10, "bold"),
            width=15,
            anchor="w"
        ).pack(side=tk.LEFT)
        
        self.resultado_raiz = tk.Label(
            raiz_frame, 
            text="---", 
            font=("Arial", 10),
            fg="#26a269"
        )
        self.resultado_raiz.pack(side=tk.LEFT)
        
        tk.Button(
            main_frame, 
            text="Limpiar Resultados", 
            command=self.limpiar_resultados,
            font=("Arial", 9)
        ).pack(pady=10)
    
    def obtener_valor(self):
        valor_str = self.entrada_valor.get()
        if not valor_str:
            messagebox.showwarning("Campo Vacío", "Por favor ingrese un valor numérico")
            return None
        
        try:
            return float(valor_str)
        except ValueError:
            messagebox.showerror("Error de Entrada", "El valor debe ser numérico")
            return None
    
    def calcular_logaritmo(self):
        valor = self.obtener_valor()
        if valor is None:
            return
        
        try:
            if valor <= 0:
                raise ValueError("El valor debe ser un número positivo")
            
            resultado = math.log(valor)
            self.resultado_log.config(text=f"{resultado:.4f}")
        except ValueError:
            self.resultado_log.config(text="Error: valor debe ser positivo")
    
    def calcular_raiz(self):
        valor = self.obtener_valor()
        if valor is None:
            return
        
        try:
            if valor < 0:
                raise ValueError("El valor debe ser un número positivo")
            
            resultado = math.sqrt(valor)
            self.resultado_raiz.config(text=f"{resultado:.4f}")
        except ValueError:
            self.resultado_raiz.config(text="Error: valor debe ser positivo")
    
    def limpiar_resultados(self):
        self.entrada_valor.delete(0, tk.END)
        self.resultado_log.config(text="---")
        self.resultado_raiz.config(text="---")
        self.entrada_valor.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraNumerica(root)
    root.mainloop()