import tkinter as tk

def validar_entry_int(entrada):
    # Verificar si la entrada es un entero
    try:
        if entrada == "":
            pass
        else: 
            int(entrada)
        return True
    except ValueError:
        return False

def validar_entry_str(entrada):
    # Verificar si la entrada es un entero
    try:
        str(entrada)
        return True
    except ValueError:
        return False

def validar_entry_float(entrada):
    # Verificar si la entrada es un entero
    try:
        if entrada == "":
            pass
        else: 
            float(entrada)
        return True
    except ValueError:
        return False
    
    
if __name__ == "__main__":
    
    # Uso
    
    ventana = tk.Tk()
    root = tk.Frame(ventana)
    root.pack()

    # Función de validación vinculada al Entry
    vcmd_int = root.register(lambda P: validar_entry_int(P))
    vcmd_str = root.register(lambda P: validar_entry_str(P))
    vcmd_float = root.register(lambda P: validar_entry_float(P))

    # Crear un Entry con validación
    entry = tk.Entry(root, validate="key", validatecommand=(vcmd_int, '%P'))
    entry.pack(pady=10)
    entry = tk.Entry(root, validate="key", validatecommand=(vcmd_str, '%P'))
    entry.pack(pady=10)

    entry = tk.Entry(root, validate="key", validatecommand=(vcmd_float, '%P'))
    entry.pack(pady=10)
    ventana.mainloop()