import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# ------------------------
# 1. Load Customer Data
# ------------------------
# Place your CSV file in the same folder as app.py
# CSV should have columns: CustomerID, Annual Income (k$), Spending Score (1-100), Cluster
df_customers = pd.read_csv("customer_data.csv")

# ------------------------
# 2. Cluster Summary Data
# ------------------------
df_summary = pd.DataFrame({
    'Cluster Label': ['Budget Group', 'Growth Opportunity', 'Luxury Cautious', 'VIP Customers'],
    'Age_mean': [32.88, 25.44, 39.37, 53.98],
    'Age_min': [27, 18, 19, 35],
    'Age_max': [40, 38, 59, 70],
    'Annual Income (k$)_mean': [86.1, 40, 86.5, 47.71],
    'Annual Income (k$)_min': [69, 15, 64, 18],
    'Annual Income (k$)_max': [137, 67, 137, 79],
    'Spending Score (1-100)_mean': [81.53, 60.3, 19.58, 39.97],
    'Spending Score (1-100)_min': [58, 6, 1, 3],
    'Spending Score (1-100)_max': [97, 99, 42, 60],
    'CustomerID_count': [40, 57, 38, 65]
})

# ------------------------
# 3. Initialize Dash App
# ------------------------
app = dash.Dash(__name__)
server = app.server  # Required for Render

# ------------------------
# 4. Scatter Plot: Income vs Spending Score
# ------------------------
fig_scatter = px.scatter(
    df_customers,
    x='Annual Income (k$)',
    y='Spending Score (1-100)',
    color='Cluster',
    title='Income vs Spending Score by Cluster',
    hover_data=['CustomerID']
)

# ------------------------
# 5. Pie Chart: Customer distribution by cluster
# ------------------------
cluster_counts = df_customers['Cluster'].value_counts().reset_index()
cluster_counts.columns = ['Cluster', 'Count']
fig_pie = px.pie(cluster_counts, names='Cluster', values='Count', title='Customer Distribution by Cluster')

# ------------------------
# 6. Layout
# ------------------------
app.layout = html.Div(style={'font-family': 'Arial, sans-serif', 'margin': '20px'}, children=[

    # Dashboard Title with emoji
    html.H1("🧩 Customer Segmentation Dashboard", style={'text-align': 'center', 'margin-bottom': '30px'}),

    # Scatter Plot
    html.Div(dcc.Graph(figure=fig_scatter), style={'width': '100%'}),

    # Pie Chart
    html.Div(dcc.Graph(figure=fig_pie), style={'width': '50%', 'margin-top': '40px'}),

    # Cluster Summary Table
    html.Div([
        html.H3("Cluster Profile Summary", style={'margin-top': '40px'}),
        html.Table([
            html.Thead(
                html.Tr([html.Th(col, style={'padding': '5px', 'border': '1px solid black'}) for col in df_summary.columns])
            ),
            html.Tbody([
                html.Tr([html.Td(df_summary.iloc[i][col], style={'padding': '5px', 'border': '1px solid black'}) 
                         for col in df_summary.columns])
                for i in range(len(df_summary))
            ])
        ], style={'border-collapse': 'collapse', 'width': '100%'})
    ])
])

# ------------------------
# 7. Run Server
# ------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
