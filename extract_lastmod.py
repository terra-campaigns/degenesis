import os
import json
import argparse
from datetime import datetime

def get_last_modified_dates(directory):
    file_mod_times = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, directory).replace("\\", "/")
                last_modified = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-W%U')
                file_mod_times[rel_path] = last_modified
    # Sort by last_modified (YYYY-weeknumber) descending
    sorted_data = dict(sorted(file_mod_times.items(), key=lambda x: x[1], reverse=True))
    return sorted_data

def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get last modified dates of markdown files.")
    parser.add_argument("directory", help="Path to the markdown files root directory.")
    parser.add_argument("--output", default="_data/lastmod.json", help="Path to output JSON file.")

    args = parser.parse_args()
    data = get_last_modified_dates(args.directory)
    save_to_json(data, args.output)
    print(f"Last modified dates have been saved to {args.output}")
