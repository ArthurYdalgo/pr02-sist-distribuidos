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

## Análise de pacotes

Abaixo encontram-se alguns pacotes capturados pelo Wireshark durante algumas operações de teste (exemplificada na imagem abaixo). O arquivo completo encontra-se nesse repositório.

### Caso de teste
![image](https://user-images.githubusercontent.com/25585428/140676723-30713ebd-1819-4d2b-98f4-3678f3a010f4.png)


### Create

Pacote de Enviado:

![image](https://user-images.githubusercontent.com/25585428/140676371-48431ea4-d4c3-4d3b-ab37-3699527b213b.png)

Pacote Recebido
![image](https://user-images.githubusercontent.com/25585428/140676431-44b7d604-ad94-4b4f-b6e6-03c9579e68c0.png)


### Update

Pacote de Enviado:

![image](https://user-images.githubusercontent.com/25585428/140676477-01807e1e-d495-49ae-8594-a5a9c10f4740.png)


Pacote Recebido
![image](https://user-images.githubusercontent.com/25585428/140676490-896e3d8a-447d-4ead-9e08-47619929d80e.png)


### Get

Pacote de Enviado:

![image](https://user-images.githubusercontent.com/25585428/140676499-47f143bb-b77c-4dab-9247-7f9a4c54a4c0.png)


Pacote Recebido
![image](https://user-images.githubusercontent.com/25585428/140676506-1a77335c-5d1e-4d2d-a4a2-3f777de87ad8.png)


### Destroy

Pacote de Enviado:

![image](https://user-images.githubusercontent.com/25585428/140676513-303537dd-3162-4ffe-aa75-7965afeb91ac.png)


Pacote Recebido

![image](https://user-images.githubusercontent.com/25585428/140676527-63a37fc7-b28b-461b-87a3-df244a56debc.png)

