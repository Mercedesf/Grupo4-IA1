# Temas Tratados en el Trabajo Práctico 1

* Diferencia entre Inteligencia e Inteligencia Artificial.

* Concepto de omnisciencia, aprendizaje y autonomía.

* Definición de Agente y sus características. Clasificación de Agentes según su estructura.

* Identificación y categorización del Entorno de Trabajo en tabla REAS.

* Caracterización del Entorno de Trabajo.

# Ejercicios Teóricos

1. Defina con sus propias palabras inteligencia natural, inteligencia artificial y agente.

La inteligencia natural es la capacidad cognitiva que es inherente a los seres biológicos (humanos, pero también animales) para percibir su entorno, aprender de la experiencia, razonar, adaptarse a diversas situaciones y resolver problemas complejos. Por otro lado, la inteligencia artificial es creada por el ser humano y son algoritmos y sistemas diseñados para ejecutar tareas de forma autónoma o semiautónoma. Además, un agente es una entidad que percibe su entorno a través de sensores o datos de entrada y actúa sobre ese entorno mediante actuadores o acciones.

2. ¿Qué es un agente racional?

Un agente racional es una entidad que toma decisiones para maximizar el resultado esperado según la información disponible y sus objetivos, teniendo en cuanta una medida de rendimineto definida. Un ejemplo puede ser un coche autónomo que percibe su entorno mediante sensores y actúa mediante actuadores. Los sensores detectan otros vehículos, peatones, señales de tráfico, etc. y toma decisiones sobre cuándo acelerar, frenar o cambiar de carril para llegar a destino.

3. ¿Un agente es siempre una computadora?

No, ya que como se define como aquel capaz de modificar el entorno en el cual se encuentra, puede ser una computadora, un humano, un animal, empresa, etc.

4. Defina Omnisciencia, Aprendizaje y Autonomía.

* Omnisciencia: Sería la cualidad de saberlo todo o saber todo lo que afecta a cierta acción.  
* Aprendizaje: Es hacer uso de las percepciones para mejorar la habilidad del agente cuando vuelva a actuar.  
* Autonomía: Actua en base al conocimiento previo, y en caso de no tener el conocimiento busca como lo compensa.

5. Defina cada tipo de agente en función de su **estructura** y dé un ejemplo de cada categoría.

* Agente Basado en Objetivos: A diferencia del basado en modelos a este se le dan objetivos y antes de inicair la accion se pregunta que consecuencias tendra esta. Ejemplo: sistema de navegacipon autónomo para llegar a una ubicación.
* Agente Basado en utilidad:En vez de tener objetivos o reglas este mide sus decisiones en utilidad preguntandose si estara contento con el resultado o si este le sera util. Ejemplo:sistema de inteligencia de taxi autónomo.
* Agente Reactivo Simple: A traves de sensores mide o analiza o el entorno y en base a reglas de condicion-accion, decide que hacer con los actuadores. Ejemplo: frenado de emergencia autónomo.
* Agente Reactivo basados en modelos: Cuando obtiene informacion del entorno analiza en que estado se encuentra, y se pregunta hacia donde o como evolucionara el entorno y que consecuencias tienen sus acciones.Sabiento todo esto y en bas a la reglas de condicion-accion actuara. Ejemplo: control de crucero adaptativo con seguimiento de carril en niebla.

6. Para los siguientes entornos de trabajo indique sus **propiedades**:

        a. Una partida de ajedrez.
        b. Un partido de baloncesto.
        c. El juego Pacman.
        d. El truco.
        e. Las damas.
        f. El juego tres en raya.
        g. Un jugador de Pokémon Go.
        h. Un robot explorador autónomo de Marte.

