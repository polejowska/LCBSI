from dash.dependencies import Input, Output

from app import app
from callbacks.predicting import register_predicting_callbacks
from callbacks.uploading import register_image_uploading_callbacks
from pages import main_page


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return main_page.layout
    else:
        return "404 Not Found"


if __name__ == "__main__":
    register_image_uploading_callbacks(app)
    register_predicting_callbacks(app)

    app.run_server(debug=False)
