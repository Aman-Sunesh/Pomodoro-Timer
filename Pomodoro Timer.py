import time
import os
import sys

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the progress bar
def display_progress_bar(total_seconds, elapsed_seconds):
    bar_length = 30  # Length of the progress bar

    progress = int((elapsed_seconds / total_seconds) * bar_length)
    bar = '#' * progress + '-' * (bar_length - progress)
    percentage = (elapsed_seconds / total_seconds) * 100

    sys.stdout.write(f"\r[{bar}] {percentage:.2f}%")
    sys.stdout.flush()

# Pomodoro timer function
def pomodoro_timer(work_duration=25, short_break=5, long_break=20, cycles=4):
    clear_screen()

    print("Welcome to the Pomodoro Timer!\n")
    print(f"Work Duration: {work_duration} minutes")
    print(f"Short Break: {short_break} minutes")
    print(f"Long Break: {long_break} minutes")
    print(f"Cycles: {cycles}")

    input("\nPress Enter to start the timer...")

    for cycle in range(1, cycles + 1):
        # Work Session
        print(f"\nCycle {cycle}/{cycles} - Work Session")
        countdown(work_duration * 60)

        # Break Session
        if cycle < cycles:
            print("\nShort Break")
            countdown(short_break * 60)

        else:
            print("\nLong Break")
            countdown(long_break * 60)

    print("\nPomodoro Timer Completed! Great job!")

# Countdown function with progress bar
def countdown(total_seconds):
    for elapsed_seconds in range(total_seconds + 1):
        clear_screen()

        remaining_minutes, remaining_seconds = divmod(total_seconds - elapsed_seconds, 60)
        print(f"Time Remaining: {remaining_minutes:02}:{remaining_seconds:02}")

        display_progress_bar(total_seconds, elapsed_seconds)
        time.sleep(1)

# Run the Pomodoro Timer
if __name__ == "__main__":
    pomodoro_timer(work_duration=25, short_break=5, long_break=15, cycles=4)
