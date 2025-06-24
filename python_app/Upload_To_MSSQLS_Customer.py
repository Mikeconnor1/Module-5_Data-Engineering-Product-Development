
from sqlalchemy import create_engine
import pandas as pd
import pyodbc


server = 'localhost'
database = 'Library_SystemCustomer'
driver = 'ODBC Driver 17 for SQL Server'

connection_string = f"mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver={driver}"
engine = create_engine(connection_string)

books = pd.read_csv('C:/Users/Admin/Desktop/Module-5_Data-Engineering-Product-Development/python_app/Cleaned_03_Library SystemBook.csv')

customers = pd.read_csv('C:/Users/Admin/Desktop/Module-5_Data-Engineering-Product-Development/python_app/Cleaned_03_Library SystemCustomer.csv')

books.to_sql(
  name='Books',
  if_exists="replace",
  con=engine 
)

customers.to_sql(
  name='Customers',
  if_exists="replace",
  con=engine
)

