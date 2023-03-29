# Extract text from a PDF file and preprocess it
#
# This is a simple example of how to extract text from a PDF file and preprocess it.
# The preprocessing includes:
# - removing the header and footer
# - removing the page numbers
# - removing the table of contents
# - removing the index
# - removing the bibliography
# - removing the footnotes
# - removing the endnotes
# - removing the images
# - removing the tables
# - removing the captions
# - removing the headers
# - removing the footers
# - removing the titles
# - removing the subtitles
# - removing the authors
# - removing the affiliations
# - removing the abstract
# - removing the keywords
# - removing the dates
# - removing the addresses
# - removing the emails

import os
import re
import sys
import time
import shutil
import logging
import argparse
import tempfile
import subprocess
import multiprocessing
from pathlib import Path
from functools import partial
from collections import defaultdict
import multiprocessing as mp

import fitz
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject
from PyPDF2.generic import NameObject, createStringObject
from PyPDF2.utils import PdfReadError

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import PDFPageAggregator


def get_pdf_pages(pdf_path):
    """
    Get the number of pages in a PDF file.
    """
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        return pdf_reader.getNumPages()
    
def get_pdf_info(pdf_path):
    """
    Get the number of pages in a PDF file.
    """
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        return pdf_reader.getDocumentInfo()
    
def get_pdf_metadata(pdf_path):
    """
    Get the number of pages in a PDF file.
    """
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        return pdf_reader.getXmpMetadata()
    
def get_pdf_text(pdf_path):
    """
    Get the text of a PDF file.
    """
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        return pdf_reader.getPage(0).extractText()


    
                


