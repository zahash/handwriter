import pathlib
import string

CHAR_MAP = {
    ".": "period",
    ",": "comma",
    ";": "semi_colon",
    ":": "colon",
    '"': "double_quote",
    "'": "single_quote",
    " ": "space",
    "!": "exclamation",
    "?": "question_mark",
    "@": "at",
    "#": "hashtag",
    "$": "dollar",
    "%": "percent",
    "&": "ampersand",
    "+": "plus",
    "-": "minus",
    "=": "equal",
    "/": "forward_slash",
    "*": "star",
    "(": "left_small_bracket",
    ")": "right_small_bracket",
    "{": "left_flower_bracket",
    "}": "right_flower_bracket",
    "[": "left_big_bracket",
    "]": "right_big_bracket",
}


def make_set_dir(base_img_dir, set_name, custom_chars=[]):
    """
    Make the directory structure for a character set in 
    <base_img_dir>/<set_name>

    Args:
        base_img_dir: base dir where each set will be stored
        set_name: (directory) name of the character set to generate
        custom_chars: any list of custom characters that needs to be included
            Eg: ["euro", "greater_than", "back_slash"]
    
    Returns: None
    """
    base_img_dir = pathlib.Path(base_img_dir)
    set_dir = base_img_dir / set_name

    if set_dir.is_dir():
        print(
            "Directory with the name {} already exists in {}".format(
                set_name, base_img_dir
            )
        )

    chars = (
        list(string.ascii_uppercase)
        + list(string.ascii_lowercase)
        + list(string.digits)
        + list(CHAR_MAP.values())
        + custom_chars
    )

    for ch in chars:
        (set_dir / ch).mkdir(parents=True, exist_ok=True)
