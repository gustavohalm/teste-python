file_name = input("Digite o nome do arquivo: ")

file = open(file_name)
lines = file.readlines()
ttask = int(lines[0])
umax = int(lines[1])

if (ttask >= 1) and (ttask <= 10):
    if(umax >= 1) and (umax >= 10):
        for i in range(2, len(lines)):
            lines = lines[i]

    else:
        print("Valor de umax fora do limite")
else:
    print("Valor de ttask fora do limite")