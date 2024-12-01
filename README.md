# Simple Azimuth Converter - README

## Introduction
Do you have a problem such as:

- **Should I add or subtract 6 degrees when taking azimuth from a map and setting it on a compass?**
- **When a commander tells you "You should walk towards 90° azimuth," should you add or subtract 6 degrees to navigate correctly on a map?**

Here's a simple rule of thumb:
- **Taking off the map? Subtract 6°.**
- **Putting on the map from a compass reading? Add 6°.**

This simple Dash app solves this confusion effortlessly. It allows you to quickly convert **topographic azimuths to magnetic azimuths** and vice versa, specific to the **UTM MGRS grid's 34UDE quadrant (100km x 100km)** for the year **2025**. 

> **Warning:** The declination changes based on location and time. This app is valid **only for the Olsztyn area in 2025**. Do not use it for other locations or years.

---

## App Description
This app has two main functionalities:
1. **Convert a topographic azimuth to a magnetic azimuth** by subtracting 6°.
2. **Convert a magnetic azimuth to a topographic azimuth** by adding 6°.

The app features a clean, intuitive **military-themed interface** and a responsive design that adapts to vertical screens. It demonstrates the **author's proficiency in Dash development**, including working with:
- `dcc` (Dash Core Components)
- `html` (Dash HTML Components)
- `Input`, `Output`, and `State` objects for interactive callback functionality.

This app is for **educational purposes only**.

---

## Features
- **Column Layout**: Inputs, labels, and outputs are well-organized for ease of use.
- **Military-Themed Design**: The app uses a dark background with vibrant colors for clear visibility.
- **Dynamic Calculations**: Automatically updates the result when inputs change.
- **Instructions Displayed**: Includes a helpful message to remind users of the calculation logic.

---

## How to Run the App
1. Clone the repository:
   ```bash
   git clone https://github.com/andy111223/11.2_Dash_Simple_Azimuth_Converter.git
   cd 11.2_Dash_Simple_Azimuth_Converter
   ```
2. Install the required dependencies:
   ```bash
   pip install dash
   ```
   Ensure you are using **Python 3.12.3** and **Dash 2.18.2**.

3. Run the app:
   ```bash
   python app.py
   ```

4. Open the app in your browser at:
   ```
   http://127.0.0.1:8050/
   ```
   If the default port is unavailable, you can specify a different port like so:
   ```python
   app.run_server(port=8051)
   ```

---

## Dependencies
- **Python**: 3.12.3
- **Dash**: 2.18.2

---

## Code Overview
### Libraries and Methods Used
- **Dash Components**:
  - `dcc.Input`: For user input fields.
  - `html.Div`, `html.H2`, and `html.Label`: For layout and styling.
- **Callback Functionality**:
  - `Input`, `Output`, and `State` objects: Used to handle dynamic interaction between components.
  - `dash.callback_context`: To identify which input triggered the callback.

---

## Author's Notes
This app showcases the author's ability to:
- Build a responsive and visually appealing Dash application.
- Implement interactive functionality using Dash Core Components and HTML Components.
- Use callback functions effectively with `Input`, `Output`, and `State`.

This app is for **educational purposes only**. It demonstrates how declination corrections are applied for a specific area and time. It should not be used for navigation outside the valid grid area or year.

Enjoy using the **Simple Azimuth Converter**!