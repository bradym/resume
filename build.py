#!/usr/bin/env python2
import subprocess
import jinja2
from rst2pdf.createpdf import RstToPdf
import tabulate
import yaml

with open("secrets.yaml", 'r') as stream:
    secrets = yaml.load(stream)

table = [
    [secrets['address'], secrets['email']],
    [secrets['phone'], "http://bradym.net"]
]

rst_table = tabulate.tabulate(table, tablefmt='rst')

rendered = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))\
    .get_template('resume.rst').render({'table': rst_table})

RstToPdf(stylesheets=['style.json'], breaklevel=0).createPdf(rendered, output='resume.pdf')

subprocess.call('open resume.pdf', shell=True)
