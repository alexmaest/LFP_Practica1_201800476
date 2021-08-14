from tkinter import *
from tkinter import filedialog
from operator import attrgetter

alumns = []
parameters = []
ascarray = []
descarray = []
minalumn = []
maxalumn = []
numaproved = []
numreproved = []
prom = []
Curso = []


def menu():
    print("*********************************")
    print("*         Menú Principal        *")
    print("*********************************")
    print("* 1) Cargar archivo             *")
    print("* 2) Mostrar reporte en consola *")
    print("* 3) Exportar reporte           *")
    print("* 4) Salir                      *")
    print("*********************************")


class saveAlumn():
    def __init__(self, alumn, grade):
        self.alumn = alumn
        self.grade = grade


def createFile():
    html = open('template/reporte.html', 'w')
    html.write("""<!DOCTYPE html>
        <html lang="en">

        <head>

            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta name="description" content="">
            <meta name="author" content="TemplateMo">
            <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700" rel="stylesheet">

            <title>Reporte</title>

            <!-- Bootstrap core CSS -->
            <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

            <!-- Additional CSS Files -->
            <link rel="stylesheet" href="assets/css/fontawesome.css">
            <link rel="stylesheet" href="assets/css/templatemo-host-cloud.css">
            <link rel="stylesheet" href="assets/css/owl.css">
        <!--

        Host Cloud Template

        https://templatemo.com/tm-541-host-cloud

        -->
        </head>

        <body>
            <!-- Header -->
            <header class="">
            <nav class="navbar navbar-expand-lg">
                <div class="container">
                <a class="navbar-brand" href="reporte.html"><h2>Reportes<em>LFP</em></h2></a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ml-auto">
                    </ul>
                </div>
                <div class="functional-buttons">
                </div>
                </div>
            </nav>
            </header>

            <!-- Page Content -->
            <!-- Banner Starts Here -->
            <div class="banner">
            <div class="container">
                <div class="row">
                <div class="col-md-8 offset-md-2">
                    <div class="header-text caption">
                    <h2 style=>Bienvenido al curso de</h2>
                    <h1 style="color: white; font-size:120px; text-align: center; font-style: italic; font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif; text-transform:uppercase">""" + Curso[0] + """</h1>
                    </div>
                </div>
                </div>
            </div>
            </div>
            <!-- Banner Ends Here -->

            <!-- Num Alumnos Starts Here -->
            <div class="services-section">
                <div class="container">
                    <div class="row">
                    <div class="col-md-12">
                        <div class="section-heading">
                        <h2 style="text-transform:uppercase; text-align: center;">Numero de alumnos</h2>
                        <h1 style="text-align: center; font-size: 200px; color:rgb(0, 50, 199);">""" + str(len(alumns)) + """</h1>
                        <h2 style="text-transform:uppercase; text-align: center; color:black;">en el curso</h1>
                        </div>
                    </div>
                    </div>
                </div>
            </div>
            <!-- Num Alumnos Ends Here -->
            
            <!-- Estudiantes Starts Here -->
            <hr>
            <div style="padding-bottom: 100px;" class="services-section">
                <div class="container">
                    <div class="row">
                        <div class="col-md-8 offset-md-2">
                            <div class="section-heading">
                            <h2 style="text-transform:uppercase; text-align: center;">Estudiantes en el curso</h2>
                            </div>
                            <table class="table">
                            <thead style="color:white; background-color: rgb(0, 50, 199); text-transform:uppercase; text-align: center;">
                                <tr>
                                <th scope="col">Nombre</th>
                                <th scope="col">Nota</th>
                                </tr>
                            </thead>
                            <tbody>
                            """)
    for studentable in alumns:
        if int(str(studentable.grade)) >= 61:
            html.write("""<tr>
            <td>""" + studentable.alumn + """</td>
            
            <td style="text-align: center; background-color:rgb(62, 111, 255); color:white">""" + str(studentable.grade) + """</td>
            </tr>
            """)
        else:
            html.write("""
            <tr>
            <td>""" + studentable.alumn + """</td>
            <td style="text-align: center; background-color:rgb(202, 46, 46); color:white">""" + str(studentable.grade) + """</td>
            </tr>
            """)
    html.write("""   
                            </tbody>
                            </table>
                        </div>
                        </div>
                </div>
                </div>
                <!-- Estudiantes Ends Here -->
                """)
    if len(ascarray) != 0:
        html.write("""<!-- Ascendente Starts Here -->
            <hr>
            <div style="padding-bottom: 100px;" class="services-section">
                <div class="container">
                    <div class="row">
                        <div class="col-md-8 offset-md-2">
                            <div class="section-heading">
                            <h2 style="text-transform:uppercase; text-align: center;">Datos de forma ascendente</h2>
                            </div>
                            <table class="table">
                            <thead style="color:white; background-color: rgb(0, 50, 199); text-transform:uppercase; text-align: center;">
                                <tr>
                                <th scope="col">Nombre</th>
                                <th scope="col">Nota</th>
                                </tr>
                            </thead>
                            <tbody>
                            """)
        for tableasc in ascarray:
            html.write("""
            <tr>
            <td>""" + tableasc.alumn + """</td>
            <td style="text-align: center;">""" + str(tableasc.grade) + """</td>
            </tr>
            """)
        html.write("""   
                                </tbody>
                                </table>
                            </div>
                            </div>
                    </div>
                    </div>
                <!-- Ascendente Ends Here -->""")
    if  len(descarray) != 0:
        html.write("""<!-- Descendente Starts Here -->
            <hr>
            <div style="padding-bottom: 100px;" class="services-section">
                <div class="container">
                    <div class="row">
                        <div class="col-md-8 offset-md-2">
                            <div class="section-heading">
                            <h2 style="text-transform:uppercase; text-align: center;">Datos de forma descendente</h2>
                            </div>
                            <table class="table">
                            <thead style="color:white; background-color: rgb(0, 50, 199); text-transform:uppercase; text-align: center;">
                                <tr>
                                <th scope="col">Nombre</th>
                                <th scope="col">Nota</th>
                                </tr>
                            </thead>
                            <tbody>
                            """)
        for tabledesc in descarray:
            html.write("""
            <tr>
            <td>""" + tabledesc.alumn + """</td>
            <td style="text-align: center;">""" + str(tabledesc.grade) + """</td>
            </tr>
            """)
        html.write("""   
                                </tbody>
                                </table>
                            </div>
                            </div>
                    </div>
                    </div>
                <!-- Descendente Ends Here -->""")
    if  len(maxalumn) != 0:
        html.write("""
        <!-- Nota max Starts Here -->
            <hr>
            <div class="services-section">
            <div class="container">
                <div class="row">
                <div class="col-md-12">
                    <div class="section-heading">
                    <h2 style="text-transform:uppercase; text-align: center;">Nota maxima en el curso</h2>
                    <h1 style="text-align: center; font-size: 200px; color:rgb(0, 50, 199);">""" + str(maxalumn[0].grade) + """</h1>
                    <h2 style="text-transform:uppercase; text-align: center; color:black;">por """ + str(maxalumn[0].alumn) + """</h1>
                    </div>
                </div>
                </div>
            </div>
            </div>
            <!-- Nota max Ends Here -->
        """)
    if len(minalumn) != 0:
        html.write("""
        <!-- Nota min Starts Here -->
            <hr>
            <div class="services-section">
            <div class="container">
                <div class="row">
                <div class="col-md-12">
                    <div class="section-heading">
                    <h2 style="text-transform:uppercase; text-align: center;">Nota minima en el curso</h2>
                    <h1 style="text-align: center; font-size: 200px; color:rgb(0, 50, 199);">""" + str(minalumn[0].grade) + """</h1>
                    <h2 style="text-transform:uppercase; text-align: center; color:black;">por """ + str(minalumn[0].alumn) + """</h1>
                    </div>
                </div>
                </div>
            </div>
            </div>
            <!-- Nota min Ends Here -->
        """)
    if len(prom) != 0:
        html.write("""
        <!-- Prom Starts Here -->
            <hr>
            <div class="services-section">
                <div class="container">
                    <div class="row">
                    <div class="col-md-12">
                        <div class="section-heading">
                        <h2 style="text-transform:uppercase; text-align: center;">Promedio de notas</h2>
                        <h1 style="text-align: center; font-size: 200px; color:rgb(0, 50, 199);">""" + str(prom[0]) + """</h1>
                        <h2 style="text-transform:uppercase; text-align: center; color:black;">en el curso</h1>
                        </div>
                    </div>
                    </div>
                </div>
            </div>
            <!-- Prom Ends Here -->
        """)
    if len(numaproved) != 0:
        html.write("""
        <!-- Num apr Starts Here -->
            <hr>
            <div class="services-section">
                <div class="container">
                    <div class="row">
                    <div class="col-md-12">
                        <div class="section-heading">
                        <h2 style="text-transform:uppercase; text-align: center;">Numero de estudiantes</h2>
                        <h1 style="text-align: center; font-size: 200px; color:rgb(0, 50, 199);">""" + str(numaproved[0]) + """</h1>
                        <h2 style="text-transform:uppercase; text-align: center; color:black;">aprobados</h1>
                        </div>
                    </div>
                    </div>
                </div>
            </div>
            <!-- Num apr Ends Here -->
        """)
    if len(numreproved) != 0:
        html.write("""
        <!-- Num rep Starts Here -->
            <hr>
            <div class="services-section">
                <div class="container">
                    <div class="row">
                    <div class="col-md-12">
                        <div class="section-heading">
                        <h2 style="text-transform:uppercase; text-align: center;">Numero de estudiantes</h2>
                        <h1 style="text-align: center; font-size: 200px; color:rgb(0, 50, 199);">""" + str(numreproved[0]) + """</h1>
                        <h2 style="text-transform:uppercase; text-align: center; color:black;">reprobados</h1>
                        </div>
                    </div>
                    </div>
                </div>
            </div>
            <!-- Num rep Ends Here -->
        """)
    html.write("""
    <!-- Bootstrap core JavaScript -->
            <script src="vendor/jquery/jquery.min.js"></script>
            <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

            <!-- Additional Scripts -->
            <script src="assets/js/custom.js"></script>
            <script src="assets/js/owl.js"></script>
            <script src="assets/js/accordions.js"></script>


            <script language = "text/Javascript">
            cleared[0] = cleared[1] = cleared[2] = 0; //set a cleared flag for each field
            function clearField(t){                   //declaring the array outside of the
            if(! cleared[t.id]){                      // function makes it static and global
                cleared[t.id] = 1;  // you could use true and false, but that's more typing
                t.value='';         // with more chance of typos
                t.style.color='#fff';
                }
            }
            </script>
        </body>
        </html>
    """)            
    html.close()
    print("\n")
    print("Reporte creado con exito")
    print("\n")


