import os
import re

FILE_NAME = "sample.md"

def main():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            f.write("This is Automated Commit #1\n")
        print("Created sample.md with Commit #1")
        return

    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    pattern = r"This is Automated Commit #(\d+)"
    current_number = None

    for i, line in enumerate(lines):
        match = re.search(pattern, line)
        if match:
            current_number = int(match.group(1))
            lines[i] = f"This is Automated Commit #{current_number + 1}\n"
            break

    if current_number is None:
        # No existing line found → create from scratch
        lines = ["This is Automated Commit #1\n"]
        print("No existing commit line found. Created #1")
    else:
        print(f"Incremented from #{current_number} to #{current_number + 1}")

    with open(FILE_NAME, "w") as f:
        f.writelines(lines)

if __name__ == "__main__":
    main()
