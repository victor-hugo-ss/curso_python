"""
CONSTANTES = "Variáveis" que não vão mudar 
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 65
local_carro = 100

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local do radar 1 está
RADAR_RANGE = 1 # distância em que o radar pega

velocidade_carro_passou = velocidade > RADAR_1
range_radar_antes = LOCAL_1 - RADAR_RANGE
range_radar_depois = LOCAL_1 + RADAR_RANGE
carro_passou_radar = local_carro >= range_radar_antes and local_carro <= range_radar_depois

if velocidade_carro_passou:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar:
    print('carro passou radar 1')

if velocidade_carro_passou and carro_passou_radar:
    print('Multado por excesso de velocidade!')
