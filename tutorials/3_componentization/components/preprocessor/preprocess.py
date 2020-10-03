import argparse
import logging
import os
import pandas as pd

# This script is a simple example of a preprocessing script for the purposes of demonstrating
# how components work and how they interact together.

parser = argparse.ArgumentParser(description='')
parser.add_argument('--input-path', type=str, help='Path to data to preprocess')
parser.add_argument('--output-path', type=str, help='Where to write the results to')
args = parser.parse_args()

logging.info("Preprocessing data")
logging.info(f"input path: {args.input_path}")
logging.info(f"output path: {args.output_path}")

# Kubeflow apparently doesn't automatically create output directories
os.makedirs(os.path.dirname(args.output_path), exist_ok=True)

logging.info("Starting to preprocess")

df = pd.read_csv(args.input_path)
df = pd.get_dummies(df, columns=['feature_1'])
df = df.fillna(0)
df['feature_4'] = df['feature_4'].astype(int)
df.to_csv(args.output_path, index=False)

logging.info("Preprocessing finished")
