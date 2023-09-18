import pandas as pd
from my_logging import create_file_console_logger

logger = create_file_console_logger("logger", log_file="cleanse.log",log_level=20)

df = pd.read_csv("input/ICICI prudential Dividend Yield.csv")
df2 = df[['Net Asset Value', 'NAV date']]
df2.rename(columns={'Net Asset Value':'NAV', 'NAV date': 'date'}, inplace=True)
logger.info(df2.columns)

df2.to_csv("data/ICICI_2018to2023Sep_NAV.csv")
