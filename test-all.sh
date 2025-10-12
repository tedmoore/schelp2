python batch_convert.py ../supercollider/HelpSource -o ./output --json --md
./build_docs.sh
cd docs/_build/html
python3 -m http.server 8000