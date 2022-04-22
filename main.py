# Entry point for application


from rich.console import Console

if __name__ == "__main__": 
    console = Console()
    console.print("[yellow]potatos [blue]are[/] poggers")

    room_descriptions = [ 
        "the first room",
        "wrrrrrrrrrrrrry",
        "The room you enter is barbie [green]pink[/] room with a mountain of stuffed animals.", 
        "The room you enter is [black]black[/] and Gothic with what can only be described as an \"edgy\" teenager energy throughout. ",
        "the last room"
    ]
    current_room = 0
    done = False
    while not done:
        console.print(room_descriptions[current_room])
        user_input = input("Left or Right? ")
        user_input = user_input.lower().strip()
        if user_input == "left" or user_input == "l":
            current_room = current_room - 1
            if current_room < 0:
                # You went out of the bounds on the left side.
                console.print("[red]Reached the near end of the cave!")
                current_room = current_room + 1
        elif user_input == "right" or user_input == "r":
            current_room = current_room + 1
            if current_room >= len(room_descriptions):
                # You went out of bounds on the right side.
                console.print("[red]Reached the far end of the cave!")
                current_room = current_room - 1
        elif user_input == "quit" or user_input == "q":
            done = True
        else:
            console.print("[red]Invalid Response!")
