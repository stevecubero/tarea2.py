saldo = int (input ("Digite el saldo inicial del dia en colones: ")) 
transaccion =(input("Desea anadir entradas a la bitacora? : " ))
listaTransacciones = ("Tipo de transaccion:" "\nD = Deposito" "\nR = Retiro" "\nPROCESAR = Procesar todas las transacciones" )
conteoDepositos = 0
conteoRetiros = 0 
saldoDepositos = 0 #Cantidad en colones de depositos
saldoRetiros = 0 #Cantidad en colones de retiros
saldoTotalDepositos = 0 #saldo inicial + cantidad en depositos
saldoTotalRetiros = 0 #saldo inicial - cantidad en retiros

def depositos (x,y,z): #Funcion encargada de procesar depositos
    x += int (input("Cantidad a depositar en colones: ")) #matches saldoDeposito
    y += 1 #matches conteoDepositos
    z = saldoDepositos #Z matchear a saldoTotalDepositos
    return (x,y,z)


def retiros (x,y,z): #Funcion encargada de procesar retiros
    x += int (input ("Cantidad a retirar en colones: ")) #matches saldoRetiros
    y += 1 #matches conteoRetiros
    z += saldoRetiros #matchear a saldoTotalRetiros
    return (x,y,z)
 


def procesar ():
    print ("Las transacciones se van a procesar ahora: ")

       

def main ():
    print ("Tipo de transaccion:" "\nD = Deposito" "\nR = Retiro" "\nPROCESAR = Procesar todas las transacciones")
    selecionTransaccion = ""
    while selecionTransaccion != "PROCESAR":
        selecionTransaccion = input ("Seleccione el tipo de transaccion que desea ejecutar. Digite PROCESAR para finalizar y hacer el calculo final: ")
        if selecionTransaccion == "D":
            depositos(saldoDepositos,conteoDepositos,saldoTotalDepositos)
        elif selecionTransaccion == "R":
            retiros(saldoRetiros, conteoRetiros, saldoTotalRetiros)
        elif selecionTransaccion == "PROCESAR":
            procesar ()
            print ("El numero de depositos del dia fueron", conteoDepositos, "y la cantidad en colones de los depositos fue de " , saldoDepositos, "colones")
            print ("El numero de retiros del dia fueron ", conteoRetiros , "Y la cantidad de colones total en retiros fue de ", saldoRetiros, " colones")
            print ("El saldo total de la cuenta para el dia de hoy es de : " , (saldoTotalDepositos - saldoRetiros), "colones. ")
            break
            #print (depositos(saldoDepositos,conteoDepositos,saldoTotalDepositos))
        else:
            print ("La seleccion es incorrecta")
            
 
main ()
