# 向哲煜  2024.4.6

def get_formatted_city_location(city, country, population = ''):
    """返回格式化的城市位置"""
    location = f"{city}, {country}"
    return location.title()