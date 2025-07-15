import psutil
import time
from datadog import initialize, statsd

options = {
    'api_key': 'API_KEY_HERE',
    'app_key': 'APP_KEY_HERE',
    'statsd_host': '127.0.0.1',
    'statsd_port': 8125,
    'telemetry_enable': False
}
initialize(**options)

def monitor_system(threshold_cpu=80, threshold_mem=80, interval=5):
    while True:
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        
        # Simulate e-commerce load
        for _ in range(1000000): pass
        
        statsd.gauge('system.cpu.usage', cpu, tags=['env:prod'])
        statsd.gauge('system.mem.usage', mem, tags=['env:prod'])
        print(f"Sending metrics: CPU {cpu}%, Mem {mem}%")
        
        if cpu > threshold_cpu:
            print(f"ALERT: CPU high at {cpu}% - potential outage")
            statsd.event('High CPU Alert', 'CPU exceeded threshold', alert_type='warning')
        if mem > threshold_mem:
            print(f"ALERT: Memory high at {mem}% - service degradation")
            statsd.event('High Memory Alert', 'Memory exceeded threshold', alert_type='warning')
        
        time.sleep(interval)

monitor_system()