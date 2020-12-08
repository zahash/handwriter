import os
import argparse
import pdfkit
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
    default="page.pdf",
    help="path to output pdf file (defaults to ./page.pdf)",
)
parser.add_argument(
    "--setname", "-s", default="set0", help="Name of character set to use",
)


args = parser.parse_args()

fpath_no_ext, _ = os.path.splitext(args.outfile)
htmlfpath = fpath_no_ext + ".html"

write_html(args.infile, htmlfpath, args.setname)
pdfkit.from_file(htmlfpath, args.outfile)

os.remove(htmlfpath)
