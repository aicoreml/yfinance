import yfinance as yf
import gradio as gr
import matplotlib.pyplot as plt
from io import BytesIO

def get_stock_data(stock_symbol, start_date, end_date):
    # Download historical data for the specified stock symbol
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Display the first few rows of the DataFrame in HTML format
    html_output = stock_data.head().to_html(index=True)

    return html_output

def plot_stock_data(html_output, stock_symbol, start_date, end_date):
    # Parse the HTML table to get data (if needed for plotting)
    import pandas as pd
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Plot the closing prices
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Closing Price', color='blue')
    plt.title(f'{stock_symbol} Stock Closing Prices ({start_date[:4]}-{end_date[:4]})')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)

    # Save the plot to a buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return buf
	
# Add a separate function for plotting
def plot_button_click(stock_symbol, start_date, end_date):
    html_output = get_stock_data(stock_symbol, start_date, end_date)
    plot_image = plot_stock_data(html_output, stock_symbol, start_date, end_date)
    return plot_image
	
# Create a Gradio interface
iface = gr.Interface(
    fn=get_stock_data,
    inputs=[
        gr.Textbox(label="Stock Symbol (e.g., AAPL)", value="AAPL"),
        gr.Textbox(label="Start Date (YYYY-MM-DD)", value="2022-01-01"),
        gr.Textbox(label="End Date (YYYY-MM-DD)", value="2023-01-01")
    ],
    outputs=[
        "html",  # HTML table
        gr.image(plot_image)  
    ],
    title="Yahoo Finance Data Downloader",
    description="Download historical stock data using Yahoo Finance API and display the closing prices."
)



iface.launch()