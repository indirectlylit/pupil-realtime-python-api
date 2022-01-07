from pupil_labs.realtime_api.basic import discover_one_device

# Look for devices. Returns as soon as it has found the first device.
print("Looking for the next best device...")
device = discover_one_device(max_search_duration_seconds=10)
if device is None:
    print("No device found.")
    raise SystemExit(-1)

try:
    while True:
        print(device.read_gaze_datum())
except KeyboardInterrupt:
    pass
finally:
    print("Stopping...")
    device.close()  # explicitly stop auto-update