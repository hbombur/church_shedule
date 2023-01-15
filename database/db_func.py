from db_requests import db_conn


# formatting shortname of month to name of table for database
def format_name_table(short_name_month):
	return "shedule_" + short_name_month + "_2023"
