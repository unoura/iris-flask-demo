from sqlalchemy import create_engine, text
from faker import Faker

# 件数
ROW_COUNT = 10000

# IRIS接続情報 
username='SuperUser'
password='YOUR-PASSWORD'
hostname='localhost'
port='1972'
namespace='USER'
CONNECTION_STRING=f"iris://{username}:{password}@{hostname}:{port}/{namespace}"
engine=create_engine(CONNECTION_STRING)

fake = Faker('jp-JP')

# Test.Personテーブルへダミーデータを登録
with engine.connect() as conn:
  with conn.begin():
    for index  in range(ROW_COUNT):
      sql = text(""" 
        INSERT INTO test.person (Name, Email, DOB, Job) values 
        (:name, :email, :dob, :job)
        """)
      conn.execute(sql, {
        'name': fake.name(),
        'email': fake.ascii_safe_email(),
     'dob': fake.date_of_birth(minimum_age=1, maximum_age=100),
     'job': fake.job()
      })
