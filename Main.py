import datetime
import os
import sys
import importlib.util

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def string_to_module(module_name):
    module = None
    for dirpath, dirnames, filenames in os.walk("Problems"):
        if module_name in filenames:
            try:
                path = ROOT_DIR + "\\" + dirpath + "\\" + module_name

                spec = importlib.util.spec_from_file_location("", path)
                foo = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(foo)
                module = foo
            except ModuleNotFoundError:
                print("file " + module_name + " is unfinished or has not been attempted (yet!)")
                return None

    result = getattr(module, "method")
    return result


if __name__ == "__main__":
    print("hello! this program runs any Project Euler problem I've completed.")

    while True:
        inp = input("enter a problem number, or any value that's not a number to exit:\n")
        try:
            val = int(inp)
        except ValueError:
            exit(0)
        # get problem number {inp}'s method
        module_name = "Problem" + inp + ".py"
        method = string_to_module(module_name)
        if method is None:
            print("\n\n")
            continue
        start = datetime.datetime.now()
        method()
        end = datetime.datetime.now()
        delta = end - start
        print(delta)
        print("\n\nWould you like to run another problem?")