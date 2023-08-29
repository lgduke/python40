import psutil

cpu = psutil.cpu_freq()
print(cpu)

cpu_core = psutil.cpu_count(logical=False)
print(cpu_core)