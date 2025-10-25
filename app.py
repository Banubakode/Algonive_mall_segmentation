import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample Data
data = {
    'Category': ['Electronics', 'Clothing', 'Groceries', 'Books'],
    'Sales': [20000, 15000, 30000, 10000],
    'Profit': [5000, 4000, 7000, 2000]
}
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server

# Pie Chart
fig_pie = px.pie(df, names='Category', values='Sales', title='Sales Distribution')

# Bar Graph
fig_bar = px.bar(df, x='Category', y='Sales', title='Sales by Category', text='Sales')

# Layout
app.layout = html.Div(style={'font-family': 'Arial, sans-serif', 'margin': '40px'}, children=[
    
    html.H1("Professional Dashboard", style={'text-align': 'center'}),
    
    # Summary Section
    html.Div([
        html.H3("Summary"),
        html.P(f"Total Sales: {df['Sales'].sum():,.0f}"),
        html.P(f"Total Profit: {df['Profit'].sum():,.0f}"),
        html.P(f"Top Category: {df.loc[df['Sales'].idxmax(), 'Category']}")
    ], style={'border': '1px solid #ccc', 'padding': '20px', 'width': '30%', 'display': 'inline-block', 'vertical-align': 'top'}),
    
    # Graph Section
    html.Div([
        dcc.Graph(figure=fig_bar)
    ], style={'width': '65%', 'display': 'inline-block', 'padding-left': '30px'}),
    
    # Pie Chart Section
    html.Div([
        dcc.Graph(figure=fig_pie)
    ], style={'width': '50%', 'padding-top': '50px'})
])

if __name__ == '__main__':
    app.run_server(debug=True)
