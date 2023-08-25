from geopy import GoogleV3
print('Введите адрес')

place = input()
location = GoogleV3(api_key="AIzaSyADkvCte0y4cAKgkARaTnh_mI1ybcIEecU", domain = 'maps.google.ru').geocode(place)

print(location.address)
print(location.latitude, location.longitude)