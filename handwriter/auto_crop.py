import os
import pathlib
import argparse
from PIL import Image
import numpy as np

pad_up = [
    "g",
    "j",
    "p",
    "q",
    "y",
    "comma",
]
pad_double_up = [
    "underscore",
]
pad_down = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "i",
    "b",
    "d",
    "f",
    "h",
    "k",
    "l",
    "t",
    "dollar",
    "percent",
    "ampersand",
    "exclamation",
    "question_mark",
]
pad_double_down = [
    "caret",
    "double_quote",
    "single_quote",
]
pad_both = [
    "a",
    "c",
    "e",
    "m",
    "n",
    "o",
    "r",
    "s",
    "u",
    "v",
    "w",
    "x",
    "z",
    "at",
    "plus",
    "star",
    "colon",
    "equal",
    "minus",
    "period",
    "hashtag",
    "less_than",
    "semi_colon",
    "greater_than",
]


def auto_crop(set_dir):
    print("set_dir: ", set_dir)

    for root, dirs, files in os.walk(set_dir):
        for fname in files:
            fpath = os.path.join(root, fname)
            print("fpath: ", fpath)

            if not fpath.endswith(".png"):
                continue

            if fname == "space.png":
                continue

            original_img = Image.open(fpath)
            original_img_data = np.asarray(original_img)

            img = Image.open(fpath).convert("L")
            img_data = np.asarray(img)

            row_zeros = ~img_data.any(axis=1)
            col_zeros = ~img_data.any(axis=0)

            row_range = [0, len(row_zeros)]
            row_start = 0
            while row_start < len(row_zeros) and row_zeros[row_start]:
                row_start += 1

            row_range[0] = max(0, row_start - 1)

            row_start = len(row_zeros) - 1
            while row_start > 0 and row_zeros[row_start]:
                row_start -= 1

            row_range[1] = min(row_start + 1, len(row_zeros) - 1)

            col_range = [0, len(col_zeros)]
            col_start = 0
            while col_start < len(col_zeros) and col_zeros[col_start]:
                col_start += 1

            col_range[0] = max(0, col_start - 1)

            col_start = len(col_zeros) - 1
            while col_start < len(col_zeros) and col_zeros[col_start]:
                col_start -= 1

            col_range[1] = min(col_start + 1, len(col_zeros) - 1)

            new_img_data = original_img_data[
                row_range[0] : row_range[1] + 1, col_range[0] : col_range[1] + 1, :
            ]

            padding = np.zeros(
                [100, new_img_data.shape[1], new_img_data.shape[2]], dtype=np.uint8
            )
            half_padding = np.zeros(
                [50, new_img_data.shape[1], new_img_data.shape[2]], dtype=np.uint8
            )

            fname_no_ext, ext = os.path.splitext(fname)

            print("before shape: ", new_img_data.shape)

            if fname_no_ext in pad_both:
                new_img_data = np.vstack((padding, new_img_data, padding))
            elif fname_no_ext in pad_up:
                new_img_data = np.vstack((padding, new_img_data))
            elif fname_no_ext in pad_down:
                new_img_data = np.vstack((new_img_data, padding))
            elif fname_no_ext in pad_double_up:
                new_img_data = np.vstack((half_padding, padding, new_img_data))
            elif fname_no_ext in pad_double_down:
                new_img_data = np.vstack((new_img_data, padding, half_padding))

            print("after shape: ", new_img_data.shape)

            new_img = Image.fromarray(new_img_data)
            new_img.save(fpath)

            print("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert text to a handwritten page")
    parser.add_argument(
        "--setdir",
        "-s",
        required=True,
        help="Directory path of the set to crop",
    )
    args = parser.parse_args()

    auto_crop(args.setdir)
