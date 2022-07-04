from turtle import back
from evaluate import evaluate_function_list
from expression_checker import *
from numerical_methods import *
from clear_cache import *
from decorators import *
from parser import *
from errors import *
from plot import *

from tkinter import messagebox
import tkinter

# Numero de iteraciones en los metodos de integracion
ITERATIONS = 100000

# Cierra el programa
def close_program():

    exit(0)

# Envia mensaje al usuario
def send_message(text, title):

    messagebox.showinfo(message=text, title=title)

# Envia mensaje de error al usuario
def send_error(text):

    send_message(text, 'Error')

# Elimina todos los widgets de la ventana excepto el background
def clean_window():

    for x in app.place_slaves():

        if x != background:

            x.place_forget()

# Muestra la ayuda
def show_help():

    send_message('F(x) - math expression containing only the variable \'x\'\nLimA - float number or \'-inf\'\nLimB - float number or \'inf\'\nError - float positive number representing the relative error','Help')

# Valida la entrada
def validate():

    clear_cache()

    function_string = function_entry.get()
    lim_a = lim_a_entry.get()
    lim_b = lim_b_entry.get()
    relative_error = relative_error_entry.get()

    expression_checker(function_string)

    if check_syntax_error():

        send_error('The expression syntax is incorrect. Repeat it again')

        return

    try:

        lim_a = float(lim_a)

        assert(lim_a != float('inf'))

    except:

        send_error('The LimA is incorrect. Repeat it again')

        return

    try:

        lim_b = float(lim_b)

        assert(lim_b != float('-inf'))

    except:

        send_error('The LimB is incorrect. Repeat it again')

        return

    if float(lim_a) > float(lim_b):

        send_error('The LimA must be less or equal than LimB. Repeat it again')

        return

    try:

        relative_error = float(relative_error)

    except:

        send_error('The Error is incorrect. Repeat it again')

        return

    if float(relative_error) <= 0:

        send_error('The Error must be greater than 0. Repeat it again')

        return

    integrate(function_string, lim_a, lim_b, relative_error)

# Integra la funcion definida
def integrate(function_string, lim_a, lim_b, relative_error):

    parse(function_string)

    import function

    if lim_a == float('-inf') and lim_b == float('inf'):

        new_function = inf_to_inf(function.function, lim_a, lim_b)
        new_lim_a = -1
        new_lim_b = 1

    elif lim_a == float('-inf'):

        new_function = inf_to_float(function.function, lim_a, lim_b)
        new_lim_a = 0
        new_lim_b = 1

    elif lim_b == float('inf'):

        new_function = float_to_inf(function.function, lim_a, lim_b)
        new_lim_a = 0
        new_lim_b = 1

    else:

        new_function = function.function
        new_lim_a = lim_a
        new_lim_b = lim_b

    value = adaptive_integration_method(new_function, new_lim_a, new_lim_b, ITERATIONS, relative_error)

    if check_name_error():

        send_error('There is a variable name error, the variable name in the function must be \'x\'')

        return

    if check_integration_error():

        send_error('The function is not integrable in this interval')

        return

    if check_infinity_error() or value == float('-inf') or value == float('inf'):

        if value > 0:

            value = float('inf')

        else:

            value = float('-inf')

    if lim_a == float('-inf') and lim_b == float('inf'):

        plot_function(function.function, function_string, -100, 100, -100, 100, value, lim_a, lim_b, ITERATIONS)

    elif lim_a == float('-inf'):

        plot_function(function.function, function_string, lim_b - 10*max(1,abs(lim_b)), lim_b + max(1,abs(lim_b)), lim_b - 10*max(1,abs(lim_b)), lim_b, value, lim_a, lim_b, ITERATIONS)

    elif lim_b == float('inf'):

        plot_function(function.function, function_string, lim_a - max(1,abs(lim_a)), lim_a + 10*max(1,abs(lim_a)), lim_a, lim_a + 10*max(1,abs(lim_a)), value, lim_a, lim_b, ITERATIONS)

    else:

        plot_function(function.function, function_string, lim_a - (lim_b - lim_a) * 0.2, lim_b + (lim_b - lim_a) * 0.2, lim_a, lim_b, value, lim_a, lim_b, ITERATIONS)

    clean_window()

    farewell = tkinter.Button(app, text='Have a nice day :)', font=('Verdana', 20), foreground='white', background='grey', command=close_program)

    farewell.place(x=100, y=150, width=400, height=100)


# Creando la ventana
app = tkinter.Tk()

# Titulo de la ventana
app.title('Integration')
# Resolucion de la ventana
app.geometry('600x400')
# Resolucion de la ventana no reajustable
app.resizable(False, False)

# Background
background_image = tkinter.PhotoImage(file='background.png')
background = tkinter.Label(app, image=background_image)
background.place(x=0, y=0)

# Entradas de la ventana
function_entry = tkinter.Entry(app, font=('Verdana', 20), foreground='white', background='grey')
lim_a_entry = tkinter.Entry(app, font=('Verdana', 20), foreground='white', background='grey')
lim_b_entry = tkinter.Entry(app, font=('Verdana', 20), foreground='white', background='grey')
relative_error_entry = tkinter.Entry(app, font=('Verdana', 20), foreground='white', background='grey')

# Etiquetas de la ventana
function_text = tkinter.Label(app, text='F(x) =', font=('Verdana', 20), foreground='white', background='grey')
lim_a_text = tkinter.Label(app, text='LimA =', font=('Verdana', 20), foreground='white', background='grey')
lim_b_text = tkinter.Label(app, text='LimB =', font=('Verdana', 20), foreground='white', background='grey')
relative_error_text = tkinter.Label(app, text='Error =', font=('Verdana', 20), foreground='white', background='grey')

# Botones de la ventana
bottom = tkinter.Button(app, text='Integrate', foreground='white', background='grey', font=('Verdana', 20), command=validate)
bottom_help = tkinter.Button(app, text='Help', foreground='white', background='grey', font=('Verdana', 20), command=show_help)

# Ubicando entradas
function_entry.place(x=120, y=20, width=450, height=50)
lim_a_entry.place(x=120, y=100, width=450, height=50)
lim_b_entry.place(x=120, y=180, width=450, height=50)
relative_error_entry.place(x=120, y=260, width=450, height=50)

# Ubicando etiquetas
function_text.place(x=10, y=20, width=100, height=50)
lim_a_text.place(x=10, y=100, width=100, height=50)
lim_b_text.place(x=10, y=180, width=100, height=50)
relative_error_text.place(x=10, y=260, width=100, height=50)

# Ubicando botones
bottom.place(x=420, y=330, width=150, height=50)
bottom_help.place(x=10, y=330, width=150, height=50)

# Ejecutando aplicacion
app.mainloop()