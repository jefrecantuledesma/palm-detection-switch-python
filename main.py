#!/usr/bin/env python
import os
import subprocess

def find_dwt() -> tuple: 
    config_path = os.path.expanduser("~/.config/sway/config")
    with open(config_path, "r") as f:
        data = f.readlines()
        counter = 0
        for line in data:
            counter +=1
            if "dwt" in line:
                truth = line.strip().split(" ")[1]
                line_number = counter
                return line_number, truth, config_path
    return ()

def replace_line(new_value: str, line_number: int, config_path: str) -> None:
    with open(config_path, "r") as f:
        lines = f.readlines()

    lines[line_number - 1] = f"dwt {new_value}\n"

    with open(config_path, "w") as f:
        f.writelines(lines)

    print("Palm-detection is now:", new_value.upper())

def main() -> None:
    line_number, truth, config_path = find_dwt()
    if truth == "disabled":
        replace_line("enabled", int(line_number), config_path)
    elif truth == "enabled":
        replace_line("disabled", int(line_number), config_path)
    
    subprocess.run(["swaymsg", "reload"])

main()
