{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c21bdf18",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pymysql\n",
    "import schedule\n",
    "import time\n",
    "from datetime import datetime\n",
    "\n",
    "def test():\n",
    "    second = datetime.now().time().second\n",
    "\n",
    "    if second < 15:\n",
    "        t = 'time1'\n",
    "    elif second < 30:\n",
    "        t = 'time2'\n",
    "    elif second < 45:\n",
    "        t = 'time3'\n",
    "    else:\n",
    "        t = 'time4'\n",
    "\n",
    "    print(t)\n",
    "\n",
    "    meal_db = pymysql.connect(\n",
    "        user='admin',\n",
    "        passwd='happymisic1#',\n",
    "        host='testdata.ch1v7vb7kdnw.ap-northeast-2.rds.amazonaws.com',\n",
    "        db='batchschedule',\n",
    "        charset='utf8'\n",
    "#         autocommit = True\n",
    "    )\n",
    "    cursor = meal_db.cursor(pymysql.cursors.DictCursor)\n",
    "\n",
    "    sql1 = \"TRUNCATE TABLE twenties;\"\n",
    "    sql2 = \"TRUNCATE TABLE thirties;\"\n",
    "    sql3 = \"TRUNCATE TABLE fourties;\"\n",
    "\n",
    "    cursor.execute(sql1)\n",
    "    cursor.execute(sql2)\n",
    "    cursor.execute(sql3)\n",
    "        \n",
    "    sql4 = \"INSERT INTO twenties (menu_code, menu) SELECT menu_code, menu FROM menu WHERE age=20 and \" + t + \" = 1;\"\n",
    "    sql5 = \"INSERT INTO thirties (menu_code, menu) SELECT menu_code, menu FROM menu WHERE age=30 and \" + t + \" = 1;\"\n",
    "    sql6 = \"INSERT INTO fourties (menu_code, menu) SELECT menu_code, menu FROM menu WHERE age=40 and \" + t + \" = 1;\"\n",
    "\n",
    "    cursor.execute(sql4)\n",
    "    cursor.execute(sql5)\n",
    "    cursor.execute(sql6)\n",
    "    meal_db.commit()\n",
    "\n",
    "    sql = \"select * from twenties;\"\n",
    "    cursor.execute(sql)\n",
    "    result = cursor.fetchall()\n",
    "    print(result)\n",
    "    \n",
    "    \n",
    "\n",
    "# schedule.every(5).seconds.do(test)\n",
    "\n",
    "# while True:\n",
    "#     schedule.run_pending()\n",
    "#     time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30846fe2",
   "metadata": {},
   "outputs": [],
   "source": [
    "test()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "053c8993",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "time2\n",
      "[{'id': 1, 'menu_code': 'MN000001', 'menu': '1955버거'}, {'id': 2, 'menu_code': 'MN000002', 'menu': 'BBQ포크'}, {'id': 3, 'menu_code': 'MN000003', 'menu': 'BLT샌드위치'}, {'id': 4, 'menu_code': 'MN000004', 'menu': 'LA갈비'}, {'id': 5, 'menu_code': 'MN000005', 'menu': 'LA갈비도시락'}, {'id': 6, 'menu_code': 'MN000006', 'menu': 'LA갈비화로구이반상'}, {'id': 7, 'menu_code': 'MN000007', 'menu': 'XO볶음밥'}, {'id': 8, 'menu_code': 'MN000008', 'menu': '가께우동'}, {'id': 9, 'menu_code': 'MN000009', 'menu': '가나슈'}, {'id': 10, 'menu_code': 'MN000010', 'menu': '가나슈마카롱'}, {'id': 11, 'menu_code': 'MN000011', 'menu': '가나슈케이크'}, {'id': 12, 'menu_code': 'MN000012', 'menu': '가다랑어초밥'}, {'id': 13, 'menu_code': 'MN000013', 'menu': '가든샐러드'}, {'id': 14, 'menu_code': 'MN000014', 'menu': '가또쇼콜라'}, {'id': 15, 'menu_code': 'MN000016', 'menu': '가라아게덮밥'}, {'id': 16, 'menu_code': 'MN000017', 'menu': '가라아게돈부리'}, {'id': 17, 'menu_code': 'MN000018', 'menu': '가라아게동'}, {'id': 18, 'menu_code': 'MN000019', 'menu': '가라아게오므라이스'}]\n"
     ]
    }
   ],
   "source": [
    "test()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
