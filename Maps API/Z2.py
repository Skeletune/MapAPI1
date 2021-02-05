import os
import sys
import pygame
from Samples.geocoder import get_coordinates, get_ll_span
from Samples.mapapi_PG import show_map


def main():
    toponym_to_find = " ".join(sys.argv[1:])
    if toponym_to_find:
        zoom = 15
        lat, lon = get_coordinates(toponym_to_find)
        ll_spn = f'll={lat},{lon}&z={zoom}'
        point_param = f'pt={lat},{lon}'
        show_map(ll_spn, 'map', point_param)
    else:
        print('Нет данных для поиска')
    map_file = 'map.png'
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_PAGEUP:
                    zoom += 1
                    if zoom >= 23:
                        zoom = 23
                if event.key == pygame.K_PAGEDOWN:
                    zoom -= 1
                    if zoom <= 1:
                        zoom = 1
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 4:
                    zoom += 1
                    if zoom >= 23:
                        zoom = 23
                if event.button == 5:
                    zoom -= 1
                    if zoom <= 1:
                        zoom = 1
        ll_spn = f'll={lat},{lon}&z={zoom}'
        point_param = f'pt={lat},{lon}'
        show_map(ll_spn, 'map', point_param)
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()
    os.remove(map_file)


if __name__ == '__main__':
    main()