| Entorno de trabajo | Observable parcial o totalmente | Determinista o estocástico | Episódico o secuencial | Estático o dinámico | Discreto o contínuo | Agentes individual o multiagente |
|---|---|---|---|---|---|---|
| Partida de Ajedrez | Parcialmente porque no se que jugada va a realizar mi oponente | Determinístico porque al mover un peón sabemos como va a quedar el tablero | Secuencial porque depende de la acciones pasadas | Estático porque el tablero queda igual mientras que uno piensa | Discreto porque tener un número finito de opciones de movimientos | Multiagente porque se juega de a dos |  
| Partido de baloncesto | Parcialmente porque no se que jugada va a realizar mi oponente | Estocástico porque no sabemos que va a pasar al realizar un pase | Secuencial porque depende de la acciones pasadas | Dinámico porque el entorno puede cambiar mientras el agente piensa | Discreto porque tener un número finito de opciones de movimientos | Multiagente porque se juega en equipo | 
| El juego de Pacman | Totalmente porque se como se mueven lo fantasmas | Determinístico porque al mover el pacman sabemos a donde va | Secuencial porque depende de la acciones pasadas | Dinámico porque el entorno puede cambiar mientras el agente piensa | Discreto porque tener un número finito de opciones de movimientos | Agente individual porque solo juega el pacman |
| El truco | Parcialmente porque no se que cartas o que jugada va a realizar mi oponente | Estocástico porque no sabemos que va a pasar al realizar una jugada | Secuencial porque depende de la acciones pasadas | Estático porque las cartas no varían mientras estás en juego | Discreto porque tener un número finito de opciones de movimientos | Multiagente porque se juega de más de dos | 
| Las damas | Parcialmente porque no se que jugada va a realizar mi oponente | Determinístico porque al mover una ficha sabemos como va a quedar el tablero | Secuencial porque depende de la acciones pasadas | Estático porque el tablero queda igual mientras que uno piensa | Discreto porque tener un número finito de opciones de movimientos | Multiagente porque se juega de a dos |  
| EL juego de tres en raya | Parcialmente porque no se que jugada va a realizar mi oponente | Determinístico porque al mover o poner una ficha sabemos como va a quedar el tablero | Secuencial porque depende de la acciones pasadas | Estático porque el tablero queda igual mientras que uno piensa | Discreto porque tener un número finito de opciones de movimientos | Multiagente porque se juega de a dos | 
| EL jugador de Pokémon Go | Parcialmente porque no sabes el lugr exacto donde está el pokemon | Estocástico porque los pokemos aparecen de manera aleatoria y los pokemones se pueden ir o no | Secuencial porque a medida que vas teniendo mas nivel vas a poder capturar más pokemones | Dinámico porque no sabemos si el entorno va a cambiar o no | Discreto porque tener un número finito de opciones de movimientos | Agente solitario si nos enfocamos en la captura del pokemon |
| Un robot explorador autónomo de Marte | Totalmente porque con los sensores y cámaras podemos conocer todo | Determinístico porque si gira a la derecha sabemos a donde va | Secuencial porque depende de la acciones pasadas | Dinámico porque no sabemos si el entorno va a cambiar o no | Discreto porque tener un número finito de opciones de movimientos | Agente solitario |

7. Elabore una tabla REAS para los siguientes entornos de trabajo:

a. Crucigrama.  
|Rendimiento|Entorno|Actuadores|Sensores|
|---|---|---|---|
|Porcentaje de palabras o casillas completadas correctamente. <br> Tiempo invertido en resolver el crucigrama (penalizando la lentitud). |Cuadrícula bidimensional. <br> Palabras del diccionario. |Comandos para escribir o reescribir las celdas. <br> Validación del crucigrama completo. | Lector de cada celda |

b. Taxi circulando.  
|Rendimiento|Entorno|Actuadores|Sensores|
|---|---|---|---|
|Llevar al pasajero en el menor tiempo posible, manteniendo su seguridad. | Infrastuctura vial. <br> Tráfico. Clima. | Controles del auto. <br> Señalización (Semáforos, carteles, etc) <br> Sistema de seguridad del pasajero y conductor | Si es un taxi autónomo: <br> Cámaras, sensores de paso, enconders.|

