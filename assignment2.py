#!/usr/bin/env python3

'''
OPS445 Assignment 2
Program: assignment2.py 
Author: "Rahul Shah"
Studen id: 125503227
'''

import argparse
import os, sys

def parse_command_args() -> object:
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts", epilog="Copyright 2023")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    parser.add_argument("-H", "--human-readable", action="store_true", help="Prints sizes in human readable format")
    parser.add_argument("program", type=str, nargs='?', help="if a program is specified, show memory use of all associated processes. Show only total use if not.")
    args = parser.parse_args()
    return args
# create argparse function
# -H human readable
# -r running only

def percent_to_graph(percent: float, length: int=20) -> str:
    "turns a percent 0.0 - 1.0 into a bar graph"
    
    if percent < 0.0 or percent > 1.0:
        raise ValueError("Percent must be between 0.0 and 1.0")

    # Apply the scaling formula
    num_hashes = int((percent - 0.0) / (1.0 - 0.0) * (length - 0) + 0)
    
    # Calculate the number of spaces
    num_spaces = length - num_hashes
    
    # Construct the bar graph string
    bar_graph = '#' * num_hashes + ' ' * num_spaces
    
    return bar_graph

# percent to graph function

def get_sys_mem() -> int:
    "return total system memory (used or available) in kB"
    with open("/proc/meminfo", "r") as file:
        for line in file:
            if line.startswith("MemTotal:"):
                # Extract the number part and convert to an integer
                total_memory_kb = int(line.split()[1])
                return total_memory_kb
    raise RuntimeError("MemTotal not found in /proc/meminfo")

def get_avail_mem() -> int:
    "return total memory that is currently in use"
    with open("/proc/meminfo", "r") as file:
        for line in file:
            if line.startswith("MemAvailable:"):
                # Extract the number part and convert to an integer
                available_memory_kb = int(line.split()[1])
                return available_memory_kb
    raise RuntimeError("MemAvailable not found in /proc/meminfo")

def pids_of_prog(app_name: str) -> list:
    "given an app name, return all pids associated with app"
    pids = []
    try:
        output = os.popen(f'pidof {app_name}').read().strip()
        if output:
            pids = output.split()
    except Exception as e:
        pass
    return pids

def rss_mem_of_pid(proc_id: str) -> int:
    "given a process id, return the resident memory used, zero if not found"
    try:
        with open(f"/proc/{proc_id}/status", "r") as file:
            for line in file:
                if line.startswith("VmRSS:"):
                    return int(line.split()[1])  # memory in kB
    except Exception as e:
        pass
    return 0

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    "turn 1,024 into 1 MiB, for example"
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']  # iB indicates 1024
    suf_count = 0
    result = kibibytes 
    while result > 1024 and suf_count < len(suffixes):
        result /= 1024
        suf_count += 1
    str_result = f'{result:.{decimal_places}f} '
    str_result += suffixes[suf_count]
    return str_result

if __name__ == "__main__":
    args = parse_command_args()
    if not args.program:
        ...
    else:
        ...
    