# encoding: utf-8
import pandas as pd
import MySQLdb
from search_system.settings import DATABASES


def export_csv_to_sql(csv_path, db_para):
    """
    export csv file to mysql
    :param csv_path: csv file path
    :param db_para: db parameters
    :return:
    """
    # open CSV file and create a dataframe object
    data = pd.read_csv(csv_path)
    conn = MySQLdb.connect(
        host=db_para["HOST"],
        user=db_para["USER"],
        passwd=db_para["PASSWORD"],
        db=db_para["NAME"],
    )
    # create a cursor object
    cursor = conn.cursor()

    # insert data into MySQL database
    for row in data.itertuples():
        query = f"INSERT INTO candidate_skill_scores (score, candidate_name, skill) VALUES (%s, %s, %s)"
        cursor.execute(query, (row.score, row.candidate_name, row.skill))

    # commit changes to database and close cursor and connection
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    csv = "../search_system_doc/candidate_skill_scores.csv"
    # connect to MySQL database
    mysql_para = DATABASES.get('default')

    export_csv_to_sql(csv_path=csv, db_para=mysql_para)
