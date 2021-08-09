import pygame
import time
import random
from random import randrange

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
azul_claro = (0, 127, 255)

pygame.init()
largura = 600
altura = 600

FPS = 30

imagem = pygame.image.load('images/SkiFac.png')
icon = pygame.image.load('images/icon.png')


superficie = pygame.Surface((altura, largura))
fundo = pygame.display.set_mode((largura, altura))
fundo.blit(superficie, [altura, largura])
pygame.display.set_icon(icon)
pygame.display.set_caption("SKIFAC")

pygame.font.init()

clock = pygame.time.Clock()

sair = True
fimdojogo = True


class Jogador(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("images/skier_down.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def direita(self):
        self.rect.x += 40

    def esquerca(self):
        self.rect.x -= 40

class Livro(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("images/livro.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def subir(self):
        self.rect.y -= 3

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("images/corote.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def subir(self):
        self.rect.y -= 3

class Caixa(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("images/caixa.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def subir(self):
        self.rect.y -= 3


def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont('arial', tam)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x, y])



listalivro = pygame.sprite.Group()
listaobstaculo = pygame.sprite.Group()
listacaixa = pygame.sprite.Group()
listajogador = pygame.sprite.Group()
jogador = Jogador(300, 70)
listajogador.add(jogador)
livro = Livro(100, 600)
obstaculo = Obstaculo(400, 600)
caixa = Caixa(250, 600)
listacaixa.add(caixa)
listalivro.add(livro)
listaobstaculo.add(obstaculo)

pontos = 0
perguntas = 0
tempo = 0

def jogo():
    global sair
    global fimdojogo
    global pontos
    global perguntas
    global tempo
    global livro
    global caixa
    global obstaculo
    while sair:
        while fimdojogo:
            segundos = int(pygame.time.get_ticks() / 1000)  # TEMPO
            clock.tick(FPS)
            livro.subir()
            obstaculo.subir()
            caixa.subir()
            bateulivro = pygame.sprite.spritecollideany(jogador, listalivro)# TRATAMENTO DE COLISÃO
            bateuobstaculo = pygame.sprite.spritecollideany(jogador, listaobstaculo)
            bateucaixa = pygame.sprite.spritecollideany(jogador, listacaixa)
            if livro.rect.y <=0:
                fimdojogo = False
            if bateulivro != None:
                pontos+=10
                livro.kill()
                caixa.kill()
                obstaculo.kill()
                livro = Livro(100, 620)
                obstaculo = Obstaculo(400, 620)
                caixa = Caixa(250, 620)
                listacaixa.add(caixa)
                listalivro.add(livro)
                listaobstaculo.add(obstaculo)
                perguntas+=1
            if bateuobstaculo != None:
                pontos-=5
                livro.kill()
                caixa.kill()
                obstaculo.kill()
                livro = Livro(100, 600)
                obstaculo = Obstaculo(400, 600)
                caixa = Caixa(250, 600)
                listacaixa.add(caixa)
                listalivro.add(livro)
                listaobstaculo.add(obstaculo)
                perguntas+=1
            if bateucaixa != None:
                pontos+=0
                livro.kill()
                caixa.kill()
                obstaculo.kill()
                livro = Livro(100, 600)
                obstaculo = Obstaculo(400, 600)
                caixa = Caixa(250, 600)
                listacaixa.add(caixa)
                listalivro.add(livro)
                listaobstaculo.add(obstaculo)
                perguntas+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #SAIR DO JOGO
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    tecla = pygame.key.get_pressed()
                    if tecla[pygame.K_RIGHT]:
                        jogador.direita()
                    if event.key == pygame.K_LEFT:
                        jogador.esquerca()
            fundo.fill(branco) # PREENCHER FUNDO
            listalivro.draw(fundo)
            listacaixa.draw(fundo)
            listaobstaculo.draw(fundo)
            listajogador.draw(fundo)
            if(perguntas==0):
                texto("Simbolo usado para iniciar uma lista:",preto, 30, 10, 10)
                texto(" [ ] ",preto,20,livro.rect.x,livro.rect.y)
                texto(" ( ) ",preto,20,obstaculo.rect.x,obstaculo.rect.y)
            elif(perguntas==1):
                texto("1.5 é qual tipo de básico de variável:",preto, 30, 10, 10)
                texto(" float ",preto,20,livro.rect.x,livro.rect.y)
                texto(" integer ",preto,20,obstaculo.rect.x,obstaculo.rect.y)
            elif(perguntas==2):
                texto("“Programação” com o método “upper”:",preto, 30, 10, 10)
                texto(" PROGRAMAÇÃO ",preto,15,livro.rect.x,livro.rect.y)
                texto(" programação ",preto,20,obstaculo.rect.x,obstaculo.rect.y)
            elif(perguntas==3):
                texto("Usado para iniciar um loop:",preto, 30, 10, 10)
                texto(" while ",preto,20,livro.rect.x,livro.rect.y)
                texto(" else ",preto,20,obstaculo.rect.x,obstaculo.rect.y)
            elif(perguntas==4):
                texto("Sintaxe para começar uma função:",preto, 30, 10, 10)
                texto(" def ",preto,20,livro.rect.x,livro.rect.y)
                texto(" str  ",preto,20,obstaculo.rect.x,obstaculo.rect.y)
            texto("Pontos: " + str(pontos), preto, 20, 480, 10)
            texto("Tempo: " + str(segundos), preto, 20, 480, 40)
            pygame.display.update()
            listalivro.update()
            listacaixa.update()
            listaobstaculo.update()
            listajogador.update()
            if perguntas == 5:
                fimdojogo = False
        fundo.fill(branco)
        fundo.blit(imagem, (0, 0))
        texto("FIM :)", preto, 50, 250, 385)
        texto("Pontuação total: " + str(pontos), preto, 30, 193, 450)
        pygame.display.update()
        pygame.mixer.music.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # SAIR DO JOGO
                sair = False
                quit()

def imagem_fundo():
    fundo.blit(imagem, (0, 0))

def texto_objetos(texto,font):
    textSurface = font.render(texto, True, preto)
    return textSurface, textSurface.get_rect()

def texto_botao():
    texto = pygame.font.SysFont('arial', 20)
    textSurf, TextRect = texto_objetos(texto)
    fundo.blit(textSurf, TextRect)

def texto_sobre_fonte(texto):
    fonte = pygame.font.SysFont('arial', 40)
    textSurf, textRect = texto_objetos(texto, fonte)
    textRect.center = ((largura/2)),((altura/2))
    fundo.blit(textSurf, textRect)
def texto_sobre():
    texto_sobre_fonte('Objeto de Aprendizagem!')

def botao(msg,x,y,w,h,cor,cor_depois,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(fundo, cor_depois, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == 'jogar':
                pygame.mixer.music.stop()
                pygame.mixer.music.load("8bits2.mp3")
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play()
                jogo()
            elif action == 'sair':
                pygame.quit()
                quit()
            elif action == 'sobre':
                texto_sobre()
    else:
        pygame.draw.rect(fundo, cor, (x, y, w, h))

        fonte = pygame.font.SysFont('arial', 30)
        textSurf, textRect = texto_objetos(msg, fonte)
        textRect.center = ((x+(w / 2),y +(h / 2)))
        fundo.blit(textSurf, textRect)

def menu():
    pygame.mixer.music.load("menu.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            fundo.blit(superficie, [altura, largura])
        imagem_fundo()
        botao('Jogar', 130, 450, 100, 50, branco, azul_claro,'jogar')
        botao('Sair', 350, 450, 100, 50, branco, azul_claro,'sair')
        botao('Sobre',240, 530, 100, 50, branco, azul_claro,'sobre')

        pygame.display.update()
        #clock.tick(60)
menu()
