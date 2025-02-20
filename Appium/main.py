from rivian_map import appiumDistanceCheck
from api_test import getAPIDuration

startAddress = "607 Hansen Way, Palo Alto, CA"
endAddress = "Gray Whale Cove State Beach, Half Moon Bay, CA 94019, United States"

rivian_duration = appiumDistanceCheck(startAddress, endAddress)
print(f"Rivian Trip Duration: {rivian_duration}")
mins = rivian_duration.split(' ')
time_riv = int(mins[0])

api_duration = getAPIDuration(startAddress, endAddress)
print(f"API Trip Duration: {api_duration} min")

if abs(time_riv - api_duration)<=1:
    print("\nBoth API and Rivian App Durations Match!")
else:
    print("\nDiscrepancy detected! Rivian and API results do not match!")


