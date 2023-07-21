"""_summary_
We are creating a new tab for our shiny app to display the tips dataset loaded earlier.
The CSV file is loaded into a pandas DataFrame and the number of rows is counted.
The server functions are defined in the get_iris_server_functions() function.

"""


import pathlib
from shiny import render
import pandas as pd
import seaborn as sns

from util_logger import setup_logger

logger, logname = setup_logger(__name__)


def get_tips_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    path_to_data = pathlib.Path(__file__).parent.joinpath("data").joinpath("tips.csv")
    original_df = pd.read_csv(path_to_data)

    # Use the len() function to get the number of rows in the DataFrame.
    total_count = len(original_df)

    @output
    @render.table
    def tips_table():
        return original_df

    @output
    @render.text
    def tips_record_count_string():
        message = f"Showing {total_count} records"
        logger.debug(f"filter message: {message}")
        return message

    @output
    @render.plot
    def tips_plot():
        """
        Use Seaborn to make a quick scatterplot.
        Provide a pandas DataFrame and the names of the columns to plot.
        """
        plt = sns.scatterplot(
            data=original_df,
            x="total bill",
            y="tip",
        )
        return plt

    # Return a list of function names for use in reactive outputs
    functions = [
        tips_table,
        tips_record_count_string,
        tips_plot,
    ]