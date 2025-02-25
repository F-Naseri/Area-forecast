import requests
from bs4 import BeautifulSoup
import pyodbc
from dotenv import load_dotenv
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

load_dotenv()

server = os.getenv('SERVER')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
database = 'UserDB'

conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE=UserDB;UID=sa;PWD={password}'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

sql_query = """
IF OBJECT_ID('dbo.scrapethissite', 'U') IS NOT NULL  
BEGIN
    TRUNCATE TABLE scrapethissite;  
END
ELSE  
BEGIN
    CREATE TABLE scrapethissite (
        country NVARCHAR(100) PRIMARY KEY,
        capital NVARCHAR(100) NOT NULL,
        population INT NOT NULL,
        area FLOAT(10) NOT NULL
    );
END;
"""
cursor.execute(sql_query)
conn.commit()

response = requests.get('https://www.scrapethissite.com/pages/simple/')
#print(response)
soup=BeautifulSoup(response.text,'html.parser')
ads=soup.find_all('div',class_='col-md-4 country')

for i in ads:    
    country=i.find('h3').text.strip()
    population=i.find('span',class_='country-population').text.strip()
    capital=i.find('span',class_='country-capital').text.strip()
    area=i.find('span',class_='country-area').text.strip()
    #print(f'{country} - {population} - {capital} - {area}')
    cursor.execute("INSERT INTO scrapethissite (country, capital, population, area) VALUES (?, ?, ?, ?)", (country, capital, population, area))
    conn.commit()

try:
    query = "SELECT country, population, area FROM scrapethissite"
    df = pd.read_sql(query, conn)
except pyodbc.Error as ex:
    sqlstate = ex.args[0]
    print(f"Error fetching data: {sqlstate}")
    conn.close()
    exit()

conn.close()

df['population'] = pd.to_numeric(df['population'], errors='coerce')
df['area'] = pd.to_numeric(df['area'], errors='coerce')
df.dropna(inplace=True)

X = df[['population']]
y = df['area']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Linear Regression Results:")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")


def predict_area(population):
    try:
        population = float(population)
        predicted_area = model.predict([[population]])  

        print("\nPredicted area:")
        print(f"Linear Model: {predicted_area[0]:.2f}")

    except ValueError:
        print("Invalid population input. Please enter a number.")

#while True:
    #try:
        #population_input = input("\nEnter a population to guess the area (or 'exit' to quit): ") 
        #if population_input.lower() == 'exit':
            #break
        #predict_area(population_input)
    #except ValueError:
        #print("Invalid input. Please enter a number or 'exit'.")

# ... (بقیه کدهای پروژه شما، شامل تعریف توابع، اسکریپت وب اسکرپینگ، آموزش مدل و غیره)

# ... (تعریف تابع predict_area)

# ... (آموزش مدل: model.fit(X_train, y_train))

# --- شروع کدهای PyQt ---
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle("Forecast of the country's area")

population_label = QLabel("Population:")
population_entry = QLineEdit()
predict_button = QPushButton("Area forecast")
result_label = QLabel("")

layout = QVBoxLayout()
layout.addWidget(population_label)
layout.addWidget(population_entry)
layout.addWidget(predict_button)
layout.addWidget(result_label)
window.setLayout(layout)

def predict_area_gui_qt(population_str):
    try:
        population = float(population_str)
        predicted_area = model.predict([[population]])
        result_label.setText(f"Projected area: {predicted_area[0]:.2f}")
    except ValueError:
        result_label.setText("Invalid input. Please enter a number.")

predict_button.clicked.connect(lambda: predict_area_gui_qt(population_entry.text()))

window.show()
app.exec()
# --- پایان کدهای PyQt ---