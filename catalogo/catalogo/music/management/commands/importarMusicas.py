# coding: utf-8

from django.core.management.base import BaseCommand, CommandError
from catalogo.music.models import *

import os, sys

class Command(BaseCommand):
    args = '<diretório a ser utilizado>'
    help = 'Varrer um diretório e adicionar artistas, albuns e músicas encontradas'
    
    def handle(self, *args, **options):
        if len(args) == 0:
            raise CommandError('Informe o diretório a ser utilizado')
            
        diretorio = args[0]
                        
#        for artista in os.listdir(diretorio):
#            banda = Artist(name=artista.decode('utf-8'))
#            self.stdout.write(banda.name)
#            banda.save()
        for raiz, pastas, arquivos in os.walk(diretorio):
            artista = raiz.split('/')
            if pastas:
                artista = artista[-1].decode('utf-8')
                albuns = [pasta for pasta in pastas if pasta.find('-') > -1]
            print artista, albuns
"""
            if len(pastas) > 0:
                albuns = [pasta for pasta in pastas if pasta.find('-') > -1]

            if albuns and arquivos:
                print raiz
                print albuns[0]
                del albuns[0]
                #print arquivos
                                    
            faixas = []
            print arquivos
            if arquivos and albuns:
                faixas = [faixa for faixa in arquivos if len(faixa) > 0 and faixa.find('.mp3') > -1]
                if faixas:
                    print albuns[0]
                    del albuns[0]
                    print faixas
                break

            for disco in albuns:
                if len(faixas) > 0:
                    #faixas = [faixa for faixa in arquivos]
                    print disco
                    print faixas, '\n'
            albuns = [pasta for pasta in pastas if pasta.find('-') > -1]
            for disco in albuns:
                album = Album()
                album.artist = banda
                album.year = disco.split('-')[0].strip()
                album.name = '-'.join(disco.split('-')[1:])
                album.save()
                for faixa in faixas:
                    song = Song()
                    song.album = album
                    song.number = faixa.split('-')[0].strip()
                    song.name = '-'.join(faixa.split('-')[1].strip())
                    print song.name
                    song.save()
                    #self.stdout.write(arquivo)
"""                        
