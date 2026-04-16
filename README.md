# Lego Typer

A background Python script that plays Lego sound effects as you type in any application. 

## Features
* Plays a continuous Lego building sound while you type.
* Plays a completion sound when you press `Enter` or `.`.
* Plays a delete sound when you press `Backspace` or `Delete`.
* Automatically mutes the building loops during completion or delete sounds to prevent overlapping.

## Prerequisites
* Python 3
* `pynput`
* `pygame`

## Setup
1. **Prepare your directory:** Create a new folder for this project and place your python script (`lego_typer.py`) inside it.
2. **Install dependencies:** Open your terminal and install the required libraries:
   `pip install pynput pygame`
3. **Add audio files:** Place your `.wav` sound files in the same directory as the script. They must be exactly named:
   * `lego_build.wav`
   * `lego_complete.wav`
   * `lego_delete.wav`
4. **Run the script:** Execute the program from your terminal:
   `python lego_typer.py`
5. **Stop execution:** Press `Ctrl+C` in your terminal to terminate the background listener.
