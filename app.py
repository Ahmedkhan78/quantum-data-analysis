import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# --- Load Data ---
df = pd.read_csv("formatted_data.csv")

# Convert 'date' to datetime type for proper sorting
df['date'] = pd.to_datetime(df['date'])

# Sort by date
df = df.sort_values('date')

# --- Create Dash App ---
app = dash.Dash(__name__)
app.title = "Pink Morsel Sales Visualiser"

# --- Layout ---
app.layout = html.Div([
    html.H1("Pink Morsel Sales Over Time", style={'textAlign': 'center'}),
    
    html.P("This chart shows sales before and after the price increase on Jan 15, 2021.", 
           style={'textAlign': 'center'}),
    
    dcc.Graph(
        id='sales-line-chart',
        figure=px.line(
            df,
            x='date',
            y='sales',
            title='Pink Morsel Sales Over Time',
            labels={'sales': 'Total Sales', 'date': 'Date'}
        )
    )
])

# --- Run Server ---
if __name__ == '__main__':
    app.run(debug=True)