c. Robot clasificador de piezas.  
|Rendimiento|Entorno|Actuadores|Sensores|
|---|---|---|---|
|Separar las piezas defectuosas lo más rapido posible sin errores | La cinta transportadora o zona de alimentación de piezas. <br> Los contenedores, ramales o bandejas de clasificación final. <br> Las piezas (variables en geometría, material, orientación, color o presencia de defectos). <br> Las condiciones de la planta industrial. | Mecanismo de posicionamiento. <br> Mecanismo para apartar la pieza. <br> Controladores de velocidad. | Cámaras, sensores de paso, enconders. |


# Ejercicios Prácticos

8. La Hormiga de Langton es un agente capaz de modificar el estado de la casilla en la que se encuentra para colorearla o bien de blanco o de negro. Al comenzar, la ubicación de la hormiga es una casilla aleatoria y mira hacia una de las cuatro casillas adyacentes. Si...

* ... la casilla sobre la que está es blanca, cambia el color del cuadrado, gira noventa grados a la derecha y avanza un cuadrado.
* ... la casilla sobre la que está es negra, cambia el color del cuadrado, gira noventa grados a la izquierda y avanza un cuadrado.

Caracterice el agente con su tabla REAS y las propiedades del entorno para después programarlo en Python:

¿Observa que se repite algún patrón? De ser así, ¿a partir de qué iteración?

| Agente | Medidas de Rendimiento | Etorno | Actuadores | Sensores |
|---|---|---|---|---|
|Hormiga de Langton|Cantidades de avenidas que genera|Agrupacion de celdas|Cambio de celda|Codigo que verfica ña ceñda|

**Prompt enviado a Claude:**  
\<rol\>  
Eres un desarrollador experto en Python, especializado en simulaciones. Escribes código limpio, modular y sigues las buenas prácticas de la industria.  
\</rol\>  

\<contexto\>  
La "Hormiga de Langton" es un autómata celular bidimensional que evoluciona siguiendo reglas sencillas pero que genera comportamientos complejos (como la creación de una "autopista" direccional después de aproximadamente 10,000 iteraciones).  
\</contexto\>  

\<objetivos\>  
Desarrollar un programa en Python que simule el comportamiento de la Hormiga de Langton. 
Reglas del sistema:  
1. El tablero es una matriz bidimensional de tamaño definido: 30x30. Inicialmente, TODAS las casillas son NEGRAS.  
2. Al comenzar, la hormiga se ubica exactamente en el centro de la cuadrícula mirando hacia arriba por defecto.  
3. Si la casilla sobre la que está es blanca, cambia el color de esa casilla a negro, gira 90 grados a la derecha y avanza una casilla.  
4. Si la casilla sobre la que está es negra, cambia el color a blanco, gira 90 grados a la izquierda y avanza una casilla.  
\</objetivos\>  

\<limites\>  
- Simplicidad: El código debe ser sencillo y directo. Evita la sobreingeniería.  
- Modularidad: Separa la lógica (ej. una clase/estructura para la Hormiga y la matriz de datos para el Tablero).  
- Visualización: Utiliza la librería `matplotlib` para mostrar la evolución del tablero en una ventana gráfica.  
- Bordes: al llegar a un borde debe desaparecer.  
- Variables dinámicas: El tamaño del tablero y la velocidad de la animación deben ser variables fácilmente configurables al inicio del script.  
\</limites\>  

\<producto\>  
1. El código fuente completo en un único bloque de código, listo para ser copiado, pegado y ejecutado.  
2. Una brevísima lista de instrucciones (1-2 líneas) indicando cómo ejecutarlo y qué dependencias instalar (ej. pip install matplotlib).  
3. Ve directo al grano: no incluyas introducciones largas, saludos ni explicaciones paso a paso de cómo funciona el código, a menos que estén en los docstrings.  
\</producto\>  

**ACLARACIÓN: luego de enviar el prompt también se le pidió en mensajes posteriores que mostrara un contador para las iteraciones y que mostrara a la hormiga con una casilla roja**
