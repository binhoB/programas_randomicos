'''
Created on 18/10/2011

@author: FABIO
'''

import pygame;
from pygame.locals import *;
from sys import exit;

pygame.init();

tabuleiro = pygame.display.set_mode((320,320),0,32); #desenho do tabuleiro

#convertendo as escalas dividindo por 8 (numero de quadradinhos)

tam = int(tabuleiro.get_width()/8);
raioBolinha = int(tabuleiro.get_width()/24); 
selecionado = False;
corBranco = (255,255,255);
corPreto = (0,0,0);
vermelho = (255,0,0);
amarelo = (255,0,255);

cenario = [
           [1,0,1,0,1,0,1,0], 
           [0,1,0,1,0,1,0,1],
           [1,0,1,0,1,0,1,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,2,0,2,0,2,0,2],
           [2,0,2,0,2,0,2,0],
           [0,2,0,2,0,2,0,2]  
           ];
           
def fazerJogada(x1,x2,y1,y2):
    if(testarJogada()):
        cenario[y2][x2],cenario[y1][x1] = cenario[y1][x1],0;
def testarJogada():
    return False;
def criarPecas():
    global cenario;
    for x in xrange(8):
        for y in xrange(8):
            if(cenario[y][x] == 1): pygame.draw.circle(tabuleiro, vermelho, ((tam * x) + (tam/2),(tam * y) + (tam/2)), raioBolinha);
            elif(cenario[y][x] == 2): pygame.draw.circle(tabuleiro, amarelo, ((tam * x) + (tam/2),(tam * y) + (tam/2)), raioBolinha);
def criarTabuleiro():
    global branco;            
    for x in xrange(8):
        for y in xrange(8):
            if((x+y)%2 == 0):
                pygame.draw.rect(tabuleiro, (255,255,255), Rect((tam * x, tam * y), (tam, tam)), 0);
            else:
                pygame.draw.rect(tabuleiro, (0,0,0) ,Rect((tam * x, tam * y), (tam, tam)), 0);
    criarPecas();

while True:
    criarTabuleiro();
    pygame.display.update();
    for e in pygame.event.get():
        if e.type == QUIT:
            exit();
        if e.type == MOUSEBUTTONDOWN:
            if (selecionado == False):
                x1,y1 = e.pos;
                print x1/tam,y1/tam;
                selecionado = True;
            else:
                x2,y2 = e.pos;
                fazerJogada((x1/tam),(x2/tam),(y1/tam),(y2/tam));
                selecionado = False;