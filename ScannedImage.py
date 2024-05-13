import pygame.camera

def getCameras():
    pygame.camera.init()
    camlist = pygame.camera.list_cameras()
    return camlist

