![Logo](heart.png)
# Animedoro
Pomodoro timer but for anime fans.  
Or simply for those who preferer 40 minutes work and 20 minutes break.  

Made for Angela Yu's 100 days of code challenge

Animedoro is a Pomodoro-style productivity timer application built with Python's `tkinter` library.
It helps you manage work sessions and breaks with a customizable timer. This app includes features like:

- Work sessions (default: 40 minutes)
- Short breaks (default: 20 minutes)
- Long breaks (default: 20 minutes)
- Bonus "Episode" mode after 8 work sessions
- Visual check marks to track completed work sessions

## Features

- **Work Timer**: Work for a set duration (default: 40 minutes).
- **Break Timer**: Short breaks after every work session and long breaks after every 4 work sessions.
- **Visual Feedback**: Track completed work sessions with 🍡 check marks.
- **Customizable Timings**: Easily adjust the work and break durations by modifying constants in the code.
- **Reset Function**: Reset the timer and clear the check marks.

## Requirements

- Python 3.x
- `tkinter` (which comes pre-installed with Python)
- A heart image (`heart.png`) for the background.

## Setup

1. Download or clone the repository to your local machine.
2. Place the `heart.png` image file in the same directory as the script.
3. Run the script:

   ```bash
   python animedoro_timer.py
   ```

## How it Works

- **Start**: Click the "Start" button to begin a work session. The timer will countdown from the set work duration.
- **Breaks**: After each work session, the app will automatically switch to a short break or long break, depending on the session count.
- **Reset**: Click the "Reset" button to stop the timer and reset the session counter.

## Code Walkthrough

### Constants
The following constants define the durations for work sessions and breaks:
- `WORK_MIN`: Duration of a work session in minutes (default: 40 minutes).
- `SHORT_BREAK_MIN`: Duration of a short break in minutes (default: 20 minutes).
- `LONG_BREAK_MIN`: Duration of a long break in minutes (default: 20 minutes).
- `REPS`: Keeps track of the number of completed work and break sessions.

### Functions

#### `reset_timer()`
This function stops the timer, resets the countdown to "00:00", and clears the check marks for completed sessions.

#### `start_timer()`
Starts the countdown based on the current session type:
- Work session: 40 minutes
- Short break: 20 minutes
- Long break: 20 minutes

#### `count_down(count)`
Handles the countdown process by updating the UI every second. Once the countdown reaches 0, the next session starts, and check marks are updated based on completed work sessions.

### UI Setup

The user interface is built using `tkinter`, with:
- A title label displaying the current session (Work, Episode, or Bonus).
- A canvas displaying the timer countdown.
- Buttons for starting and resetting the timer.
- A label to show completed work sessions using 🍡 symbols.

## Customization

You can customize the work, short break, and long break durations by modifying the following constants in the script:

```python
WORK_MIN = 40
SHORT_BREAK_MIN = 20
LONG_BREAK_MIN = 20
```

Additionally, feel free to replace the `heart.png` image with your own background image.

## License

This project is open source and available under the MIT License.

## Acknowledgements

- `tkinter` for the GUI library.
- Inspiration from the Pomodoro Technique for productivity.
