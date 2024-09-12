## Overview

This program processes flow logs and tags each entry based on a lookup table of port and protocol combinations. The idea is to read flow log data, find the matching tag from the lookup table, and generate an output file with:
1. The count of how many times each tag was applied.
2. The count of unique port/protocol combinations found in the logs.

This program can handle large files (up to 10MB for flow logs) and lookup tables with as many as 10,000 mappings. It's designed to work efficiently with large datasets.

## Assumptions

Here are the main assumptions I made while building this:
- The program only supports the default AWS VPC flow log format, specifically **version 2** logs.
- A tag can apply to multiple `dstport` and `protocol` combinations. This means a tag like `sv_P1` can apply to both `25/tcp` and `443/tcp`, for example.
- The input files (flow logs and lookup table) should be in plain text format (ASCII).
- The protocol matching is case-insensitive, and the program uses Python's built-in functions for file handling and CSV parsing.

## How to Run the Program

### Prerequisites
- You'll need Python 3.x installed on your machine.

### Steps to Run:
1. Download or clone the repository to your local machine.
2. Make sure the input files (`lookup_table.csv` and `flow_logs.txt`) are in the same directory as the Python script (`main.py`).
3. Open a terminal, navigate to the root folder where the files are located.
4. Run the script using the following command:
   ```bash
   python main.py
5. The program will process the logs and generate an output file named `output_counts.csv`.

## Output
The program creates a single CSV file (output_counts.csv) with two sections:

1. Tag Counts: This shows how many times each tag was applied.
2. Port/Protocol Combination Counts: This shows how often each unique combination of port and protocol appeared in the flow logs.

## How I Tested It
Test Files:

1. Small Test: I started with a small lookup table and flow log file to make sure everything was working as expected.
2. Large Test: Next, I tested the program with a larger dataset. The program handled both large files without performance issues.

The program processess large flow logs by reading the logs line by line, rather than loading the entire file into memory. This ensures it can handle logs up to 10MB.

## Reference
- Amazon Web Services. AWS Documentation. [https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html)

If you have any questions or run into any issues, feel free to reach out!
