import Pyro4, Pyro4.naming
from crud import CRUD

def main():

    crud = CRUD()

    daemon = Pyro4.Daemon()
    
    uri = daemon.register(crud)
    print("Publicado")

    ns = Pyro4.locateNS()

    ns.register("crudYdalgo", uri)

    print("Objeto registrado")

    daemon.requestLoop()

main()