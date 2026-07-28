# sql="""create database if not exists AI_chat"""
# CREATE TABLE `chat_info` (
#   `id` int NOT NULL AUTO_INCREMENT COMMENT '序号',
#   `duser` varchar(500) NOT NULL COMMENT '提问',
#   `AI` varchar(500) NOT NULL COMMENT '回答',
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

# CREATE TABLE `teacher_info` (
#    `id` int NOT NULL AUTO_INCREMENT COMMENT '序号',
#    `duser` varchar(500) NOT NULL COMMENT '提问',
#    `AI` varchar(500) NOT NULL COMMENT '回答',
#    PRIMARY KEY (`id`)
#  ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

# CREATE TABLE `history` (
#   `id` int NOT NULL AUTO_INCREMENT,
#   `card` varchar(5000) NOT NULL,
# 	`update_time` datetime not null,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
#
# create trigger update_trigger
# before insert on history
# for each ROW
# set new.update_time=NOW()

import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

class Dataset():
    def __init__(self,database,host='localhost',port=3306,user='root',password=os.getenv("DB_PASSWORD")):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
    def connect(self):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )
    def change(self,sql):
        db=self.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()

    def select(self,sql):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        res=cursor.fetchall()
        cursor.close()
        db.close()
        return res
if __name__ == '__main__':
    obj=Dataset('AI_chat')
    sql = """insert into chat_info values(0,"data","total_result")"""
    obj.change(sql)
