# ================================================
# Customer Segmentation Dashboard using Plotly Dash
# ================================================

# ---- Import Libraries ----
from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

# ---- Load the Processed Customer Data ----
# Make sure this file is in the same folder as this script
df = pd.read_csv('customer_segments.csv')

# ---- Create Cluster Profile Summary ----
cluster_profiles = df.groupby('Cluster Label').agg({
    'Age': ['mean', 'min', 'max'],
    'Annual Income (k$)': ['mean', 'min', 'max'],
    'Spending Score (1-100)': ['mean', 'min', 'max'],
    'CustomerID': 'count'
}).round(2)

# Flatten the multi-level column names
cluster_profiles.columns = ['_'.join(col) for col in cluster_profiles.columns]
cluster_profiles = cluster_profiles.reset_index()

# ---- Create Visualizations ----

# Scatter Plot: Annual Income vs Spending Score by Cluster
scatter_fig = px.scatter(
    df,
    x='Annual Income (k$)',
    y='Spending Score (1-100)',
    color='Cluster Label',
    title='Customer Segments: Income vs Spending Score',
    template='plotly_dark',
    hover_data=['Age']
)

# Pie Chart: Customer distribution across clusters
cluster_counts = df['Cluster Label'].value_counts().reset_index()
cluster_counts.columns = ['Cluster Label', 'Count']

pie_fig = px.pie(
    cluster_counts,
    names='Cluster Label',
    values='Count',
    title='Customer Distribution by Cluster',
    hole=0.3,
    color_discrete_sequence=px.colors.qualitative.Bold
)

# ---- Initialize Dash App ----
app = Dash(__name__)

# ---- Layout of the Dashboard ----
app.layout = html.Div([
    html.H1(
        '🧩 Customer Segmentation Dashboard',
        style={'textAlign': 'center', 'color': '#2E86C1'}
    ),

    html.Div([
        dcc.Graph(figure=scatter_fig),
        dcc.Graph(figure=pie_fig)
    ], style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}),

    html.H3('Cluster Profile Summary', style={'textAlign': 'center'}),

    # Display cluster summary table
    html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in cluster_profiles.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(cluster_profiles.iloc[i][col]) for col in cluster_profiles.columns
            ]) for i in range(len(cluster_profiles))
        ])
    ], style={
        'width': '90%',
        'margin': 'auto',
        'border': '1px solid black',
        'borderCollapse': 'collapse',
        'textAlign': 'center'
    })
])

# ---- Run the Dash App ----
if __name__ == '__main__':
    app.run(debug=True)





