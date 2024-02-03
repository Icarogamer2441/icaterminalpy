import subprocess
from pytkinterui import Window
import os

def execute_terminal(command):
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        return f"Erro ao executar o comando: {e}"

def open_search():
    def searchh():
        sear = search_bar.get()
        if sear.lower() == "twitch":
            result.configure(text="https://www.twitch.tv/")
        elif sear.lower() == "youtube":
            result.configure(text="https://www.youtube.com")
        elif sear.lower() == "toretori":
            result.configure(text="https://www.twitch.tv/toretori")
        elif sear.lower() == "imensy":
            result.configure(text="https://www.twitch.tv/imensy_")

    search = Window(340, 230, "icaSearch")
    search.window.resizable(False, False)
    search_bar = search.new_entry(0, 0, 340, "black", placeholder="search here...")
    result = search.new_label("", 60, 0, 340, 50, "white", "black")
    submit = search.new_button("submit", 20, 0, 340, 35, "lightgreen", "white", command=lambda: searchh())

    search.window.mainloop()

def open_terminal():
    def submit(event=None):
        comm = command.get()
        if comm.startswith("print"):
            message = comm.split(" ")[1].strip("\"\'")
            result.configure(text=f"message: {message}")
        elif comm.startswith("app"):
            appname = comm.split(" ")[1].strip("\"\'")
            if appname.lower() == "icasearch":
                open_search()
            elif appname.lower() == "icaterminal":
                open_terminal()
            elif appname.lower() == "icacalc":
                open_calc()
            elif appname.lower() == "icanotepad":
                open_notepad()
        elif comm.startswith("ls"):
            result.configure(text=execute_terminal("dir" if os.name == "nt" else "ls"))
        elif comm.startswith("cd"):
            directory = comm.split(" ")[1].strip("\"\'")
            try:
                os.chdir(directory)
                result.configure(text=f"Current directory changed to: {os.getcwd()}")
            except Exception as e:
                result.configure(text=f"Error changing directory: {str(e)}")
        elif comm.startswith("pwd"):
            result.configure(text=os.getcwd())
        elif comm.startswith("run"):
            command_to_run = comm.split(" ", 1)[1]
            result.configure(text=execute_terminal(command_to_run))
        else:
            result.configure(text="Comando não reconhecido.")

    terminal = Window(530, 450, "icaterminal")
    terminal.window.configure(bg="black")
    terminal.window.resizable(False, False)

    command = terminal.new_entry(0, 0, 530, "green", placeholder="command...")
    command.configure(bg="black")
    result = terminal.new_label("no commands executed", 25, 0, 530, 100, "black", "lightgreen")

    terminal.window.bind("<Control-s>", submit)

    terminal.window.mainloop()

def open_calc():
    def calculate():
        expression = calc_entry.get()
        try:
            result.configure(text=f"Result: {eval(expression)}")
        except Exception as e:
            result.configure(text=f"Error: {str(e)}")

    calculator = Window(300, 200, "icacalc")
    calculator.window.resizable(False, False)

    calc_entry = calculator.new_entry(0, 0, 300, "lightblue", placeholder="enter expression...")
    result = calculator.new_label("result will be displayed here", 40, 0, 300, 50, "white", "black")
    calc_submit = calculator.new_button("calculate", 20, 0, 300, 30, "lightgreen", "black", command=lambda: calculate())

    calculator.window.mainloop()

def open_notepad():
    def save_file():
        filename = filename_entry.get()
        content = notepad_text.get("1.0", "end-1c")
        filepath = os.path.join("icaterhome", filename)

        try:
            with open(filepath, "w") as file:
                file.write(content)
            result.configure(text=f"File '{filename}' saved successfully.")
        except Exception as e:
            result.configure(text=f"Error saving file: {str(e)}")

    notepad = Window(400, 350, "icanotepad")
    notepad.window.resizable(False, False)

    filename_label = notepad.new_label("File Name:", 10, 0, 400, 20, "white", "black")
    filename_entry = notepad.new_entry(30, 0, 400, "lightblue", placeholder="enter filename with extension...")

    notepad_text = notepad.new_text(110, 0, 400, 200, "lightyellow", "black")
    save_button = notepad.new_button("Save", 60, 0, 400, 50, "lightgreen", "black", command=lambda: save_file())
    result = notepad.new_label("", 10, 0, 400, 20, "white", "black")

    notepad.window.mainloop()
