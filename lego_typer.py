import time
import threading
from pynput.keyboard import Key, Listener
import pygame

# Initialize the audio mixer
pygame.mixer.init()

# Load the sound files
sound_build = pygame.mixer.Sound("lego_build.wav")
sound_complete = pygame.mixer.Sound("lego_complete.wav")
sound_delete = pygame.mixer.Sound("Lego_Break.wav")

is_typing = False
last_key_time = 0
block_end_time = 0
delete_end_time = 0
complete_end_time = 0
TYPING_TIMEOUT = 0.4  # Seconds of silence before the build sound stops


def check_typing_status():
    global is_typing
    while True:
        time.sleep(0.1)
        if is_typing and (time.time() - last_key_time > TYPING_TIMEOUT):
            sound_build.stop()
            is_typing = False


# Start the background monitor thread
monitor_thread = threading.Thread(target=check_typing_status, daemon=True)
monitor_thread.start()


def on_press(key):
    global is_typing, last_key_time, block_end_time, delete_end_time, complete_end_time

    current_time = time.time()
    last_key_time = current_time

    try:
        # Enter or Period pressed
        if key == Key.enter or (hasattr(key, 'char') and key.char == '.'):
            sound_build.stop()
            sound_delete.stop()
            is_typing = False
            # Only play if the complete sound has finished
            if current_time > complete_end_time:
                complete_end_time = current_time + sound_complete.get_length()
                sound_complete.play()
                block_end_time = current_time + sound_complete.get_length()


        # Backspace or Delete pressed
        elif key in (Key.backspace, Key.delete):
            sound_build.stop()
            is_typing = False
            # Only play if the delete sound has finished
            if current_time > delete_end_time:
                sound_delete.play()
                delete_end_time = current_time + sound_delete.get_length()
                block_end_time = delete_end_time

        # Any other key pressed
        else:
            # Only start the build sound if no blocking sound is playing
            if current_time > block_end_time:
                if not is_typing:
                    is_typing = True
                    sound_build.play(loops=-1)
    except Exception:
        pass


# Start the global keyboard listener
with Listener(on_press=on_press) as listener:
    listener.join()