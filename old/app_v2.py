import yfinance as yf
import gradio as gr

def get_stock_data(stock_symbol, start_date, end_date):
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    return stock_data.head().to_html(index=True)  # Convert to HTML for display in Gradio

# Create a Gradio interface
iface = gr.Interface(
fn=get_stock_data,
inputs=[
    gr.Textbox(label="Stock Symbol (e.g., AAPL)", value="AAPL"),
    gr.Textbox(label="Start Date (YYYY-MM-DD)", value="2022-01-01"),
    gr.Textbox(label="End Date (YYYY-MM-DD)", value="2023-01-01")
    ],
    outputs=gr.HTML(),
    title="Yahoo Finance Data Downloader",
    description="Download historical stock data using Yahoo Finance API."
)

# Launch the interface
iface.launch()