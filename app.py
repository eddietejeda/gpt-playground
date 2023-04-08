import os
import importlib
import argparse
from examples import simple, summerize

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def main():
    # return
    parser = argparse.ArgumentParser(description='Run a specified module and function.')
    parser.add_argument('module', metavar='M', type=str, help='the name of the module to run')
    args = parser.parse_args()

    # Import the specified module
    try:
        # module = importlib.import_module(args.module)
        module = importlib.import_module("examples." + args.module)
    except ModuleNotFoundError:
        print(f"Module '{args.module}' not found.")
        return

    # Run the 'run' function in the specified module
    try:
        module.run()
    except AttributeError:
        print(f"Module '{args.module}' does not have a 'run' function.")
        return

if __name__ == '__main__':
    main()
