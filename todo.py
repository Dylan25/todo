# controller
import argparse

parser = argparse.ArgumentParser(description="Maintain a todo list.")
parser.add_argument("todo-item", metavar="I", type=str,
                    help="Item to add to todo list.")