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

        for raiz, pastas, arquivos in os.walk(diretorio):
            artista = raiz.split('/')
            if pastas:
                artista = artista[-1].decode('utf-8')
                if len(artista.strip()) == 0:
                    continue
                    
                banda = Artist(name=artista)
                banda.save()
                print banda
                albuns = [pasta for pasta in pastas if pasta.find('-') > -1]

            if albuns and arquivos:
                disco = albuns[0]
                # Salva os albuns localizados
                album = Album()
                album.artist = banda
                album.year = disco.split('-')[0].strip()
                album.name = '-'.join(disco.split('-')[1:]).decode('utf-8')
                
                print 'Salvando o album {0} do artista {1}'.format(album.name, banda.name)
                album.save()
                faixas = [faixa for faixa in arquivos if len(faixa) > 0 and faixa.find('.mp3') > -1]
                for faixa in faixas:
                    song = Song()
                    song.album = album
                    song.number = faixa.split('-')[0].strip()
                    song.name = ''.join(faixa.split('-')[1].strip()).decode('utf-8')
                    print u'Salvando a música {0} faixa de {1} do album {2}'.format(song.name.decode('utf-8'), banda.name.decode('utf-8'), album.name.decode('utf-8'))
                    song.save()
                
                del albuns[0]

"""                                    
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