def graphicBrowser():
    win = Tk()
    win.geometry("1x1")
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select a File", filetypes=(("Lfp files", "*.lfp*"), ("All files", "*.*")))
    win.destroy()
    return filename


def printAlumns():
    print("\n")
    print("----------- Bienvenido al curso de " + Curso[0] + " -----------")
    print("\n")
    print("Total de alumnos en el curso: " + str(len(alumns)))
    print("Alumnos en el curso: ")
    for estudiante in alumns:
        print("Nombre = " + estudiante.alumn + ", Nota = " + str(estudiante.grade))
    print("\n")

    # Parameters functions
    for parameter in parameters:
        if parameter == "ASC":
            print("Notas ordenadas de forma ascendente: ")
            for alumnito in ascarray:
                print("Nota: " + str(alumnito.grade) +
                      ", Nombre: " + alumnito.alumn)
            print("\n")

        if parameter == "DESC":
            print("Notas ordenadas de forma descendente: ")
            for alumnito2 in descarray:
                print("Nota: " + str(alumnito2.grade) +
                      ", Nombre: " + alumnito2.alumn)
            print("\n")

        if parameter == "AVG":
            print("El promedio de los alumnos es: " + str(prom[0]))

        if parameter == "MIN":
            print("La nota mínima es de: " + str(minalumn[0].grade))

        if parameter == "MAX":
            print("La nota maxima es de: " + str(maxalumn[0].grade))

        if parameter == "APR":
            print("Número de estudiantes aprobados: " + str(numaproved[0]))

        if parameter == "REP":
            print("Número de estudiantes reprobados: " + str(numreproved[0]))
    print("\n")


