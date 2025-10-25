# app.py
import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample data for demo
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 15, 13, 17, 14],
    'category': ['A', 'B', 'A', 'B', 'A']
})

# Initialize Dash app
app = dash.Dash(__name__)
server = app.server  # <- needed for Render

# Layout
app.layout = html.Div([
    html.H1("Dashboard Example for Render"),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': c, 'value': c} for c in df['category'].unique()],
        value='A'
    ),
    dcc.Graph(id='cluster-graph')
])

# Callback to update graph
@app.callback(
    Output('cluster-graph', 'figure'),
    Input('dropdown', 'value')
)
def update_graph(selected_category):
    filtered_df = df[df['category'] == selected_category]
    fig = px.scatter(filtered_df, x='x', y='y', color='category', title=f"Category: {selected_category}")
    return fig

# Run server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))  # Render provides PORT environment variable
    app.run_server(host='0.0.0.0', port=port, debug=False)
