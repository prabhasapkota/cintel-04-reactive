"""
Purpose: Provide user interaction options for the Tips dataset.

"""
from shiny import ui


def get_tips_inputs():
    return ui.panel_sidebar(
        ui.h2("Tip Interaction"),
        ui.tags.hr(),
        ui.input_numeric("TPIS_MAX_TIP", "Max tips:", value=10.0),
        
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )