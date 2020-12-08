import argparse
from .writer import write_html

parser = argparse.ArgumentParser(description="Convert text to a handwritten page")
parser.add_argument(
    "--infile",
    "-i",
    required=True,
    help="path to input text file (defaults to ./content.txt)",
)
parser.add_argument(
    "--outfile",
    "-o",
    default="page.html",
    help="path to output html file (defaults to ./page.html)",
)
parser.add_argument(
    "--setname", "-s", default="set0", help="Name of character set to use",
)


args = parser.parse_args()

write_html(args.infile, args.outfile, args.setname)