def read(path):
    try:
        global parameters
        parameters = []
        global ascarray
        ascarray = []
        global descarray
        descarray = []
        global minalumn
        minalumn = []
        global maxalumn
        maxalumn = []
        global numaproved
        numaproved = []
        global numreproved
        numreproved = []
        global prom
        prom = []
        with open(path, 'r') as f:
            format = path.find(".lfp")
            if format:
                alltext = f.readlines()
                temptext = " "
                for it in alltext:
                    temptext += it.replace("\n", " ")
                #print(temptext)

                # print(len(alltext))

                #if len(temptext) == 1:
                cursosplit = temptext.split("=")
                # Course
                global Curso
                Curso = []
                Curso.append(cursosplit[0].strip())
                keysplit = cursosplit[1].split("}")

                # Parameters
                quitlastcommas = keysplit[1].split(",")
                cont = 0
                for iteration in quitlastcommas:
                    tempvar = quitlastcommas[cont].replace(",", " ")
                    cleantempvar = tempvar.strip()
                    parameters.append(cleantempvar)
                    cont += 1

                # Alumns
                global alumns
                alumns = []
                keyremove1 = keysplit[0].replace("{", " ")
                keyremove2 = keyremove1.replace("}", " ")
                commasplit = keyremove2.split(",")
                for student in commasplit:
                    text1 = student.replace(",", " ")
                    text2 = text1.replace("<", " ")
                    text3 = text2.replace(">", " ")
                    text4 = text3.split(";")
                    text5 = text4[0].replace("\"", " ")
                    text6 = text5.replace(";", " ")
                    alumn = text6.strip()
                    grade = text4[1].strip()
                    upgrade = int(str(grade))
                    tempAlumn1 = saveAlumn(alumn, upgrade)
                    alumns.append(tempAlumn1)
                """
                else:
                    # Course
                    quitone = temptext[0].replace("=", " ")
                    quitwo = quitone.replace("{", " ")
                    cleanquitwo = quitwo.strip()
                    Curso.append(cleanquitwo)

                    # Parameters array
                    quitlast = temptext[-1].replace("}", " ")
                    quitlastcommas = quitlast.split(",")
                    cont = 0
                    for iteration in quitlastcommas:
                        tempvar = quitlastcommas[cont].replace(",", " ")
                        cleantempvar = tempvar.strip()
                        parameters.append(cleantempvar)
                        cont += 1

                    # Alumns Array
                    for line in temptext:
                        first = line.split(";")
                        if len(first) > 1:
                            # Name
                            minorquit = first[0].replace("<", " ")
                            commasquit = minorquit.replace('\"', " ")
                            cleancommasquit = commasquit.strip()
                            # Grade
                            majorquit = first[1].replace(">", " ")
                            extrasquit = majorquit.replace(",", " ")
                            cleanextrasquit = extrasquit.strip()
                            tempAlumn = saveAlumn(
                                cleancommasquit, cleanextrasquit)
                            alumns.append(tempAlumn)
                """
                # Parameters functions
                for parameter in parameters:
                    if parameter == "ASC":
                        #print("ASC Encontrado")
                        #global ascarray
                        ascarray += alumns
                        quickSort(ascarray, 0, len(ascarray) - 1, lambda x, y: x.grade > y.grade)

                    if parameter == "DESC":
                        #print("DESC Encontrado")
                        #global descarray
                        descarray += alumns
                        quickSort(descarray, 0, len(descarray) - 1, lambda x, y: x.grade < y.grade)

                    if parameter == "AVG":
                        #print("AVG Encontrado")
                        tempalumn3 = []
                        cont2 = 0
                        for alumn3 in alumns:
                            tempalumn3 = alumn3.grade
                            cont2 += int(str(tempalumn3))
                        prom.append(round(cont2/len(alumns), 2))

                    if parameter == "MIN":
                        #print("MIN Encontrado")
                        minalumn.append(min(alumns, key=attrgetter("grade")))

                    if parameter == "MAX":
                        #print("MAX Encontrado")
                        maxalumn.append(max(alumns, key=attrgetter("grade")))

                    if parameter == "APR":
                        #print("APR Encontrado")
                        tempalumn5 = []
                        cont3 = 0
                        for alumn5 in alumns:
                            tempalumn5 = alumn5.grade
                            if int(str(tempalumn5)) >= 61:
                                cont3 += 1
                        numaproved.append(cont3)

                    if parameter == "REP":
                        #print("REP Encontrado")
                        tempalumn6 = []
                        cont4 = 0
                        for alumn6 in alumns:
                            tempalumn6 = alumn6.grade
                            if int(str(tempalumn6)) <= 61:
                                cont4 += 1
                        numreproved.append(cont4)
                
                print("\n")
                print("Carga de datos realizada correctamente")
                print("\n")
            else:
                print("\n")
                print("Formato de carga no coincide con .lfp, intentalo de nuevo")
                print("\n")
        return temptext
    except:
        print("\n")
        print("Ha ocurrido un error, intentalo de nuevo")
        print("\n")


def partition(array, start, end, function):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and function(array[high], pivot):
            high = high - 1

        while low <= high and not function(array[low], pivot):
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


def quickSort(array, start, end, function):
    if start >= end:
        return

    p = partition(array, start, end, function)
    quickSort(array, start, p-1, function)
    quickSort(array, p+1, end, function)

Ejecucion = True
while Ejecucion:
    menu()

    opcion = input("Elige una opción: ")

    if opcion == "1":
        name = graphicBrowser()
        read(name)

    elif opcion == "2":
        printAlumns()

    elif opcion == "3":
        createFile()

    elif opcion == "4":
        print("Has salido del programa")
        Ejecucion = False

    else:
        print("Intenta de nuevo")
