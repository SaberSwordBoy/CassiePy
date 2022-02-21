import sys
import multiprocessing
import threading
from time import sleep
import os
import itertools
from pyfiglet import figlet_format


from rich.console import Console
from rich.table import Table
from rich import print
console = Console()

VERSION = "0.1 Development"

def load_module(module):
    module_path = "modules.%s" % module
    #module_path = module

    if module_path in sys.modules:
        return sys.modules[module_path]

    return __import__(module_path, fromlist=[module])


commands = {
    "help": ["show this message", "help <args>"],
    "about": ["about CassiePy", "about"],
    "version": ["CassiePy version", 'version'],
    "modules": ['use and run modules', 'modules <args>']
}

modules = {}

for r, d, f, in os.walk("./modules"):
    for file in f:
        if '__' in file:
            continue
        elif 'cpython' in file:
            continue
        else:
            module = load_module(file.replace(".py", ""))
            modules.update({file: [module.NAME, module.DESCRIPTION, module]})

def usage(*args):
    console.print("[green][INFO][/green] [magenta bold] == COMMANDS AND USAGE == [/magenta bold]")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Command", style="dim")
    table.add_column("About", justify="right")
    table.add_column("Usage", justify="right")

    try:
        if args[1] == "modules":
            print("Use a module.\nYou can specify to use a module here. Will ask you to pick an avaliable module."
                  "`modules`")
    except IndexError:
        for cmd in commands:
            table.add_row(cmd, commands[cmd][0], commands[cmd][1])

        console.print(table)

def about():
    console.print(figlet_format('CassiePy', font='basic'), style='blue')
    print("Fuck ya life. Bing Bong")

def version():
    console.print(figlet_format('CassiePy', font='basic'), style='blue')
    print(f"Version {VERSION}")

def module(*args):
    console.print("[green][INFO][/green] [magenta bold] == Module Selector == [/magenta bold]")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Index", style="dim")
    table.add_column("Name", justify="right")
    table.add_column("Description", justify="right")

    table_index = 0

    for module in modules:
        table.add_row(str(table_index), modules[module][0], modules[module][1])
        table_index += 1
    table.add_row("99", "Back to main menu")

    console.print(table)

    running = True
    while running:
        prompt = inputPrompt("moduleSelector@CassiePy")

        try:
            prompt = int(prompt)

            if prompt == 99:
                running = False
            elif prompt > table_index:
                print("Not an option dumbass.")

            dict_index = list(modules)
            name = dict_index[prompt]
            try:
                modules[name][2].run()
            except KeyboardInterrupt:
                return

        except ValueError:
            print(f"[red][ERROR][/red][red dim] '[underline]{prompt}[/underline]' is not a valid option[/red dim]")

def inputPrompt(text):
    print(f"[bold green][INPUT][/bold green] [yellow]{text}[/yellow][blue]~[/blue][green]$[/green]", end="")
    return input()

def process_input(text):
    processed_text = text.lower().split()
    if processed_text[0] == "help":
        usage(*processed_text)
    elif processed_text[0] == 'about':
        about()
    elif processed_text[0] == 'version':
        version()
    elif processed_text[0] == 'modules':
        module(processed_text)
    else:
        print(f"[red][ERROR][/red] [red dim]Command '[underline]{processed_text[0]}[/underline]' not found. [/red dim]")

def main_menu():
    try:
        accepting_input = True
        while accepting_input:
            prompt = inputPrompt('menu@CassiePy')
            process_input(prompt)

    except KeyboardInterrupt:
        print("\n[red bold]Are you sure you want to quit?[/red bold] (Y/n) ", end="")
        if "y" in input().lower():
            return
        else:
            main_menu()

if os.name == "nt":
    platform = 'windows'
else:
    clear_command = "clear"
    platform = 'superior'

startup_tasks = [
    "Warming up the engines...",
    "Infiltrating NASA...",
    "Stealing all your passwords...",
    "Gathering information..."
]
tasks = itertools.cycle(startup_tasks)

def main():
    with console.status("Loading...", spinner="point") as status:
        for i in range(len(startup_tasks)):
            console.log(next(tasks))
            sleep(1)

    print("[green][INFO][/green] [dim]Done loading... Starting up now![/dim]")
    sleep(0.2)
    if platform == 'windows':
        os.system('cls')
    else:
        os.system('clear')

    console.print(figlet_format('CassiePy', font='basic'), style='magenta')
    print('\n\n\n\n')
    main_menu()

if __name__ == '__main__':
    main()