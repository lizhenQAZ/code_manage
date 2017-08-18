import pymysql
import global_data


def create_connection():
    # 新建连接对象
    global_data.conn = pymysql.connect(**global_data.g_mysql_config)


def close_connection():
    # 关闭连接对象
    global_data.conn.close()


def query():
    # 新建光标对象
    conn = global_data.conn
    with conn.cursor() as cur:
        # 执行查询语句
        sql = global_data.g_mysql_query_sql
        cur.execute(sql)
        # results = cur.fetchone()
        # print(results)

        # 获取所有记录列表
        results = cur.fetchall()
        for row in results:
            print(row)
    conn.commit()


def insert():
    # 新建光标对象
    conn = global_data.conn
    with conn.cursor() as cur:
        # 执行插入语句
        sql = global_data.g_mysql_insert_sql
        cur.execute(sql)
    conn.commit()


def query_main():
    create_connection()
    query()
    close_connection()


def insert_main():
    create_connection()
    global_data.g_mysql_insert_sql = '''INSERT INTO scrapy_websites(id, websites) VALUES ('%d', '%s')''' % (1, 'www.baidu.com')
    insert()
    close_connection()


if __name__ == '__main__':
    # insert_main()
    query_main()
