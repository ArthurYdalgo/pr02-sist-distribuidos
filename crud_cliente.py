import sys
import Pyro4

crud_ydalgo = Pyro4.Proxy("PYRONAME:crudYdalgo")

try:
    crud_ydalgo._pyroBind()
except Pyro4.errors.CommunicationError:
    print("Objeto remoto não encontrado. Encerrando execução")
    sys.exit(1)
    pass

op = 1

def getUserUUID():
    user_uuid_length = 0
    while(user_uuid_length > 4 or user_uuid_length == 0):
        user_uuid = input("Insira o id do usuario (no máximo 4 characteres): ")
        user_uuid_length = len(user_uuid)
    return {'uuid' : user_uuid}

def getUserData():
    name_length = 0
    email_length = 0
    password_length = 0
    while(name_length > 50 or name_length == 0):
        name = input("Insira um nome (no máximo 50 characteres): ")
        name_length = len(name)
    while(email_length > 50 or email_length == 0):
        email = input("Insira um email (no máximo 50 characteres): ")
        email_length = len(email)
    while(password_length > 50 or password_length == 0):
        password = input("Insira uma senha (no máximo 50 characteres): ")
        password_length = len(password)
    
    return {'name' : name, 'email': email, 'password':password}


while op != 5:
    print('Digite:')
    print('1 - Inserir')
    print('2 - Atualizar')
    print('3 - Achar')
    print('4 - Deletar')
    print('5 Sair')

    op = int(input())

    if op >= 1 and op <= 4:

        if(op == 1):
            user_data = getUserData()

            print(crud_ydalgo.store(user_data))
            
        elif(op==2):
            user_uuid_obj = getUserUUID()

            print("Agora insira os novos dados do usuario...")

            user_new_data = getUserData()
            user_new_data['uuid'] = user_uuid_obj['uuid']

            print(crud_ydalgo.update( user_uuid_obj['uuid'], user_new_data))

        elif(op==3):
            user_uuid_obj = getUserUUID()            

            print(crud_ydalgo.get(user_uuid_obj['uuid']))
        elif(op==4):
            user_uuid_obj = getUserUUID()  

            print(crud_ydalgo.destroy(user_uuid_obj['uuid']))

    elif op == 5:
        print("Obrigado e volte sempre!")
    else:
        print("Operação inválida")

    
