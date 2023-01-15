import psycopg2
from db_func import format_name_table


# create connection to database
def db_conn():
	conn = psycopg2.connect(
		user="postgres",
		password="11041972propoved",
		host="localhost",
		port="5432",
		dbname="Church_shedule"
	)
	print("Connection to DataBase")
	return conn


# get shortname of month
def get_shortname_month(month):
	conn = db_conn()
	with conn.cursor() as cursor:
		cursor.execute(f"""SELECT shortname_of_month
							FROM public.months
							WHERE ru_name_of_month LIKE %s""", (month,))
		shortname_month = cursor.fetchone()
	if conn:
		conn.close()
	return shortname_month[0]


# check exists table
def check_table(shortname_month):
	conn = db_conn()
	with conn.cursor() as cursor:
		cursor.execute(f"""SELECT EXISTS (
							SELECT *
							FROM pg_catalog.pg_class
							WHERE relname LIKE %s
							);""", (format_name_table(shortname_month),))
		result = cursor.fetchone()
	if conn:
		conn.close()
	return result[0]


# insert data into table of shedule
def insert_shedule(table_lst, shortname_month):
	conn = db_conn()
	with conn.cursor() as cursor:
		for row in table_lst:
			tmp = ''
			for j in row:
				tmp = tmp + "," + j
			cursor.execute(f"""INSERT INTO public.{format_name_table(shortname_month)} (day_month,
							day_week, celebration, ministry, support_prist,
							time_start, type_of_worship)
							VALUES (%s, %s, %s, %s, %s, %s, %s)""", row)
	if conn:
		conn.commit()
		conn.close()


# create new table for shedule on DB
def create_table_month(shortname_month):
	if not check_table(shortname_month):
		conn = db_conn()
		with conn.cursor() as cursor:
			cursor.execute(f"""CREATE TABLE {format_name_table(shortname_month)} (day_month int NOT NULL, 
				day_week varchar NOT NULL,
				celebration varchar NOT NULL,
				ministry varchar NOT NULL,
				support_prist varchar NULL,
				time_start varchar NOT NULL,
				type_of_worship varchar NOT NULL);""")
		if conn:
			conn.commit()
			conn.close()
		print('Table was created')
	else:
		print("Table already exists")


# add new month shedule [need refactor to another file]
def add_month_shedule(table_lst, month):
	shortname_month = get_shortname_month(month)
	create_table_month(shortname_month)
	insert_shedule(table_lst, shortname_month)
