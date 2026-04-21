# terra-jekyll tools v0.7.0

#!/usr/bin/env python3

import argparse
import subprocess
import sys
from pathlib import Path


def run_command(command, cwd):
    print(f"Running: {' '.join(command)}", flush=True)
    subprocess.run(command, cwd=cwd, check=True)


def main():
    parser = argparse.ArgumentParser(
        description="Update extracted data files and then run the Jekyll bundle command."
    )
    parser.add_argument(
        "--directory",
        default=".",
        help="Repository directory to process (default: current directory).",
    )
    parser.add_argument(
        "--skip-serve",
        action="store_true",
        help="Only refresh the extracted files and skip the bundle command.",
    )
    parser.add_argument(
        "bundle_args",
        nargs=argparse.REMAINDER,
        help="Optional arguments to pass to bundle after '--'.",
    )

    args = parser.parse_args()
    repo_dir = Path(args.directory).resolve()

    extract_commands = [
        ["python3", "extract_repo.py", "."],
        ["python3", "extract_links.py", "."],
        ["python3", "extract_lastmod.py", "."],
        ["python3", "extract_images.py", "."],
    ]

    for command in extract_commands:
        run_command(command, repo_dir)

    if args.skip_serve:
        print("Skipping bundle command.")
        return

    bundle_args = args.bundle_args or ["exec", "jekyll", "serve", "--trace"]
    if bundle_args and bundle_args[0] == "--":
        bundle_args = bundle_args[1:]

    run_command(["bundle", *bundle_args], repo_dir)


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as error:
        sys.exit(error.returncode)
