import pygame
from network import Network

pygame.init()
winWidth = 500
winHeight = 500
WIN = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Shooter")
font = pygame.font.SysFont("comicsansms", 16)
players = [None, None]
is_winner = None


def redraw_window(win, _players):
    win.fill((232, 236, 241))
    # draw the player and bullet relative client
    for i in range(len(_players)):
        _players[i].draw(win)
        other_num = (i + 1) % 2
        if _players[i].is_fire:
            _players[i].bullet.draw(win)
            other_player = _players[other_num]
            if _players[i].bullet.is_collided_with(other_player):
                other_player.damaged()
        # rendering the font based on id (dir)
        if _players[i].pid == 1:
            actual_player = 1
            text = font.render('PLAYER{} HP: {} left'.format(actual_player, _players[other_num].health), True, (140, 20, 252))
            WIN.blit(text, (25, 20 - text.get_height()/2))
        else:
            actual_player = 2
            text = font.render('PLAYER{} HP: {} left'.format(actual_player, _players[other_num].health), True, (107, 185, 240))
            WIN.blit(text, (winWidth - (text.get_width() + 25), winHeight - 20 - text.get_height()/2))
        # check whois dead
        is_dead(_players[i], actual_player)
    pygame.display.update()


def is_dead(player, p_id):
    global is_winner
    if player.is_destroy and not is_winner:
        is_winner = p_id
    elif is_winner == p_id:
        player.color = (232, 236, 241)
        winner(is_winner)  # display winner text


def winner(id):
    font_win = pygame.font.SysFont("comicsansms", 40)
    text = font_win.render('PLAYER' + str(id) + ' WON!', True, (0, 0, 0))
    WIN.blit(text, (winWidth/2 - (text.get_width()/2), winHeight/2 - text.get_height()))


def main():
    run = True
    n = Network('localhost', 9901)
    players[0] = n.player()  # waiting for getting player object from server
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        players[1] = n.send(players[0])  # sending object player1 on index 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        players[0].update((0, winWidth))  # player bound screen: 0px to 500px
        redraw_window(WIN, players)


main()
