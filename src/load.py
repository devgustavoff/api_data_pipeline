from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import Table, MetaData 
import os

def load(datas):

    engine = create_engine(f"postgresql://postgres:{os.getenv("PASSWORD_DB")}@localhost:5433/weather")
    metadata = MetaData()

    table = Table('weather_readings', metadata, autoload_with=engine)

    records = datas.to_dict(orient='records') 

    insert_stmt = insert(table).values(records) 

    do_update_stmt = insert_stmt.on_conflict_do_update(         
        constraint="uq_name_collected_at",
        set_={
            "temperature": insert_stmt.excluded.temperature,
            "humidity": insert_stmt.excluded.humidity,
            "description": insert_stmt.excluded.description
        }
    )

    with engine.begin() as conn: 
        try:
            conn.execute(do_update_stmt)
            print("Data inserted successfully!")
        except Exception as e:
            print("Error:", e)
            raise
