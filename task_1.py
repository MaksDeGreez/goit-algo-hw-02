import queue
import random
import time

def generate_request(requests_queue):
    request_id = random.randint(1000, 10_000)
    request_body = f"Request {request_id}"
    requests_queue.put(request_body)
    print(f"Generated: {request_body}")

def process_request(requests_queue):
    if not requests_queue.empty():
        request = requests_queue.get()
        print(f"Processing: {request}")
    else:
        print("Queue is empty, no requests to process.")

def main():
    requests_queue = queue.Queue()
    try:
        while True:
            generate_request(requests_queue)
            time.sleep(random.uniform(0.5, 1.5))
            process_request(requests_queue)
            time.sleep(random.uniform(0.5, 1.5))
    except KeyboardInterrupt:
        print("\nProgram stopped by the user.")

if __name__ == "__main__":
    main()
