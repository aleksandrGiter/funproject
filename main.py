import pygame

done = False

screen = pygame.display.set_mode((1280, 720))

objects = []
palitra = []
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238), (0,0,0)]
selectedcolor = (0,0,0)
selectedradius = 5
isdrawing = False

last_pos = pygame.mouse.get_pos()

for i in range(0, len(colors)):
    palitra.append([pygame.Rect(100*i,620,100,100), colors[i], 80])

def roundline(pos1, pos2, color, radius):
    pygame.draw.line(screen, color, pos1, pos2, radius*2+1)
    pygame.draw.circle(screen, color, pos1, radius)
    pygame.draw.circle(screen, color, pos2, radius)
while not done:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = True
        if i.type == pygame.MOUSEMOTION and isdrawing:
            objects.append([last_pos, pygame.mouse.get_pos(), selectedcolor, selectedradius])
            last_pos = pygame.mouse.get_pos()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if pygame.Rect(1180,620,100,100).collidepoint(pygame.mouse.get_pos()):
                    objects.clear()
                else:
                    last_pos = pygame.mouse.get_pos()
                    isdrawing = True
            elif i.button == 3:
                for yx in palitra:
                    if yx[0].collidepoint(pygame.mouse.get_pos()):
                        selectedcolor = yx[1]
        if i.type == pygame.MOUSEBUTTONUP:
            isdrawing = False
        if i.type == pygame.MOUSEWHEEL:
            if i.y == 1:
                selectedradius += 1
            elif i.y == -1:
                selectedradius -= 1
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, selectedcolor, pos, selectedradius)

    screen.fill((0,150,255))
    for i in objects:
        # pygame.draw.circle(screen, i[1], i[0], i[2])
        roundline(i[0], i[1], i[2], i[3])
    for i in palitra:
        pygame.draw.rect(screen, i[1], i[0])
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(1180,620,100,100))
    pygame.display.flip()

