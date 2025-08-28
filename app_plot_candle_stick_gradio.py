import yfinance as yf
import plotly.graph_objects as go
import gradio as gr
from datetime import datetime

end = datetime.now().strftime('%Y-%m-%d')  # End date is current date
tf = '1d'  # Time frame (daily)

# Function that plots the candlestick chart
def plot_candlestick(ticker="AAPL", start_date="2024-12-01", end_date="2024-12-31"):
    stock_data = yf.download(ticker, start=start_date, end=end_date, interval=tf)
    stock_data.columns = stock_data.columns.droplevel(1)
	
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=stock_data.index,
                open=stock_data['Open'],
                high=stock_data['High'],
                low=stock_data['Low'],
                close=stock_data['Close']
            )
        ]
    )


				  
    fig.update_layout(
        title=f"{ticker} Stock Candlestick Chart {start_date}-{end_date}",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        xaxis_rangeslider_visible=False
    )

    # Ensure the figure is properly returned
    return fig

# Create a Gradio interface with input parameters and the plotting function
demo = gr.Interface(
    fn=plot_candlestick, 

    inputs=[
        gr.Textbox(label="Ticker", value="AAPL"),
        gr.Textbox(label="Start Date (YYYY-MM-DD)", value="2024-03-01"),
        gr.Textbox(label="End Date (YYYY-MM-DD)", value="2024-03-14")
    ],
    outputs=['plot'],
    title="Stock Plot",
    description="{ticker} Stock Candlestick Chart ",
    #article="Test",
    
)

# Launch the interface
demo.launch()

