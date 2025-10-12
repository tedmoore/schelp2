import argparse
import batch_schelp_to_json
import batch_json_to_markdown

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        help='Input directory of .schelp files'
    )
    parser.add_argument(
        '-j',
        help='directory for storing JSON files'
    )
    parser.add_argument(
        '-o',
        help='Output directory of md files'
    )
    args = parser.parse_args()
    batch_schelp_to_json.main(args.i, args.j)
    batch_json_to_markdown.main(args.j, args.o)