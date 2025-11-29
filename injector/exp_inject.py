#!/usr/bin/env python3
"""POC injector: create minimal HWPX template (if missing), replace {{KEY}} placeholders in section*.xml, and write output .hwpx

Usage:
  python injector/exp_inject.py --template input/hwpx_templates/template.hwpx --data input/reference/sample_data.json --output output/injected.hwpx

If --template is missing, the script will generate a minimal template at the given path.
If --data is missing, the script will look for input/reference/sample_data.json or use embedded sample data.
"""
import argparse
import json
import os
import shutil
import sys
import tempfile
import zipfile
import glob
import re

WORKDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

SAMPLE_DATA = {
    "TITLE": "POC Title",
    "NAME": "Alice",
    "ITEMS": ["First item", "Second item", "Third item"],
}

MIMETYPE_CONTENT = b"application/vnd.haansoft.hwpx\n"

MINIMAL_HEADER_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<hp:header xmlns:hp="urn:hwpx">
  <hp:master>
    <hp:name>default</hp:name>
  </hp:master>
</hp:header>
'''

MINIMAL_SECTION_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<hp:section xmlns:hp="urn:hwpx">
  <hp:p>
    <hp:run><hp:t>{{TITLE}}</hp:t></hp:run>
  </hp:p>
  <hp:p>
    <hp:run><hp:t>By: {{NAME}}</hp:t></hp:run>
  </hp:p>
  <hp:p>
    <hp:run><hp:t>Items:</hp:t></hp:run>
  </hp:p>
  <hp:p>
    <hp:run><hp:t>{{ITEMS}}</hp:t></hp:run>
  </hp:p>
</hp:section>
'''


def create_minimal_hwpx(path):
    """Create a very small hwpx archive suitable for POC tests.
    The `mimetype` file is stored uncompressed as required by many ZIP-based formats.
    """
    tmpdir = tempfile.mkdtemp()
    try:
        # create folder structure
        os.makedirs(os.path.join(tmpdir, 'Contents'))
        # write files
        with open(os.path.join(tmpdir, 'mimetype'), 'wb') as f:
            f.write(MIMETYPE_CONTENT)
        with open(os.path.join(tmpdir, 'Contents', 'header.xml'), 'w', encoding='utf-8') as f:
            f.write(MINIMAL_HEADER_XML)
        with open(os.path.join(tmpdir, 'Contents', 'section0.xml'), 'w', encoding='utf-8') as f:
            f.write(MINIMAL_SECTION_XML)
        # write zip: mimetype must be stored (no compression) as first entry
        with zipfile.ZipFile(path, 'w') as z:
            z.writestr('mimetype', MIMETYPE_CONTENT, compress_type=zipfile.ZIP_STORED)
            for root, dirs, files in os.walk(os.path.join(tmpdir, 'Contents')):
                for fn in files:
                    full = os.path.join(root, fn)
                    arcname = os.path.relpath(full, tmpdir)
                    z.write(full, arcname)
    finally:
        shutil.rmtree(tmpdir)


def unzip_to_dir(hwpx_path, dest_dir):
    with zipfile.ZipFile(hwpx_path, 'r') as z:
        z.extractall(dest_dir)


def rezip_dir(src_dir, out_path):
    # Ensure mimetype is first and stored
    mimetype_path = os.path.join(src_dir, 'mimetype')
    with zipfile.ZipFile(out_path, 'w') as z:
        if os.path.exists(mimetype_path):
            with open(mimetype_path, 'rb') as f:
                z.writestr('mimetype', f.read(), compress_type=zipfile.ZIP_STORED)
        # add the rest
        for root, dirs, files in os.walk(src_dir):
            for fn in files:
                full = os.path.join(root, fn)
                arcname = os.path.relpath(full, src_dir)
                if arcname == 'mimetype':
                    continue
                z.write(full, arcname)


def load_data(data_path):
    if data_path and os.path.exists(data_path):
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    # fall back to sample
    return SAMPLE_DATA


def replace_placeholders_in_file(path, data):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # find placeholders like {{KEY}}
    pattern = re.compile(r"\{\{\s*([A-Z0-9_]+)\s*\}\}")

    def repl(match):
        key = match.group(1)
        if key not in data:
            return match.group(0)
        val = data[key]
        if isinstance(val, list):
            # join list elements as separate paragraphs/runs
            # produce multiple runs within the same file: keep hp XML structure
            # We'll return concatenated runs separated by '</hp:t></hp:run></hp:p><hp:p><hp:run><hp:t>'
            escaped = [escape_xml(str(x)) for x in val]
            return '</hp:t></hp:run></hp:p>\n  <hp:p>\n    <hp:run><hp:t>'.join(escaped)
        else:
            return escape_xml(str(val))

    new_text = pattern.sub(repl, text)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_text)


def escape_xml(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            .replace('"', '&quot;').replace("'", '&apos;'))


def process_template(template_path, data, out_path):
    if not os.path.exists(template_path):
        print(f"Template {template_path} not found — creating minimal template.")
        os.makedirs(os.path.dirname(template_path), exist_ok=True)
        create_minimal_hwpx(template_path)

    tmpdir = tempfile.mkdtemp()
    try:
        unzip_to_dir(template_path, tmpdir)
        # replace in section*.xml files under tmpdir/Contents
        contents_dir = os.path.join(tmpdir, 'Contents')
        if os.path.isdir(contents_dir):
            for fn in glob.glob(os.path.join(contents_dir, 'section*.xml')):
                replace_placeholders_in_file(fn, data)
        else:
            # fallback: replace anywhere .xml files
            for fn in glob.glob(os.path.join(tmpdir, '**', '*.xml'), recursive=True):
                replace_placeholders_in_file(fn, data)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        rezip_dir(tmpdir, out_path)
        print(f"Wrote injected HWPX to: {out_path}")
    finally:
        shutil.rmtree(tmpdir)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--template', default=os.path.join(WORKDIR, 'input', 'hwpx_templates', 'template.hwpx'))
    p.add_argument('--data', default=os.path.join(WORKDIR, 'input', 'reference', 'sample_data.json'))
    p.add_argument('--output', default=os.path.join(WORKDIR, 'output', 'injected.hwpx'))
    args = p.parse_args()

    data = load_data(args.data)
    process_template(args.template, data, args.output)


if __name__ == '__main__':
    main()
