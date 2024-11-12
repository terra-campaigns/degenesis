import os
import re
import json
import argparse

def find_markdown_links(directory):
    links = {}

    # Regular expression to match markdown links, excluding image links
    # Markdown link format: [link text](url)
    link_pattern = re.compile(r'(?<!\!)\[(.*?)\]\((.*?)\)')

    # Walk through all files and subfolders in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # Remove any leading './' or '.' from file path
                cleaned_file_path = os.path.relpath(file_path, directory).lstrip('./')
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Find all markdown links
                    file_links = link_pattern.findall(content)
                    valid_links = []
                    for text, url in file_links:
                        # Skip links that contain Jekyll templating syntax
                        if "{{" in text or "}}" in text or "{{" in url or "}}" in url:
                            continue
                        
                        # Check if the URL is internal (relative path, not starting with http:// or https://)
                        is_internal = not url.startswith(('http://', 'https://'))
                        
                        # For internal links, make the path start from the directory root
                        if is_internal:
                            # Calculate the absolute path starting from the root of the directory
                            full_url = os.path.normpath(os.path.join('/', os.path.relpath(url, directory)))
                        else:
                            full_url = url
                        
                        # Append link data with the is_internal field and full_url
                        valid_links.append({
                            "text": text,
                            "url": full_url.lstrip('./'),
                            "is_internal": is_internal
                        })

                    if valid_links:
                        # Add valid links to dictionary under the cleaned file path
                        links[cleaned_file_path] = valid_links

    return links

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

