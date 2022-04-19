# Entry point for application

from xmlrpc.client import ResponseError
from rich.console import Console

if __name__ == "__main__": 
    console = Console()
    console.print("[yellow]potatos [blue]are[/] poggers")

    room_descriptions = [ 
        "wrrrrrrrrrrrrry",
        "The room you enter is barbie [green]pink[/] room with a mountain of stuffed animals.", 
        "The room you enter is [black]black[/] and Gothic with what can only be described as an \"edgy\" teenager energy throughout. "
    ]
    current_room = 2
    done = False
    while not done:
        console.print(room_descriptions[current_room])
        user_input = input("Left or Right? ")
        user_input = user_input.lower().strip()
        if user_input == "left" or user_input == "l":
            current_room = 1
        elif user_input == "right" or user_input == "r":
            current_room = 0 
        else:
            console.print("[red]Invalid Response!")