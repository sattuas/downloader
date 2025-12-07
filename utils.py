# from rich import print


def set_color(text, color=None):
    return f'[bold {color}]{text}[/bold {color}]'


if __name__ == "__main__":
    print(f"{set_color('testing', 'red')} {set_color('differents', 'blue')} {set_color('colors', 'yellow')}")