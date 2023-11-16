from fastapi import FastAPI
from pydantic import BaseModel
# import sqlite3
from sqlfile import create_table

# Initialize FastAPI
app = FastAPI()

# Create a Pydantic model for the data expected in the POST request
class Item(BaseModel):
    status: str

# Route handling POST requests
@app.post("/check/")
async def create_item(item: Item):
    def call_api(t):
        conn = create_table()
        if t == "pass":
            cursor = conn.cursor()
            passed_data = cursor.execute('''SELECT * from pass_table''')
            value = [ans for ans in passed_data]
            # rows = cursor.fetchall()
            # for row in rows:
            # print(row)
            # Commit your changes in the database
            conn.commit()
            # Closing the connection
            conn.close()
            return value
        elif t == "fail":
            cursor = conn.cursor()
            failed_data = cursor.execute('''SELECT * from fail_table''')
            value = [ans for ans in failed_data]
            # print(value)
            # Commit your changes in the database
            conn.commit()
            # Closing the connection
            conn.close()
            return value
        else:
            return None
    b = call_api(item.status)
    return b
