import pymysql
import schedule
import time
from datetime import datetime

def lambda_handler(event,context):
    minute = datetime.now().time().minute

    if minute%4 == 0:
        t = 'time1'
    if minute%4 == 1:
        t = 'time2'
    if minute%4 == 2:
        t = 'time3'
    if minute%4 == 3:
        t = 'time4'

    print(t)

    meal_db = pymysql.connect(
        user='admin',
        passwd='happymisic1#',
        host='testdata.ch1v7vb7kdnw.ap-northeast-2.rds.amazonaws.com',
        db='batchschedule',
        charset='utf8'
    )
    cursor = meal_db.cursor(pymysql.cursors.DictCursor)

    sql1 = "TRUNCATE TABLE twenties;"
    sql2 = "TRUNCATE TABLE thirties;"
    sql3 = "TRUNCATE TABLE fourties;"

    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)

    sql4 = "INSERT INTO twenties (menu_code, menu) SELECT menu_code, menu FROM menu WHERE age=20 and " + t + " = 1;"
    sql5 = "INSERT INTO thirties (menu_code, menu) SELECT menu_code, menu FROM menu WHERE age=30 and " + t + " = 1;"
    sql6 = "INSERT INTO fourties (menu_code, menu) SELECT menu_code, menu FROM menu WHERE age=40 and " + t + " = 1;"

    cursor.execute(sql4)
    cursor.execute(sql5)
    cursor.execute(sql6)
    meal_db.commit()

    sql = "select * from twenties;"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    
    return result
