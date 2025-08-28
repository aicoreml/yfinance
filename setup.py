from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="stock-market-visualizer",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for visualizing stock market data with YFinance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/stock-market-visualizer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "stock-line-chart=app_plot_gradio:demo.launch",
            "stock-candlestick=app_plot_candle_stick_gradio:demo.launch",
        ],
    },
)