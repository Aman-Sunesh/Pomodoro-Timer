# Pomodoro Timer

## Overview

The **Pomodoro Timer** is a Python-based terminal application designed to help you improve focus and productivity. It implements the Pomodoro Technique, alternating between work sessions and breaks. The application features a dynamic progress bar and a countdown timer for each session, making it easy to track your progress in real-time.

## Prerequisites

Ensure you have the following installed on your system:

- **Python 3.6 or higher**: Required to run the script.

## Installation

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/Aman-Sunesh/Pomodoro-Timer.git
cd Pomodoro-Timer
```

## 2. Run the Script
Execute the script using Python:

```bash
python "Pomodoro Timer.py"
```

## Usage

### Starting the Timer
1. Launch the script using the above command.
2. Enter the desired work duration, break durations, and number of cycles when prompted (default values are provided in the script.
3. Press `Enter` to start the timer.

### Timer Sessions
#### Work Session:
- Focused work for the specified duration.
- A countdown timer and progress bar will appear.

#### Short Break:
- A short break between work sessions.

#### Long Break:
- A longer break after completing all cycles.

### Completion
- Once all cycles are complete, the timer displays a congratulatory message.

---

## Features and Functionalities

1. **Dynamic Progress Bar**:
   - Visual progress bar dynamically updates in real-time, indicating the elapsed time.

2. **Real-Time Countdown**:
   - Displays the remaining time in `MM:SS` format for each session.

3. **Session Management**:
   - Tracks and alternates between work sessions, short breaks, and long breaks.
   - Customizable durations for each session and the number of cycles.

4. **User-Friendly Interface**:
   - Clear instructions and progress visualization.

5. **Cross-Platform Compatibility**:
   - Works on Windows, macOS, and Linux terminals.

---

## Customization

Modify the session durations and cycles by editing the parameters in the `pomodoro_timer` function at the bottom of the script:

```python
pomodoro_timer(work_duration=25, short_break=5, long_break=15, cycles=4)
```
- **work_duration**: Work session duration in minutes (default: 25).  
- **short_break**: Short break duration in minutes (default: 5).  
- **long_break**: Long break duration in minutes (default: 15).  
- **cycles**: Number of work-break cycles (default: 4).  

## Troubleshooting

### Script Not Running
- **Issue**: Python is not installed or not in the system's PATH.  
- **Solution**: Install Python 3.6 or higher and ensure it is added to your PATH.  

### Progress Bar or Countdown Issues
- **Issue**: Display issues in the terminal.  
- **Solution**: Resize the terminal window or ensure you are using a modern terminal emulator.  

### Customization Not Working
- **Issue**: Modifications to the script parameters are not applied.  
- **Solution**: Verify that the parameters are updated in the `pomodoro_timer` function call.  

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements or additional features. Suggestions for improving functionality, optimizing performance, or enhancing user experience are appreciated.

## Acknowledgments
- [Python Documentation](https://docs.python.org/3/)  
- Open Source Community: For tools and resources.
