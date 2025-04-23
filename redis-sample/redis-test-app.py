import redis
import time
def main(iter):
    client = redis.Redis(host="10.225.117.83", port=6379)
    # Set a key-value pair
    if iter % 50 ==0:
        value_set = f"Rahul Raj Pandey {iter}"
        client.set("Name", value_set)
    # Get the value of a key
    value = client.get("Name")
    # Print the value
    print(value)


if __name__ == "__main__":
    iter=0
    while True:
        print(f"Starting new REDIS Iteration No. {iter}")
        try:
            main(iter)
        except Exception as e:
            print(e)
        iter+=1
        time.sleep(5)