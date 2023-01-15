from db_requests import db_conn


# update ministry prist on day
def update_shedule_ministry(ministry_prist, day, month):
	conn = db_conn()
	with conn.cursor() as cursor:
		cursor.execute(f"""UPDATE public.{month} SET ministry = '{ministry_prist}'
		WHERE day_month = {day}""")
	if conn:
		conn.commit()
		conn.close()


# update support prist
def update_support_prist(prist_name, day, month):
	conn = db_conn()
	with conn.cursor() as cursor:
		cursor.execute(f"""UPDATE public.{month} SET support_prist = {prist_name}
		WHERE day_month = {day}""")


# update time start on day
def update_timestart(time, day, month):
	conn = db_conn()
	with conn.cursor() as cursor:
		cursor.execute(f"""UPDATE public.{month} SET time_start = {time}
		WHERE day_month = {day}""")
	if conn:
		conn.commit()
		conn.close()


# update type of worship
def update_type_worship(type_str, day, month):
	conn = db_conn()
	with conn.cursor() as cursor:
		cursor.execute(f"""UPDATE public.{month} SET type_of_worship = {type_str}
		WHERE day_month = {day}""")
	if conn:
		conn.commit()
		conn.close()


# delete one worship from database
def delete_worship(day, time, month):
	conn = db_conn()
	with conn.cursor() as cursor:
		cursor.execute(f"""DELETE FROM public.{month} WHERE day_month = {day}
		AND time_start = {time}""")
	if conn:
		conn.commit()
		conn.close()
