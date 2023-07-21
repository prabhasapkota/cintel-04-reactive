"""
Purpose: Display outputs for Tips dataset.

Choose the correct ui method for the type of output you want to display.
Provide the exact name of the server function that will provide the output.
"""
from shiny import ui
from shinywidgets import output_widget

def get_tip_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Filtered Tip : Charts"),
            output_widget("tip_output_widget1"),
            ui.tags.hr(),
            ui.h3("Filtered Tip Table"),
            ui.output_text("tip_record_count_string"),
            ui.output_table("tip_filtered_table"),
            ui.tags.hr(),
        ),
    )