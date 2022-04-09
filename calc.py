import tkinter

window = tkinter.Tk()
window.title("Калькулятор")
window.geometry("500x550")
window.resizable(width=False, height=False)
window.configure(bg='white')


### вычисление операций
def calc(operation):
    global formula

    if operation == 'C':
        formula = ''
    elif operation == "del":
        formula = formula[0:-1]
    elif operation == "x^2":
        formula = str((eval(formula)) ** 2)
    elif operation == "=":
        formula = str(eval(formula))
    elif operation == "+/-":
        formula = str(eval(formula) * (-1))
    else:
        if formula == "0":
            formula = ''
        formula += operation
    label_text.configure(text=formula)


### создание окна

formula = "0"
label_text = tkinter.Label(text=formula, font=('Roboto', 30, 'bold'), bg="white", fg="black")
label_text.place(x=11, y=50)

### создаём кнопки

buttons = [
    'C', 'del', "*", "=", "1", "2", "3", "4", "/", "5", "6", "+", "7", "8", "9", "-", "+/-", "0", "%", "x^2"
]

x = 18
y = 140

for button in buttons:
    get_label = lambda x=button: calc(x)
    tkinter.Button(text=button, bg='gray', font=('Roboto', 20), command=get_label).place(x=x, y=y, width=115, height=79)
    x += 117
    if x > 400:
        x = 18
        y += 81

window.mainloop()
