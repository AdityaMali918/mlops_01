import argparse
import json
parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True,help="Feature list as JSON string. Example: \"[5.1,3.5,1.4,0.2]\"")
args = parser.parse_args()
print(args)
features = json.loads(args.input)
print(features)
''' python exp.py --input "[5.1, 3.5, 1.4, 0.2]" '''