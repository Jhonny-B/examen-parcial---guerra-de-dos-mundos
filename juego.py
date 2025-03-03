import pygame, sys
pygame.init()

# variables con las medidas de la ventana
ventana = (800, 600)

#creación de la ventana
screen = pygame.display.set_mode(ventana)

# cambiamos el nombre de la ventana
pygame.display.set_caption("INVACIÓN")

# agregamos la imagen de fonde de la ventana
fondo = pygame.image.load("Espacio.jpg")

# posicion de la imagen
screen.blit(fondo, (0 ,0))
pygame.display.flip()


# creamos el bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

pygame.quit()
