import argparse
import logging
import os

# This script is minimal, it just writes out a file stored in the container itself to the output
# file. Obviously, in a real scenario, a data source would query an external remote system
# to retrieve the data from. It would then manage traversing that data and writing that out to
# to the file.

# All arguments that the script accepts are also described in the component yaml file later
parser = argparse.ArgumentParser(description='')
parser.add_argument('--output-path', type=str, help='Path to write the output data to')
args = parser.parse_args()

logging.info(f"Extracting data with {args.output_path}")

# Kubeflow apparently doesn't automatically create output directories
os.makedirs(os.path.dirname(args.output_path), exist_ok=True)

# And simply copy the contents of one file to the output file.
with open(args.output_path, 'w') as output_file:
    with open('simulated_data.csv', 'r') as input_file:
        output_file.write(input_file.read())

logging.info("Finished extracting data")
