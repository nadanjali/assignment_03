"""
process_file.py — Part 2: one file of package descriptions, uploaded.

A Streamlit app that accepts an uploaded text file with one package description
per line, shows the total for every line, and writes the parsed packages to a
JSON file in the `data/` folder — `data/packaging1.txt` in, `data/packaging1.json`
out.

New here: an uploaded file arrives as **bytes**, not text, so it has to be
decoded before it can be split into lines. And a text file usually ends with a
newline, so the last "line" is empty and must be skipped rather than parsed.

Run it:  Run and Debug -> "Streamlit Run: Current File"   (see README Reference #1)
Test it: pytest tests/test_streamlit.py -k process_file
"""

# --- The page ---------------------------------------------------------------------
#
# Less scaffolding this time. The steps are described, but which widget and which
# function does each job — and what to call the result — is now yours to work out.
# `one_package.py` is your worked example for anything structural, and README
# Reference #4 and #5 cover the two things that are new here.

# TODO: imports — streamlit, json, and what you need from packaging_parser.
import streamlit as st
import json
from packaging_parser import parse_packaging, calc_total_units, get_unit

# TODO: the title, exactly:   Process File of Packages
st.title("Process File of Packages")


# TODO: a file uploader, key="package_file". Like the text box in Part 1 it returns
#       a value — None until a file has been chosen — so the same kind of guard
#       goes around everything below.
uploaded_file = st.file_uploader(
    "Upload package file:",
    key="package_file"
)


# 1. Bytes to text. The upload is bytes; decode it, then split it into lines.
# TODO
if uploaded_file is not None:
    text = uploaded_file.getvalue().decode("utf-8")
    packages = []    
    for line in text.splitlines():                     
        line = line.strip()
        if not line:                                   
            continue


# 2. Every line: strip it, SKIP IT IF IT IS BLANK, parse it, keep the parsed package
#    in a list, and show the line with its total. Match this layout:
#
#        12 eggs in 1 carton / 3 cartons in 1 box ➡️ Total 📦 Size: 36 eggs
# TODO
        package = parse_packaging(line)
        total = calc_total_units(package)
        unit = get_unit(package)
        packages.append(package)

        st.info(f"{line} ➡️ Total 📦 Size: {total} {unit}")


# 3. Write the list of parsed packages to data/<name>.json with json.dump, where
#    <name> is the uploaded file's name with .txt replaced by .json.
# TODO
    output_name = uploaded_file.name.replace(".txt", ".json")

    with open(f"data/{output_name}", "w") as json_file:
        json.dump(packages, json_file, indent=4)


# 4. Say what happened, with st.success, exactly:
#
#        3 packages written to data/packaging1.json
# TODO

    st.success(f"{len(packages)} packages written to data/{output_name}")