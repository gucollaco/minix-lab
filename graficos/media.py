import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def CriaGraficoLinha(processos, loteria, srtn, minix, titulo):

    plt.title(titulo)
    plt.xlabel('Processos')
    plt.ylabel('Tempo Médio (sec)')
    plt.plot(processos, loteria, color='#6A5ACD', label='Loteria')
    plt.plot(processos, srtn, color='#6495ED', label='SRTN')
    plt.plot(processos, minix, color='#00BFFF' ,label='Minix')
    plt.legend()
    plt.savefig(titulo + '.png')
    plt.show()

def CriaGraficoBarras(io, cpu, titulo):

    largura = 0.25

    r1 = np.arange(len(io))
    r2 = [x + largura for x in r1]

    plt.bar(r1, io, color='#6A5ACD', width=largura, label='IO')
    plt.bar(r2, cpu, color='#6495ED', width=largura, label = 'CPU')

    plt.xlabel('Escalonadores')
    plt.xticks([r + largura/2 for r in range(3)],['Minix', 'Loteria', 'SRTN'])
    plt.ylabel('Tempo Médio (sec)')
    plt.title(titulo)

    plt.legend()
    plt.savefig(titulo + '.png')
    plt.show()


    

def CalculaMedia(arquivo):

    dados = pd.read_csv(arquivo, header=None)
    novo_dados = dados.values

    total_cpu = 0
    total_io = 0

    for i in novo_dados:
        if i[0] == 'CPU':
            total_cpu += i[2]
        else: total_io += i[2]

    media_io = round(total_io/(len(novo_dados)/2), 6)
    print(media_io)

    media_cpu = round(total_cpu/(len(novo_dados)/2), 6)
    print(media_cpu)

    return media_io, media_cpu



def main():

    # 10000 IO - 10000 CPU

    io_loteria_10, cpu_loteria_10 = CalculaMedia('mediateste.csv')
    io_loteria_50, cpu_loteria_50 = CalculaMedia('mediateste.csv')
    io_loteria_100, cpu_loteria_100 = CalculaMedia('mediateste.csv')
    io_loteria_150, cpu_loteria_150 = CalculaMedia('mediateste.csv')

    io_srtn_10, cpu_srtn_10 = CalculaMedia('mediateste.csv')
    io_srtn_50, cpu_srtn_50 = CalculaMedia('mediateste.csv')
    io_srtn_100, cpu_srtn_100 = CalculaMedia('mediateste.csv')
    io_srtn_150, cpu_srtn_150 = CalculaMedia('mediateste.csv')
    
    io_minix_10, cpu_minix_10 = CalculaMedia('mediateste.csv')
    io_minix_50, cpu_minix_50 = CalculaMedia('mediateste.csv')
    io_minix_100, cpu_minix_100 = CalculaMedia('mediateste.csv')
    io_minix_150, cpu_minix_150 = CalculaMedia('mediateste.csv')

    processos = [10, 50, 100, 150]

    # IO
    loteria_io = [io_loteria_10, io_loteria_50, io_loteria_100, io_loteria_150]
    srtn_io = [io_srtn_10, io_srtn_50, io_srtn_100, io_srtn_150]
    minix_io = [io_minix_10, io_minix_50, io_minix_100, io_minix_150]

    # CPU
    loteria_cpu = [cpu_loteria_10, cpu_loteria_50, cpu_loteria_100, cpu_loteria_150]
    srtn_cpu = [cpu_srtn_10, cpu_srtn_50, cpu_srtn_100, cpu_srtn_150]
    minix_cpu = [cpu_minix_10, cpu_minix_50, cpu_minix_100, cpu_minix_150]
    

    CriaGraficoLinha(processos, loteria_cpu, srtn_cpu, minix_cpu, 'CPU-Bound')
    CriaGraficoLinha(processos, loteria_io, srtn_io, minix_io, 'IO-Bound')


    # =======================================================================================

    # 100 processos - 5000 IO - 10000 CPU
    minix_100_5io, minix_100_10cpu = CalculaMedia('mediateste.csv')
    loteria_100_5io, loteria_100_10cpu = CalculaMedia('mediateste.csv')
    srtn_100_5io, srtn_100_10cpu = CalculaMedia('mediateste.csv')


    # minix loteria srtn 
    io_5 = [minix_100_5io, loteria_100_5io, srtn_100_5io]
    cpu_10 = [minix_100_10cpu, loteria_100_10cpu, srtn_100_10cpu]
    

    # 100 processos - 10000 IO - 5000 CPU
    minix_100_10io, minix_100_5cpu = CalculaMedia('mediateste.csv')
    loteria_100_10io, loteria_100_5cpu = CalculaMedia('mediateste.csv')
    srtn_100_10io, srtn_100_5cpu = CalculaMedia('mediateste.csv')

    # minix loteria srtn 
    io_10 = [minix_100_10io, loteria_100_10io, srtn_100_10io]
    cpu_5 = [minix_100_5cpu, loteria_100_5cpu, srtn_100_5cpu]


    CriaGraficoBarras(io_5, cpu_10, '5k IO - 10k CPU')
    CriaGraficoBarras(io_10, cpu_5, '10k IO - 5k CPU')


main()