time_in_hour = int(input())
spreed_per_hour = int(input())
distance = time_in_hour * spreed_per_hour

car_distance_km_per_liter = 12
total_liters_need = distance / car_distance_km_per_liter

print(f"{total_liters_need:.3f}")