# coding:utf-8

import math


# Определяем функцию, считающую расстояние между двумя точками, заданными координатами
def lonlat_distance(a, b):
    # длина дуги меридиана в 1 градус в метрах
    degree_to_meters_factor = 111 * 1000  # 111 километров в метрах
    a_lon, a_lat = a  # широта и долгота 1-й точки
    b_lon, b_lat = b  # широта и долгота 2-й точки

    # Берем среднюю по широте точку и считаем коэффициент для нее.
    # угол в радианах для средней точки по широте
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    # косинус угла для средней точки
    lat_lon_factor = math.cos(radians_lattitude)

    # Вычисляем смещения в метрах по вертикали и горизонтали.
    # чем больше широта, тем меньше метров будет приходиться на 1 метр по долготе
    # разницу в градусах по долготе умножаем на косинус угла
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    # разницу в градусах по широте умножаем на кол-во метров в 1 градусе
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)

    return distance