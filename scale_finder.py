import sys
import argparse

root_notes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
modes = ["ionian", "dorian", "phrygian", "lydian", "mixlolydian", "aeolian", "locrian"]
pattern = [2, 2, 1, 2, 2, 2, 1]


def find_scale(starting_note, starting_mode):
    notes = []
    current_note = root_notes.index(starting_note)
    current_mode = modes.index(starting_mode)

    notes.append(root_notes[current_note])
    for i in range(0, 7):
        current_note += pattern[(current_mode + i) % len(pattern)]
        notes.append(root_notes[current_note % len(root_notes)])

    return notes


def main():
    parser = argparse.ArgumentParser(description="Show musical scale based on root and mode")

    parser.add_argument("-r", "--root", type=str, required=True, help = "The root notes are c, c#, d, d#, e, f, f#, g, g#, a, a#, b ")
    parser.add_argument("-m", "--mode", type=str, required=True, help = "The modes are ionian, dorian, phrygian, lydian, mixlolydian, aeolian, locrian")

    args = parser.parse_args()

    root = args.root
    mode = args.mode

    scale = find_scale(root, mode)
    print(f"Scale for {root} {mode}: {scale}")

if __name__ == "__main__":
    main()
