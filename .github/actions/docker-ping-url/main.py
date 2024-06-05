import os
import time
import requests

def ping_url(url, delay, max_trials):
    trials = 0
    while trials < max_trials:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
        except requests.RequestException as e:
            print(f"Request failed: {e}")
        time.sleep(delay)
        trials += 1
    return False

def run():
    url = os.getenv('INPUT_URL')
    delay_str = os.getenv('INPUT_DELAY', '5')
    max_trials_str = os.getenv('INPUT_MAX_TRIALS', '3')
    
    if not delay_str:
        delay_str = '5'
    if not max_trials_str:
        max_trials_str = '3'

    delay = int(delay_str)
    max_trials = int(max_trials_str)

    if not url:
        raise ValueError("URL input is required.")

    success = ping_url(url, delay, max_trials)
    if not success:
        raise Exception(f"Failed to ping {url} after {max_trials} attempts.")
    
if __name__ == "__main__":
    run()



#if __name__ == "__main__":
    #print("Hello world")
