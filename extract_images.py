# terra-jekyll tools v0.7.0

import argparse
import json
import os
import re
from urllib.parse import unquote

FRONT_MATTER_PATTERN = re.compile(r'^---\s*\n(.*?)\n---\s*\n?', re.DOTALL)
MARKDOWN_IMAGE_PATTERN = re.compile(r'!\[(.*?)\]\((.*?)\)')


def normalize_path(path):
    return os.path.normpath(unquote(path)).replace("\\", "/")


def extract_front_matter_images(content):
    match = FRONT_MATTER_PATTERN.match(content)
    if not match:
        return []

    lines = match.group(1).splitlines()
    images = []
    collecting_images = False

    for raw_line in lines:
        line = raw_line.rstrip()
        stripped = line.strip()

        if collecting_images:
            if stripped.startswith("- "):
                image_path = stripped[2:].strip()
                if image_path:
                    images.append(image_path)
                continue

            if line.startswith(" ") or line.startswith("\t") or stripped == "":
                continue

            collecting_images = False

        if stripped.startswith("image:"):
            image_path = stripped.split(":", 1)[1].strip()
            if image_path:
                images.append(image_path)
        elif stripped.startswith("images:"):
            collecting_images = True
            inline_value = stripped.split(":", 1)[1].strip()

            if inline_value.startswith("[") and inline_value.endswith("]"):
                inline_items = [item.strip() for item in inline_value[1:-1].split(",")]
                images.extend([item for item in inline_items if item])
                collecting_images = False
            elif inline_value:
                images.append(inline_value)
                collecting_images = False

    return images


def collect_gallery_images(directory, gallery_dir):
    gallery_images = {}
    gallery_root = os.path.join(directory, gallery_dir)

    for root, _, files in os.walk(gallery_root):
        for file_name in sorted(files):
            if file_name.startswith("."):
                continue

            image_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(image_path, directory)
            normalized_path = normalize_path(relative_path)
            gallery_images[normalized_path] = []

    return gallery_images


def find_markdown_image_references(directory, gallery_dir):
    gallery_images = collect_gallery_images(directory, gallery_dir)
    markdown_files = []

    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".md"):
                markdown_files.append(os.path.join(root, file_name))

    for file_path in markdown_files:
        cleaned_file_path = os.path.relpath(file_path, directory).replace("\\", "/")

        with open(file_path, "r", encoding="utf-8") as file_handle:
            content = file_handle.read()

        image_targets = []
        image_targets.extend(extract_front_matter_images(content))
        image_targets.extend(url for _, url in MARKDOWN_IMAGE_PATTERN.findall(content))

        for target in image_targets:
            if any(unwanted in target for unwanted in ["{{", "}}", "+", "\""]):
                continue
            if target.startswith(("http://", "https://")):
                continue

            resolved_path = os.path.normpath(os.path.join(os.path.dirname(cleaned_file_path), target))
            normalized_target = normalize_path(resolved_path)

            if normalized_target in gallery_images and cleaned_file_path not in gallery_images[normalized_target]:
                gallery_images[normalized_target].append(cleaned_file_path)

    return gallery_images


def save_images_to_json(images, output_file):
    ordered_images = dict(
        sorted(images.items(), key=lambda item: (len(item[1]) == 0, item[0]))
    )

    with open(output_file, "w", encoding="utf-8") as file_handle:
        json.dump({"file": ordered_images}, file_handle, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Map gallery images to markdown files that reference them.")
    parser.add_argument("directory", help="The path to the folder containing markdown files and imgs/gallery.")
    parser.add_argument("--gallery-dir", default="imgs/gallery", help="Gallery directory relative to the target directory.")
    parser.add_argument("--output", default="_data/gallery_links.json", help="The output JSON file name (default: _data/gallery_links.json)")

    args = parser.parse_args()

    images = find_markdown_image_references(args.directory, args.gallery_dir)
    save_images_to_json(images, args.output)

    print(f"Gallery image links have been saved to {args.output}")
