# Problem5 - Create a Script to Monitor Disk Usage

### Create a Python script to monitor disk usage on a system and alert if usage exceeds a certain threshold.

# Solution5 - Creating a Script to Monitor Disk Usage
``` python

import shutil

def monitor_disk_usage(disk, threshold):
    total, used, free = shutil.disk_usage(disk)
    usage_percentage = (used / total) * 100
    
    return usage_percentage > threshold, usage_percentage

def main():
    disk = "E:/"
    threshold = 80
    
    alert, usage_percentage = monitor_disk_usage(disk, threshold)
    
    if alert: 
        print(f"Warning: Disk usage on {disk} has reached {usage_percentage:.2f}%. ")
    
    else:
         print(f"Disk usage on {disk} is under control at {usage_percentage:.2f}%.")
         
if __name__ == "__main__":
    main()

```