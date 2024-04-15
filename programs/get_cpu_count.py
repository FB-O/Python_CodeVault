import os

def get_cpu_count():
    try:
        num_cores = os.cpu_count()
        if num_cores is None:
            return "Unable to determine the number of CPU cores."
        else:
            return num_cores
    except Exception as e:
        return f"Error occurred while getting CPU count: {e}"

if __name__ == "__main__":
    print("Number of CPU cores available:", get_cpu_count())
