"""
Purpose: Provide user interaction options for the Tips dataset.

"""
from shiny import ui


def get_tip_inputs():
    return ui.panel_sidebar(
        ui.h2("Tip Interaction"),
        ui.tags.hr(),
        ui.input_slider(
            "TIP_RANGE",
            "Tip",
            min=1,
            max=10,
            value=[1, 10],
        ),
        
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )