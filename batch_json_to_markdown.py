from json_to_markdown import convert_to_markdown
import argparse
import os

def main(input_dir, output_dir):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Walk through the directory tree recursively
    converted_files = 0
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
        
        # Process all .json files in current directory
        for filename in files:
            if filename.endswith('.json'):
                input_file = os.path.join(root, filename)
                output_file = os.path.join(current_output_dir, filename.replace('.json', '.md'))
                print(f"{converted_files+1} Converting {input_file} to {output_file}")
                convert_to_markdown(input_file, output_file)
                converted_files += 1

    print(f"Converted {converted_files} files")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        help='Input directory of .json files'
    )
    parser.add_argument(
        '-o',
        help='Output directory'
    )
    args = parser.parse_args()
    main(args.i, args.o)
