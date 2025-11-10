import reader
import table
import friend
import book

import sys



def main() -> None:

        if len(sys.argv) != 2:
                print("Usage: main.py input.json")
                sys.exit()

        # TODO: implement .json file reading
        print("opening .json file")
        filename = "input.txt"
        reader.read_json(filename)

        

if __name__ == "__main__":
        main()