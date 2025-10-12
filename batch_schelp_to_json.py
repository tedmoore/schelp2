from schelp_to_json import parse_file
import argparse
import os
from schelp_to_json import BLOCK_TAGS, BLOCK_PARSERS

def main(input_dir, output_dir):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Walk through the directory tree recursively
    parsed_files = 0
    for root, dirs, files in os.walk(input_dir):
        # Calculate the relative path from input_dir
        rel_path = os.path.relpath(root, input_dir)
        
        # Create corresponding output directory
        if rel_path == '.':
            current_output_dir = output_dir
        else:
            current_output_dir = os.path.join(output_dir, rel_path)
        
        if not os.path.exists(current_output_dir):
            os.makedirs(current_output_dir)
        
        # Process all .schelp files in current directory
        for filename in files:
            if filename.endswith('.schelp'):
                input_file = os.path.join(root, filename)
                output_file = os.path.join(current_output_dir, filename.replace('.schelp', '.json'))
                print(f"{parsed_files+1} Parsing {input_file} to {output_file}")
                parse_file(input_file, output_file)
                parsed_files += 1

    print(f"Parsed {parsed_files} files")
                
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Batch parse .schelp files to .json format')
    parser.add_argument('-i', '--input_dir', help='Directory containing .schelp files')
    parser.add_argument('-o', '--output_dir', help='Directory to save .json files')

    args = parser.parse_args()
    
    input_dir = args.input_dir
    output_dir = args.output_dir
    
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")
    
    missing_parsers = set(BLOCK_TAGS) - set(BLOCK_PARSERS.keys())
    if missing_parsers:
        print(f"Warning: Missing parsers for block tags: {missing_parsers}")
        exit()

    main(input_dir, output_dir)