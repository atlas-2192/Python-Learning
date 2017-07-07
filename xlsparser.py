# -*- coding: utf-8 -*-
import xlrd
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def whatisthis(s):
    if isinstance(s, str):
        print "ordinary string"
    elif isinstance(s, unicode):
        print "unicode string"
    else:
        print "not a string"

def force_decode(string, codecs=['utf8', 'big5']):
    for i in codecs:
        try:
            return string.decode(i)
        except:
            pass

def open_xls_parse(file):
    workbook = xlrd.open_workbook('test.xls')
    worksheets = workbook.sheet_names()
    for worksheet in worksheets:
        worksheet = workbook.sheet_by_name(worksheet)
        num_rows = worksheet.nrows - 1
        num_cells = worksheet.ncols - 1
        curr_row = -1
        while curr_row < num_rows:
            curr_row += 1
            row = worksheet.row(curr_row)
            print 'Row:', curr_row
            curr_cell = -1
            while curr_cell < num_cells:
                curr_cell += 1
                # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
                cell_type = worksheet.cell_type(curr_row, curr_cell)
                cell_value = worksheet.cell_value(curr_row, curr_cell)
                print ' ', cell_type, ':', cell_value

if __name__ == '__main__':
    if len(sys.argv) == 1: #No other parameter.
        print 'No any argument.'
        print '-------------------------'
        print ' xlsparser.py filename   '
        print '-------------------------'
    else:
        open_xls_parse(sys.argv[1])