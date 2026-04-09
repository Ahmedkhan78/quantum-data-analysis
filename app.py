import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# --- Load Data ---
df = pd.read_csv("formatted_data.csv")  # or processed_sales.csv
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# --- Create Dash App ---
app = dash.Dash(__name__)
app.title = "Pink Morsel Sales Visualiser"

# --- Layout ---
app.layout = html.Div([
    html.H1("Pink Morsel Sales Over Time", style={'textAlign': 'center', 'color': '#2c3e50'}),
    
    html.P("Filter sales by region:", style={'textAlign': 'center', 'color': '#34495e'}),
    
    # Radio buttons for region selection
    dcc.RadioItems(
        id='region-selector',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',
        labelStyle={'display': 'inline-block', 'margin-right': '15px', 'font-weight': 'bold', 'color': '#2980b9'},
        inputStyle={"margin-right": "5px"}
    ),
    
    dcc.Graph(id='sales-line-chart')
], style={'font-family': 'Arial, sans-serif', 'padding': '20px', 'backgroundColor': '#ecf0f1'})

# --- Callback to update chart based on region ---
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'].str.lower() == selected_region.lower()]
    
    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title=f'Pink Morsel Sales Over Time ({selected_region.capitalize()})',
        labels={'sales': 'Total Sales', 'date': 'Date'}
    )
    
    fig.update_layout(
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ecf0f1',
        title_font_size=24,
        title_font_color='#2c3e50',
        xaxis_title='Date',
        yaxis_title='Sales'
    )
    
    return fig

# --- Run Server ---
if __name__ == '__main__':
    app.run(debug=True)