""" 
Purpose: Provide reactive output for the MT Cars dataset.

- Use inputs from the UI Sidebar to filter the dataset.
- Update reactive outputs in the UI Main Panel.

Matching the IDs in the UI Sidebar and function/output names in the UI Main Panel
to this server code is critical. They are case sensitive and must match exactly.

"""

import pathlib
from shiny import render , reactive
import matplotlib.pyplot as plt
import pandas as pd
from plotnine import aes, geom_point, ggplot, ggtitle
from shinywidgets import render_widget
import plotly.express as px

from util_logger import setup_logger

logger, logname = setup_logger(__name__)




def get_tip_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    p = pathlib.Path(__file__).parent.joinpath("data").joinpath("mtcars.csv")
    # logger.info(f"Reading data from {p}")
    original_df = pd.read_csv(p)
    total_count = len(original_df)

    reactive_df = reactive.Value()

    @reactive.Effect
    @reactive.event(input.TIP_RANGE,)
    def _():
        df = original_df.copy()

        input_range = input.TIP_RANGE()
        input_min = input_range[1]
        input_max = input_range[10]

        """
        Filter the dataframe to just those greater than or equal to the min
        and less than or equal to the max
        Note: The ampersand (&) is the Python operator for AND
        The column name is in quotes and is "mpg".
        You must be familiar with the dataset to know the column names.
        """

        tips_filter = (df["tip"] >= input_min) & (df["tip"] <= input_max)
        

    # Set the reactive value
    reactive_df.set(df)

    


    @output
    @render.text
    def tip_record_count_string():
        filtered_df = reactive_df.get()
        filtered_count = len(filtered_df)
        message = f"Showing {filtered_count} of {total_count} records"
        # logger.debug(f"filter message: {message}")
        return message
    
    @output
    @render.table
    def tip_filtered_table():
        filtered_df = reactive_df.get()
        return filtered_df


    @output
    @render_widget
    def tip_output_widget1():
        df = reactive_df.get()
        plotly_express_plot = px.scatter(df, x="total bill", y="tip")
        plotly_express_plot.update_layout(title="Tips with Plotly Express")
        return plotly_express_plot


    # Return a list of function names for use in reactive outputs
    return [
        tip_record_count_string,
        tip_filtered_table,
        tip_output_widget1
       ]