# to use please create an folder named icaterhome and execute this file
from functions import *
from pytkinterui import Window

UI = Window(760,509,"icaterminal OS")
UI.window.configure(bg="cyan")

main_menu = UI.new_menu()

apps_menu = UI.new_submenu(main_menu, "IcaOS")
UI.new_submenu_button(apps_menu, "search", command=lambda: open_search())
UI.new_submenu_button(apps_menu, "icaterminal", command=lambda: open_terminal())
UI.new_submenu_button(apps_menu, "icacalc", command=lambda: open_calc())
UI.new_submenu_button(apps_menu, "icanotepad", command=lambda: open_notepad())

terminalApp = UI.new_button("termi", 10, 5, 55,55, "black", "white", command=lambda: open_terminal())
searchApp = UI.new_button("search", 70,5,55,55,"yellow", "black", command=lambda: open_search())

UI.window.mainloop()
