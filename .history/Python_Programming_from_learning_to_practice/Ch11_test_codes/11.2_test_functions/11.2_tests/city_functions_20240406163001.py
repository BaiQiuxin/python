# 向哲煜  2024.4.6

def get_formatted_city_location(city, country, population = 0):
    """返回格式化的城市位置"""
    if population:
        location = f"{city} {country}"
        location = location.title()
        location += f" - population {population}"
    else:
        location = f"{city}, {country}"
        location = loc
    return location