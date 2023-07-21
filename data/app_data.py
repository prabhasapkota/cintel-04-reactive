"""
Purpose: Use Python to generate local data files in this folder.

To create data files,
   modify the code to import the dataset in the format you want.
   Uncomment those lines and run this script in the terminal with `python app_data.py`.

After creating the data files, you can comment out code you don't need to re-run.
In VS Code, you can select many lines, and use CTRL + / to comment out all of them.

CSV files can be easily reviewed in VS Code.

@imports pathlib to manage directories and file paths
@imports seaborn as sns to load datasets into Pandas DataFrames (df)
@imports pandas as pd to write DataFrames (df) to Excel and CSV files
@imports bokeh.sampledata to load sample datasets into Pandas DataFrames (df)

mtcars.csv was copied from the Shiny example at:
https://shinylive.io/py/examples/#read-local-csv


"""

import pathlib
import pandas as pd
import seaborn as sns

from bokeh.sampledata.les_mis import data as les_mis_data

from util_logger import setup_logger

logger, logname = setup_logger(__name__)

# Get a path object representing this data folder.
data_folder = pathlib.Path(__file__).parent

penguins_df = sns.load_dataset("penguins")
penguins_df.to_excel(data_folder.joinpath("penguins.xlsx"))
penguins_df.to_csv(data_folder.joinpath("penguins.csv"))

flights_df = sns.load_dataset("flights")
flights_df.to_excel(data_folder.joinpath("flights.xlsx"))
flights_df.to_csv(data_folder.joinpath("flights.csv"))

mtcars_df = pd.read_csv(data_folder.joinpath("mtcars.csv"))
mtcars_df.to_excel(data_folder.joinpath("mtcars.xlsx"))

les_mis = pd.DataFrame(les_mis_data["links"])
les_mis.to_excel("les_mis.xlsx")
les_mis.to_csv("les_mis.csv")

tips_df = sns.load_dataset("tips")
tips_df.to_excel(data_folder.joinpath("tips.xlsx"))
tips_df.to_csv(data_folder.joinpath("tips.csv"))


# url="https://webpath/to/your/data.csv"
# df=pd.read_csv(url)
