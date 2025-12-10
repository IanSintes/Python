import pygame
import random
import os

pygame.init()

pantalla_amplada = 800
pantalla_alçada = 600
pantalla = pygame.display.set_mode((pantalla_amplada, pantalla_alçada))
pygame.display.set_caption("Mini Arkanoid")

BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)

directori_actual = os.path.dirname(__file__)

barra_img = pygame.image.load(os.path.join(directori_actual, "barra.png"))
barra_amplada, barra_alçada = 100, 20
barra_img = pygame.transform.scale(barra_img, (barra_amplada, barra_alçada))
barra_x = pantalla_amplada // 2 - barra_amplada // 2
barra_y = pantalla_alçada - barra_alçada - 10
velocitat_barra = 7

pilota_img = pygame.image.load(os.path.join(directori_actual, "pilota.png"))
pilota_radius = 10
pilota_img = pygame.transform.scale(pilota_img, (pilota_radius*2, pilota_radius*2))
pilota_x = pantalla_amplada // 2
pilota_y = pantalla_alçada // 2
velocitat_pilota_x = 4 * random.choice([-1, 1])
velocitat_pilota_y = -4

bloc_img = pygame.image.load(os.path.join(directori_actual, "bloc.png"))
bloc_amplada, bloc_alçada = 70, 30
bloc_img = pygame.transform.scale(bloc_img, (bloc_amplada, bloc_alçada))
files_blocs = 5
col_blocs = 10
blocs = []
for fila in range(files_blocs):
    for col in range(col_blocs):
        bloc_x = col * (bloc_amplada + 5) + 35
        bloc_y = fila * (bloc_alçada + 5) + 50
        blocs.append(pygame.Rect(bloc_x, bloc_y, bloc_amplada, bloc_alçada))

rellotge = pygame.time.Clock()
FPS = 60
joc_actiu = True
joc_comenca = False  # La pilota no es mou fins pitjar barra

while joc_actiu:
    pantalla.fill(NEGRE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            joc_actiu = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                joc_comenca = True

    tecles = pygame.key.get_pressed()
    if tecles[pygame.K_LEFT]:
        barra_x -= velocitat_barra
    if tecles[pygame.K_RIGHT]:
        barra_x += velocitat_barra
    barra_x = max(0, min(barra_x, pantalla_amplada - barra_amplada))

    if joc_comenca:
        pilota_x += velocitat_pilota_x
        pilota_y += velocitat_pilota_y

        if pilota_x - pilota_radius <= 0 or pilota_x + pilota_radius >= pantalla_amplada:
            velocitat_pilota_x *= -1
        if pilota_y - pilota_radius <= 0:
            velocitat_pilota_y *= -1
        if pilota_y + pilota_radius >= pantalla_alçada:
            pilota_x = pantalla_amplada // 2
            pilota_y = pantalla_alçada // 2
            velocitat_pilota_y *= -1
            joc_comenca = False  # Espera altra vegada barra

        barra_rect = pygame.Rect(barra_x, barra_y, barra_amplada, barra_alçada)
        pilota_rect = pygame.Rect(pilota_x - pilota_radius, pilota_y - pilota_radius, pilota_radius*2, pilota_radius*2)
        if pilota_rect.colliderect(barra_rect):
            velocitat_pilota_y *= -1
            offset = (pilota_x - (barra_x + barra_amplada / 2)) / (barra_amplada / 2)
            velocitat_pilota_x = 5 * offset

        for bloc in blocs[:]:
            if pilota_rect.colliderect(bloc):
                blocs.remove(bloc)
                velocitat_pilota_y *= -1
                break

    pantalla.blit(barra_img, (barra_x, barra_y))
    pantalla.blit(pilota_img, (pilota_x - pilota_radius, pilota_y - pilota_radius))
    for bloc in blocs:
        pantalla.blit(bloc_img, (bloc.x, bloc.y))

    pygame.display.flip()
    rellotge.tick(FPS)

pygame.quit()
