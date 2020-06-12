import psutil
import time

time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(psutil.boot_time()))