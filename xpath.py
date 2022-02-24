
import xml.etree.ElementTree as ET
import sys
file = ET.parse(sys.argv[1]) #leemos argumento de consola


#seleccionamos una opcion
print("""        
    Selecciona tu querie:

    1) //book/title | //book/price   
    
    2) //title | //price

    3) /bookstore/book/title | //price    

    """)

eligio=input("-Selecciona un opcion :") #introducimos una opcion


if eligio=="1":
   ruta1 = file.findall('.//book/title | //book/price')
   for element in ruta1:
        print(element.text)

elif eligio=="2":
   ruta2 = file.findall('.//title | //price') 
   for element in ruta2:
       print(element.text)


elif eligio=="3":
    ruta3 = file.findall('.//book/title | //book/price')
    for element in ruta3:
        print(element.text)

else:
    print("opcion no valida")
    
