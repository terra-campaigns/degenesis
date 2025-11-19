# consolidate_files.py

import os
import argparse
import re

def extract_and_consolidate(repo_path, target_folders):
    consolidated_text = []
    files_with_order = []
    for folder in target_folders:
        folder_path = os.path.join(repo_path, folder)
        if not os.path.exists(folder_path):
            continue

        for root, _, files in os.walk(folder_path):
            for file in files:
                if file == '.DS_Store':
                    continue
                if file == 'inklings.md':
                    continue
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            content = re.sub(r'{%.*?%}|{{.*?}}', '', content)
                            content = "\n".join(
                                line for line in content.splitlines()
                                if '{:' not in line and not line.lstrip().startswith('`=map')
                            )
                            content = re.sub(r'<[^>]+>', '', content)
                            nav_order_match = re.search(r'nav_order\s*[:=]\s*(\S+)', content)
                            nav_order_val = nav_order_match.group(1) if nav_order_match else None
                            nav_order = None
                            if nav_order_val:
                                if re.match(r'^\d{4}-\d{2}-\d{2}$', nav_order_val):
                                    nav_order = tuple(map(int, nav_order_val.split('-')))
                                elif nav_order_val.isdigit():
                                    nav_order = int(nav_order_val)
                            files_with_order.append((file_path, nav_order, content))
                    except Exception as e:
                        print(f"Could not read {file_path}: {e}")

    # Sort files by nav_order, placing those without nav_order last
    def sort_key(item):
        nav_order = item[1]
        if isinstance(nav_order, tuple):
            return (False, nav_order)
        elif isinstance(nav_order, int):
            return (False, (nav_order,))
        else:
            return (True, ())
    files_with_order.sort(key=sort_key)

    for file_path, _, content in files_with_order:
        header = f"\n\n# FILE: {os.path.relpath(file_path, repo_path)}\n\n"
        consolidated_text.append(header + content)

    return "\n".join(consolidated_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract and consolidate text files from specific folders.")
    parser.add_argument("repo_path", help="Path to the repository")
    args = parser.parse_args()

    repo_path = os.path.abspath(args.repo_path)
    repo_name = os.path.basename(repo_path.rstrip("/\\"))
    output_dir = os.path.dirname(repo_path)
    output_file = os.path.join(output_dir, f"{repo_name}.txt")

    target_folders = ['campaigns', 'directory', 'systems']
    result = extract_and_consolidate(repo_path, target_folders)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"Consolidated content saved to {output_file}")
