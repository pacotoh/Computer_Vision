# ROI

 Prueba de captura de una Región de Interés en vídeo capturado por webcam usando python y opencv.

## Funciones de captura y creación de una sesión

- Comando 'c': Se realiza una foto y se guarda en disco.
- Comando 's': se guarda la sesión, es decir, el conjunto de fotos realizadas en un .pkl.

## Funcionamiento del ROI

- Haciendo click y desplegando sobre la zona de la imagen deseada se generará una nueva ventana con la ROI, aplicando un filtro que por defecto es el paso de RGB a escala de grises.
- Para desactivar la ROI y volver a generar una nueva pulsamos botón izquierdo y a continuación se puede volver a repetir
el paso 1.

# CHROMA

Prueba de Chroma utilizando imágenes rgb y yuv.

## Funcionamiento del Chroma

- Pulsando 'b' se toma una captura como background de Chroma. Esto quiere decir que lo nuevo que aparezca añadido a dicha imagen será seleccionado para transferirse a un nuevo fondo.
- Pulsando 'c' comienza la ejecución del Chroma. Anteriormente ha tenido que establecerse una imagen de background con el comando 'b'.
- Pulsando '+' y '-' se ajusta el límite para la máscara.

# Filters

El primer paso es instalar PyQt. Si utilizas linux puedes instalarlo en la terminal con el comando:
```
sudo apt-get install python-qt4
```
Ahora contamos con una pequeña GUI con botones. Cada uno de estos botones es un filtro para aplicar sobre la imagen.

# Move Detector

El background tarda del orden de 12-20 imágenes en configurarse, por lo que echa esa cantidad de fotos antes de ser operativo.
Las imágenes se generan en la carpeta images/move_detector.

El funcionamiento es sencillo, se van acumulando los frames que superan una cantidad de pixels con variación respecto al fondo y cuando
esta cantidad de frames llega a un umbral se echa una foto.

# Feature Matching

Primera versión del Feature Matching usando SIFT.

## Imágenes y modelos

Dentro de 'images/feature_matching/models/' vamos a tener almacenadas las imágenes creadas como modelos.
Una vez generado el primer modelo y almacenada la primera imagen se generará un fichero 'save.pkl' para no tener que volver a cargar las imágenes siempre que se ejecute la aplicación.

## Funcionamiento

Contamos con dos comandos posibles:

- Comando 'm' para generar un nuevo modelo. Genera una imagen y guarda en el .pkl dicha imagen junto al resto.
- Comando 'c' para capturar una imagen y hacer el matching con los modelos generados

- Hacer el matching de forma más eficiente: almacenar todos los detectAndCompute en un pickle. Para poder realizar el matching debemos tener al menos un modelo generado.

## Salida

Nuestra salida es la imagen capturada y el modelo más próximo a dicha imagen.

```
sol = cv.drawMatchesKnn(capt, kpoints1, model, kpoints2, matches[:20], None, flags = 2)
```
Se puede ajustar el número de puntos de interés que se quiere mostrar en el matching con el parámetro matches. En el ejemplo mostramos 20 matches en la imagen.


# Face Detection

Prueba de aplicación de un filtro cualquiera a una cara detectada mediante haar cascade. En este caso se ha utilizado un filtro laplaciano. De esta forma podemos aplicar algún filtro que distorsione las caras en un vídeo o imagen para codificarlas de tal forma que sean irreconocibles.
