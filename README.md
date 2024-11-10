

---

# Spread Bet Pairs Trade Calculator

A simple Python Tkinter application to help balance pairs trades in spread betting. The calculator determines the stake per point needed on two ETFs (or other assets) to ensure equal monetary exposure for each asset, based on their prices. The minimum stake for the second ETF can be adjusted, making it suitable for different trading scenarios.

## Features

- Calculates the required stake per point on ETF1 to balance with ETF2.
- Allows customization of the minimum stake per point for ETF2 (default is £1).
- Easy-to-use graphical interface with a dark theme.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/spread-bet-pairs-calculator.git
   cd spread-bet-pairs-calculator
   ```

2. **Install the required dependencies**:
   This application only requires Python’s built-in Tkinter library, so no additional installations are needed if you have Python and Tkinter.

3. **Run the application**:
   ```bash
   python pairs_trade_calculator.py
   ```

   > **Note**: This app is designed to run on Linux but will work on any platform that supports Python and Tkinter.

## Usage

1. Enter the **Price per Share** for ETF1 in the first input field.
2. Enter the **Price per Share** for ETF2 in the second input field.
3. Specify the **Minimum Stake for ETF2** in the third field (e.g., £1, £5, £10).
4. Click the **Calculate** button.

The result will display the required stake per point for ETF1 and the specified minimum stake per point for ETF2 to ensure equal monetary exposure.

### Example

- **ETF1 Price per Share**: 2682
- **ETF2 Price per Share**: 5681
- **Minimum Stake for ETF2**: £5

Clicking **Calculate** will display:
```
To balance:
ETF1 stake per point = £10.59
ETF2 stake per point = £5.00
```

This means you need £10.59 per point on ETF1 to match the monetary exposure of £5 per point on ETF2.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve this project.

