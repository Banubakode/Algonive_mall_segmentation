# ==============================
# 📊 Mall Customer Segmentation Dashboard
# ==============================

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import plotly.express as px
from dash import Dash, dcc, html
import os

# ------------------------------
# Load the dataset
# ------------------------------
df = pd.read_csv('customer_segments.csv')  # ensure this file is in your root folder

# ------------------------------
# KMeans Clustering (optional – only if not pre-labeled)
# ------------------------------
if 'Cluster' not in df.columns:
    X = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]
    kmeans = KMeans(n_clusters=5, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)

# ------------------------------
# Initialize the Dash app
# ------------------------------
app = Dash(__name__)

app.title = "Mall Customer Segmentation Dashboard"

# ------------------------------
# Layout
# ------------------------------
app.layout = html.Div([
    html.H1("🛍️ Mall Customer Segmentation Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Select feature for X-axis:"),
        dcc.Dropdown(
            id='x-axis',
            options=[
                {'label': 'Age', 'value': 'Age'},
                {'label': 'Annual Income (k$)', 'value': 'Annual Income (k$)'},
                {'label': 'Spending Score (1-100)', 'value': 'Spending Score (1-100)'}
            ],
            value='Annual Income (k$)',
            clearable=False
        ),
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        html.Label("Select feature for Y-axis:"),
        dcc.Dropdown(
            id='y-axis',
            options=[
                {'label': 'Age', 'value': 'Age'},
                {'label': 'Annual Income (k$)', 'value': 'Annual Income (k$)'},
                {'label': 'Spending Score (1-100)', 'value': 'Spending Score (1-100)'}
            ],
            value='Spending Score (1-100)',
            clearable=False
        ),
    ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

    dcc.Graph(id='cluster-graph')
])

# ------------------------------
# Callback
# ------------------------------
@app.callback(
    output=dcc.Output('cluster-graph', 'figure'),
    inputs=[
        dcc.Input('x-axis', 'value'),
        dcc.Input('y-axis', 'value')
    ]
)
def update_graph(x_axis, y_axis):
    fig = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        color='Cluster',
        hover_data=['Age', 'Annual Income (k$)', 'Spending Score (1-100)'],
        title=f'Customer Segmentation: {x_axis} vs {y_axis}'
    )
    fig.update_layout(transition_duration=500)
    return fig

# ------------------------------
# Run the server (Render compatible)
# ------------------------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8050))  # Render assigns this automatically
    app.run_server(host="0.0.0.0", port=port, debug=False)





