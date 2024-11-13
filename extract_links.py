import os
import re
import json
import argparse
from collections import defaultdict

def find_markdown_links(directory):
    links = defaultdict(list)

    # Regular expression to match markdown links, excluding image links
    link_pattern = re.compile(r'(?<!\!)\[(.*?)\]\((.*?)\)')

    # Walk through all files and subfolders in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # Clean the file path by removing any leading './' or '/' characters
                cleaned_file_path = os.path.relpath(file_path, directory).lstrip('./')
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Find all markdown links in the file
                    file_links = link_pattern.findall(content)
                    for text, url in file_links:
                        # Skip links that contain Jekyll templating syntax
                        if "{{" in text or "}}" in text or "{{" in url or "}}" in url:
                            continue
                        
                        # Check if the URL is internal (relative path, not starting with http:// or https://)
                        is_internal = not url.startswith(('http://', 'https://'))
                        
                        # For internal links, make the path start from the directory root
                        if is_internal:
                            # Calculate the absolute path starting from the root of the directory
                            full_url = os.path.normpath(os.path.join('/', os.path.relpath(url, directory))).lstrip('./')
                        else:
                            full_url = url
                        
                        # Append outbound link data with the is_internal field, full URL, and direction as "outbound"
                        links[cleaned_file_path].append({
                            "text": text,
                            "url": full_url,
                            "is_internal": is_internal,
                            "direction": "outbound"
                        })

                        # If the link is internal, add this file as an inbound link in the target file's entry
                        if is_internal:
                            links[full_url].append({
                                "text": text,
                                "url": cleaned_file_path,  # Store inbound file path in the "url" field
                                "is_internal": True,
                                "direction": "inbound"
                            })

    # Convert the defaultdict to a regular dict for JSON serialization
    return dict(links)

def save_links_to_json(links, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({"file": links}, f, indent=4)

if __name__ == "__main__":
    # Setup command-line argument parsing
    parser = argparse.ArgumentParser(description="Extract markdown links from a folder.")
    parser.add_argument("directory", help="The path to the folder containing markdown files.")
    parser.add_argument("--output", default="_data/markdown_links.json", help="The output JSON file name (default: _data/markdown_links.json)")

    args = parser.parse_args()

    # Get directory and output file from arguments
    directory = args.directory
    output_file = args.output

    # Run the functions
    links = find_markdown_links(directory)
    save_links_to_json(links, output_file)

    print(f"Markdown links have been saved to {output_file}")

