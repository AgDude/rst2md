#!/usr/bin/env python

"""
rst2md.py
======

This module provides a simple command line interface that uses the
Markdown writer to output from reStructuredText source.
"""
import sys, os
import locale

try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_file, default_description
try:
    from docutils.writers import markdown
except ImportError:
    # Obviously still just testing this package (i.e. have not installed it)
    # Remove this try-except from the final release version.
    sys.path.insert(0, os.path.abspath('.'))
    import markdown

description = ('Generates Markdown formatted text from standalone '
               'reStructuredText sources.  ' + default_description)

def main():
    this_dir = os.path.dirname(os.path.realpath(__file__))
    src_dir = 'source'
    dest = 'build/md'
    rst_list = [os.path.join(dp, f) for dp, dn, filenames in os.walk(src_dir) for f in filenames if os.path.splitext(f)[1] == '.rst']
    
    for rst in rst_list:
        outpath = os.path.join(dest,os.path.relpath(rst, src_dir)).replace('.rst','.md')
        if not os.path.exists(os.path.dirname(outpath)):
            os.makedirs(os.path.dirname(outpath))
        try:
            publish_file(source_path = rst,
                         destination_path = outpath,
                         writer = markdown.Writer()
                         )
        except UnicodeEncodeError as e:
            print e
            print 'Unicode error in file: %s' % rst

main()
# publish_cmdline(writer=markdown.Writer(), description=description)
