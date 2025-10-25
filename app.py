import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# ------------------------
# 1. Sample Data
# ------------------------
data = {
    'Category': ['Electronics', 'Clothing', 'Groceries', 'Books'],
    'Sales': [20000, 15000, 30000, 10000],
    'Profit': [5000, 4000, 7000, 2000]
}
df = pd.DataFrame(data)

# ------------------------
# 2. Initialize Dash app
# ------------------------
app = dash.Dash(__name__)
server = app.server   # Required for Render deployment

# ------------------------
# 3. Create Charts
# ------------------------
# Pie chart for sales distribution
fig_pie = px.pie(df, names='Category', values='Sales', title='Sales Distribution')

# Bar chart for sales
fig_bar = px.bar(df, x='Category', y='Sales', text='Sales', title='Sales by Category')

# ------------------------
# 4. Layout (Dashboard)
# ------------------------
app.layout = html.Div(style={'font-family': 'Arial, sans-serif', 'margin': '40px'}, children=[

    # Title
    html.H1("Simple Professional Dashboard", style={'text-align': 'center'}),

    # Summary section
    html.Div(style={'border': '1px solid #ccc', 'padding': '20px', 'width': '30%', 'display': 'inline-block', 'vertical-align': 'top'}, children=[
        html.H3("Summary"),
        html.P(f"Total Sales: ${df['Sales'].sum():,.0f}"),
        html.P(f"Total Profit: ${df['Profit'].sum():,.0f}"),
        html.P(f"Top Category: {df.loc[df['Sales'].idxmax(), 'Category']}")
    ]),

    # Bar chart
    html.Div(dcc.Graph(figure=fig_bar), style={'width': '65%', 'display': 'inline-block', 'padding-left': '30px'}),

    # Pie chart below
    html.Div(dcc.Graph(figure=fig_pie), style={'width': '50%', 'padding-top': '50px'})
])

# ------------------------
# 5. Run the app (local debug)
# ------------------------
if __name__ == '__main__':
    app.run_server(debug=True)

