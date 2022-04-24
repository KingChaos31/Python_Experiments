# Entry point for application


from rich.console import Console
from rich.prompt import Prompt

if __name__ == "__main__": 
    console = Console()
    console.print("[yellow]potatos [blue]are[/] poggers")

    room_data = [ 
        {
            "description": "Before your eyes you see a normal living room. Which is strange since you're supposed to be in a cave.",
            "title": "the first room"
        },
        {
            "description": "\"Wrrrrrrrrrry\" is the sound you hear when entering the room. Then you observe that the room is covered in Jojo's Bizarre Adventure merchandise. Plushies, posters, manga , and a Dio action figure that made the sound you heard when you first entered.",
            "title": "the second room"
        },
        {
            "description": "The room you enter is barbie [magenta]pink[/] room with a mountain of stuffed animals.",
            "title": "the third room"
        },
        {
            "description": "The room you enter is [black]black[/] and Gothic with what can only be described as an \"edgy\" teenager energy throughout. ",
            "title": "the fourth room"
        },
        {
            "description": "You enter and see a sign that says Uche accept the cringe, the based, and the bringe. Then you see a smaller sign underneath that says 'Never. Also Mary there is no exit and this cave is your punishment for putting me through this. From your reluctant mentor Uche. ",
            "title": "the last room"
        }
    ]
    current_room = 0
    done = False
    while not done:
        console.rule(room_data[current_room]["title"])
        console.print(room_data[current_room]["description"])
        user_input = console.input("[#00FFFF]Left[/] or Right? ")
        user_input = user_input.lower().strip()
        if user_input == "left" or user_input == "l":
            current_room = current_room - 1
            if current_room < 0:
                # You went out of the bounds on the left side.
                console.print("[red]Reached the near end of the cave!")
                current_room = current_room + 1
        elif user_input == "right" or user_input == "r":
            current_room = current_room + 1
            if current_room >= len(room_data):
                # You went out of bounds on the right side.
                console.print("[red]Reached the far end of the cave!")
                current_room = current_room - 1
        elif user_input == "quit" or user_input == "q":
            done = True
        else:
            console.print("[red]Invalid Response!")
