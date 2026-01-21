import tkinter as tk
import subprocess

def lapsCommand():
    command = "Get-LapsADPassword"
    identity = "-Identity"
    domain = "-Domain"
    nameOfDomain = "intercity.pl"
    textParam = "-AsPlainText"
    historyParam = "-IncludeHistory"
    #ipOrHost = input("Podaj adres IP lub nazwę hosta/domeny: ")

    resHost = subprocess.run(["powershell.exe", "-Command", command, identity, ipOrHost.get(), domain, nameOfDomain, textParam, historyParam], capture_output = True, text = True)

    outputHost = resHost.stdout

    print(outputHost)


root = tk.Tk()
root.title("LAPS")

tk.Label(root, text="Nazwa Komputera: ").grid(row=0)
ipOrHost = tk.Entry(root)
ipOrHost.grid(row=0, column=1)
tk.Button(root, text="Zatwierdź", width=25, command=lapsCommand).grid(row=1, column=1)
tk.mainloop()