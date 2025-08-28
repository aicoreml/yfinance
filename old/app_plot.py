import yfinance as yf
import matplotlib.pyplot as plt
import gradio as gr

# Function that plots the data and returns the plot
def plot_stock(ticker="AAPL", start_date="2022-01-01", end_date="2023-01-01"):
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Closing Price', color='blue')
    plt.title(f"{ticker} Stock Closing Prices ({start_date[:4]}-{end_date[:4]})")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)

    # Save the plot to a file for Gradio to display
    img_path = "plot.png"
    plt.savefig(img_path, bbox_inches='tight')
    return img_path

# Create a Gradio interface with input parameters and the plotting function
demo = gr.Interface(
    fn=plot_stock,
    inputs=[
        gr.Textbox(label="Ticker", value="TSLA"),
        gr.Textbox(label="Start Date (YYYY-MM-DD)", value="2025-01-01"),
        gr.Textbox(label="End Date (YYYY-MM-DD)", value="2025-03-12")
    ],
    outputs=gr.Image(type='filepath')
)

# Launch the interface
demo.launch()