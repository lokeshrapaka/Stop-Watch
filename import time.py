import time
import threading

def stopwatch():
    input("Press Enter to start the stopwatch.")
    start_time = time.time()
    running = True

    def wait_for_enter():
        nonlocal running
        input()
        running = False

    print("Stopwatch started! Press Enter to stop.")
    threading.Thread(target=wait_for_enter, daemon=True).start()

    while running:
        elapsed = time.time() - start_time
        print(f"\rElapsed time: {elapsed:.2f} seconds", end="")
        time.sleep(0.1)

    print(f"\nStopwatch stopped at {elapsed:.2f} seconds.")

stopwatch()

