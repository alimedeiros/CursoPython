#desafio da aula 6 - Faça um programa que leia algo e mostre seu tipo primitivo.

p = input('Digite para saber detalhes do tipo primitivo:')
print('É numérico?', p.isnumeric())
print('É uma string?', p.isalpha())
print('É alfanumérico?', p.isalnum())
print('É todo maiúsculo?', p.isupper())
print('É todo miníscul?', p.islower())