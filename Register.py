import webbrowser as wb
import pyautogui as pg
from time import sleep
import pandas as pd

dataframe = pd.read_excel('contacts.xlsx', skiprows=0)
print(dataframe)
myData = dataframe.to_numpy().tolist()
print(myData)
# wb.open("https://bestforyouth.net/joinus?id=BFY23257929")
