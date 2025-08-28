# Stock Market Data Visualizer with YFinance

This project provides interactive web applications for visualizing stock market data using Yahoo Finance API. It includes two different implementations:

1. **Line Chart Visualization** (`app_plot_gradio.py`) - Displays closing prices over time
2. **Candlestick Chart Visualization** (`app_plot_candle_stick_gradio.py`) - Displays detailed OHLC (Open, High, Low, Close) data

## Features

- Interactive web interface built with Gradio
- Real-time stock data from Yahoo Finance
- Customizable date ranges
- Support for any stock ticker symbol
- Two visualization types:
  - Simple line chart of closing prices
  - Detailed candlestick charts

## Requirements

- Python 3.7 or higher
- Yahoo Finance API access
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run either of the applications:
   ```
   python app_plot_gradio.py
   ```
   or
   ```
   python app_plot_candle_stick_gradio.py
   ```

2. Open your web browser and go to the URL provided in the terminal (typically `http://localhost:7860`)

3. Enter a stock ticker symbol (e.g., AAPL for Apple, GOOGL for Google) and date range

4. Click "Submit" to generate the visualization

## Files

- `app_plot_gradio.py` - Line chart visualization of stock closing prices
- `app_plot_candle_stick_gradio.py` - Candlestick chart visualization
- `requirements.txt` - List of required Python packages
- `plot.png` - Sample output from the line chart app
- `Visualizing Stock Market Data with YFinance and Python.pdf` - Related documentation

## Development

The `old/` directory contains earlier versions of the application during development.

## License

This project is open source and available under the MIT License.