import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Python Calculator")
        self.root.geometry("340x500")
        self.root.resizable(False, False)

        self.expression = ""

        # Display
        self.display = tk.Entry(
            root,
            font=("Arial", 24),
            bd=10,
            relief=tk.RIDGE,
            justify="right"
        )
        self.display.pack(fill="both", padx=10, pady=10, ipady=12)

        # Button Layout
        buttons = [
            ['C', '⌫', '/', '*'],
            ['7', '8', '9', '-'],
            ['4', '5', '6', '+'],
            ['1', '2', '3', '='],
            ['0', '.', '(', ')']
        ]

        frame = tk.Frame(root)
        frame.pack(expand=True, fill="both")

        for r, row in enumerate(buttons):
            for c, btn in enumerate(row):
                button = tk.Button(
                    frame,
                    text=btn,
                    font=("Arial", 18),
                    command=lambda b=btn: self.click(b)
                )
                button.grid(
                    row=r,
                    column=c,
                    sticky="nsew",
                    padx=2,
                    pady=2
                )

        for i in range(5):
            frame.rowconfigure(i, weight=1)

        for i in range(4):
            frame.columnconfigure(i, weight=1)

    def click(self, value):
        if value == "C":
            self.expression = ""
            self.update_display()

        elif value == "⌫":
            self.expression = self.expression[:-1]
            self.update_display()

        elif value == "=":
            try:
                result = str(eval(self.expression))
                self.expression = result
                self.update_display()
            except ZeroDivisionError:
                self.expression = ""
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Cannot divide by zero")
            except Exception:
                self.expression = ""
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")

        else:
            self.expression += value
            self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()