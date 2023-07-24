
import os
import pathlib
import argparse

def scan_files(directory, verbose=False):
    total_files = 0
    total_size = 0
    problem_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        contents = f.read()
                    total_files += 1
                    total_size += pathlib.Path(file_path).stat().st_size
                except UnicodeDecodeError:
                    problem_files.append(file_path)
                    if verbose:
                        print(f"Error reading file: {file_path}")
    return total_files, total_size, problem_files

def main():
    parser = argparse.ArgumentParser(description="Scan files and report problems.")
    parser.add_argument('directory', type=str, help='Directory to scan')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    args = parser.parse_args()

    total_files, total_size, problem_files = scan_files(args.directory, args.verbose)

    print(f"Total files scanned: {total_files}")
    print(f"Total size of scanned files: {total_size} bytes")
    print(f"Problem files: {len(problem_files)}")

if __name__ == "__main__":
    main()
