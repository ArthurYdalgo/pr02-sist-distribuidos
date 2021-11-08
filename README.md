# PR 02 - Sistemas Distribuidos

## Requisitos

- Python3.7+
- Pyro4 (use `pip install Pyro4`)

## Instruções de uso

- Descubra o IP da sua máquina (usando o comando `ipconfig`, `ifconfig` ou algum similar)

- Execute o comando:
```
$ pyro4-ns -n 192.168.1.102 // Troque o IP pelo IP da sua máquina
```

- Inicie o servidor executando:
```
$ python3 crud_servidor.py
```

- Inicie o cliente executando:
```
$ python3 crud_cliente.py
```

Após esses passos, basta seguir as instruções do menu