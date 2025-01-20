# Digital Hourglass

## Overview

The **Digital Hourglass** is a Python-based console application that simulates an hourglass. It visually displays sand grains falling from the top section to the bottom, based on a user-specified duration. The application includes interactive controls, sound effects, and dynamic text-based visualization, providing an engaging way to measure time.

## Prerequisites

Before running the **Digital Hourglass**, ensure the following:

- **Python 3.6 or higher** is installed on your system.
- Required Python libraries:
  - `colorama`: For colored console output.
  - `winsound`: For sound playback (Windows only).

### Install Required Libraries

To install the required libraries, run the following command:

```bash
pip install colorama
```

## Sound Files

Ensure the following sound files are available in the same directory as the script:

- **`time_up.wav`**: Played when the hourglass timer ends.
- **`flip_sound.wav`**: Played when the hourglass is reset.

## Usage

### Running the Application

1. Clone the repository or download the script file.
2. Run the script using Python:

   ```bash
   python digital_hourglass.py
   ```

## Input Duration

- Upon starting the application, you will be prompted to input the total duration (in seconds) for the hourglass.

## Interactive Controls

- **`R`**: Reset the hourglass and start again.
- **`E`**: Exit the application.

## Visual Output

- The console displays a dynamic hourglass with colored sand grains.
- The visualization updates in real-time as sand grains move from the top to the bottom.

## Sound Effects

- **Time's Up Sound**: A sound plays when the hourglass timer ends (`time_up.wav`).
- **Reset Sound**: A reset sound plays when the hourglass is flipped (`flip_sound.wav`).

## Features and Functionalities

### Interactive Hourglass
- Real-time simulation of sand grains falling.
- User-friendly controls for resetting and exiting.

### Customizable Duration
- Input the total time (in seconds) for the hourglass.
- The falling speed adjusts dynamically based on the specified duration.

### Sound Effects
- **Time's Up Sound**: Alerts the user when the hourglass empties.
- **Reset Sound**: Indicates the hourglass is flipped and reset.

### User-Friendly Controls
- Clear instructions displayed in the console.
- Simple keyboard inputs for interactive control.

### Dynamic Visualization
- Top and bottom sections of the hourglass are displayed as grids.
- Sand grains are represented using yellow dots (`.`) for clear visualization.

## Troubleshooting

### Missing Sound Files
- **Issue**: Sound files (`time_up.wav`, `flip_sound.wav`) are not found.
- **Solution**: Ensure the files are in the same directory as the script.

### Invalid Input
- **Issue**: Non-numeric or negative input for the duration causes errors.
- **Solution**: Enter a positive integer for the total duration.

### Display Issues
- **Issue**: The console display appears distorted.
- **Solution**: Ensure your terminal window is large enough to accommodate the hourglass display.

### Compatibility
- **Issue**: `winsound` is unavailable on non-Windows systems.
- **Solution**: Replace `winsound` with a cross-platform sound library like `playsound`.

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements or additional features. Whether it's enhancing the algorithm, optimizing performance, or adding new functionalities, your contributions are valuable.

---

## Acknowledgments

- **[Python Documentation](https://docs.python.org/3/)**: For providing comprehensive resources and guides on Python programming.
- **[Colorama Documentation](https://pypi.org/project/colorama/)**: For enabling colorful terminal text and cross-platform support.
- **Open Source Community**: For tools, libraries, and contributions that made this project possible.
