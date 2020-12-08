import os
import pathlib
import random
import string
from .utils import CHAR_MAP

trcolor = False
letter_color = "blue"
letter_type = ""
letter_set = "set0"
html_page = [
    """
    <html>
        <head>
            <style>
                .lines{width:100%;
                    height:auto;
                    float:left;}

                #paper{background:white;
                    height:auto;float:left;
                    padding:50px 50px;
                    width:90%;}

                img,span{height:25px;
                        width:10px;
                        float:left;
                        margin-top:5px;
                        margin-bottom:10px;}

                .clblack{filter:brightness(30%);}
                .clblue{filter:brightness(100%);}

            </style>
        </head>
        <body>
            <div id='paper'>
    """
]

"""
<html>
    <head>
        <style>
            .lines{width:100%;
                   height:auto;
                   float:left;}

            #paper{background:white;
                   height:auto;float:left;
                   padding:50px 50px;
                   width:90%;}

            img,span{height:25px;
                     width:10px;
                     float:left;
                     margin-top:5px;
                     margin-bottom:10px;}

        </style>
    </head>
    <body>
        <div id='paper'>
"""


def write_html(input_filepath, output_filepath, set_name):
    chars_dir = pathlib.Path(__file__).parent.parent.absolute() / "chars"
    set_dir = chars_dir / set_name

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits

    if not input_filepath.endswith(".txt"):
        raise ValueError("input filename must end with .txt")
    if not output_filepath.endswith(".html"):
        raise ValueError("output filename must end with .html")

    content = []
    with open(input_filepath, "r") as input_file:
        for line in input_file:
            line = line.rstrip()
            content.append(line)

    for line in content:
        html_page.append('<div class="lines">')
        for char in line:
            if char not in uppercase + lowercase + digits:
                char = CHAR_MAP[char]

            random_char_image_fname = random.choice(
                os.listdir(set_dir / char) or os.listdir(set_dir / "space")
            )

            html_page.append(
                "<img src='{}/{}/{}'/>".format(set_dir, char, random_char_image_fname)
            )

        html_page.append("</div>")
    html_page.append("</div></body></html>")

    with open(output_filepath, "w") as page_html:
        page_html.writelines(html_page)


# with open(args.inputfile, "r") as textfile:
#     for line in textfile:

#         # Strips the newline character
#         curst = line.strip()
#         htmlc.append('<div class="lines">')
#         for ch in curst:
#             # get char ASCII Code of char
#             chcode = ord(ch)

#             if chcode >= 65 and chcode <= 90:
#                 letter_type = "caps"
#                 ch = ch.lower()
#             elif chcode >= 97 and chcode <= 177:
#                 letter_type = "small"
#             elif chcode >= 48 and chcode <= 57:
#                 letter_type = "others"
#                 ch = "{}".format(chcode)
#             elif chcode == 32 or chcode == 36:
#                 htmlc.append("<span></span>")
#             else:
#                 letter_type = "others"
#                 ch = "{}".format(chcode)

#             if chcode != 35 and chcode != 32 and chcode != 36:
#                 htmlc.append(
#                     "<img src='images/letters/{}/{}/{}/{}.png'/>".format(
#                         letter_set, letter_color, letter_type, ch
#                     )
#                 )
#         htmlc.append("</div>")

# htmlc.append("</div></body></html>")

# with open(args.outputfile, "w") as page_html:
#     page_html.writelines(htmlc)
