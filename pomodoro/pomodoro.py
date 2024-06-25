import tkinter as tk
import time
from playsound import playsound

# Configuración de la ventana principal
root = tk.Tk()
root.title("Pomodoro")
root.config(bg="#000000")

# Configuración de la barra de progreso
progress_bar = tk.Canvas(root, width=200, height=5, bg="#ffffff")
progress_bar.pack(pady=0)

# Configuración de la etiqueta de temporizador
timer_label = tk.Label(root, text="25:00", font=("Arial", 48), bg="#000000", fg="#ffffff")
timer_label.pack(pady=0)

# Función para actualizar el temporizador y la barra de progreso
def update_timer_and_progress(current_time, total_time):
    # Calcular el porcentaje completado de la tarea actual
    completion_percentage = (current_time * 100) / total_time

    # Actualizar el temporizador
    minutes, seconds = divmod(current_time, 60)
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

    # Actualizar la barra de progreso
    progress_bar.delete("all")
    progress_bar.create_rectangle(0, 0, int(completion_percentage * 2), 20, fill="#000000")

# Función para ejecutar el temporizador
def run_timer(minutes):
    for i in range(minutes * 60, -1, -1):
        update_timer_and_progress(i, minutes * 60)
        root.update()
        time.sleep(1)

        if i == 0 :
         playsound("/home/wilson/descanso.mp3")


# Función para ejecutar un ciclo de trabajo y descanso
def run_cycle(work_minutes, break_minutes, cycles):
    for i in range(cycles):
        run_timer(work_minutes)
        if i < cycles - 1:
            run_timer(break_minutes)

# Función para iniciar o detener el temporizador
def start_stop_timer():
    global start_time, paused_time, is_running

    # Si el temporizador está detenido
    if not is_running:
        # Inicializar el temporizador
        start_time = time.time()
        paused_time = 0
        is_running = True
        button_3.config(text="Detener")
    # Si el temporizador está corriendo
    else:
        # Detener el temporizador
        paused_time += time.time() - start_time
        is_running = False
        button_3.config(text="Iniciar")

# Crear un Frame para los botones
button_frame = tk.Frame(root, bg="#000000")
button_frame.pack(side=tk.BOTTOM, pady=10)

# Crear los botones simétricos
button_1 = tk.Button(button_frame, text="25", width=8, height=1, relief="groove", bg="#000000", fg="#ffffff",
                     command=lambda: run_timer(25))
button_2 = tk.Button(button_frame, text="", width=8, height=1, relief="groove", bg="#290000", fg="#ffffff",
                     command=root.quit)
button_3 = tk.Button(button_frame, text="5 ", width=8, height=1, relief="groove", bg="#090037", fg="#ffffff",
                     command=lambda: run_timer(5))

# Agregar los botones al Frame
button_1.pack(side=tk.LEFT, padx=10)
button_2.pack(side=tk.LEFT, padx=10)
button_3.pack(side=tk.LEFT, padx=10)

# Ejecución del pomodoro
while True:
    run_cycle(25, 5, 2)
    run_timer(15)

# Iniciar el bucle principal
root.mainloop()