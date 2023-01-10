import docx
import psycopg2
from db_requests import add_month_shedule
from win32com import client as wc
import os
import re

# convert file .doc to file .docx
def conv_doc2docx():
	w = wc.Dispatch('Word.Application')

	paths = []
	folder = os.getcwd()

	for root, dirs, files in os.walk(folder):
		for file in files:
			if file.endswith('doc') and not file.startswith('~'):
				paths.append(os.path.join(root, file))

	for path in paths:
		doc = w.Documents.Open(path)
		doc.SaveAs(path+'x', 16)
		doc.Close()

	w.Quit()

# delete all doc/docx files
def delete_word_file():
	paths = []
	folder = os.getcwd()
	for root, dirs, files in os.walk(folder):
		for file in files:
			if file.endswith('doc') or file.endswith('docx'):
				paths.append(os.path.join(root, file))
	for path in paths:
		os.remove(path)

# open fil to read and extract
def open_file():
	doc = docx.Document('Расписание на Январь 2023 духовенство.docx')
	return doc

# exctract data from table object
def extract_table(doc):
	table = doc.tables[0]
	table_lst = [['' for i in range(len(table.columns))] for j in range(len(table.rows))]
	for i, row in enumerate(table.rows):
		for j, cell in enumerate(row.cells):
			if cell.text:
				table_lst[i][j] = cell.text
	table_lst.pop(0)
	return table_lst


def parsing_file():
	# need create download file function on server
	conv_doc2docx()
	month = input()
	table_lst = extract_table(open_file())
	add_month_shedule(table_lst, month)

	# except Exception as _ex:
	# 	print("[INFO] error while working with PostgreSQL", _ex)
	# finally:
	# 	if conn:
	# 		conn.commit()
	# 		conn.close()
	# 		print('[INFO] PostgreSQL connection closed')

parsing_file()