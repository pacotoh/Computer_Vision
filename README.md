# Menú de aplicaciones

Incluido menú de aplicaciones gráfico para elegir, por ahora, entre la aplicación de ROI y la de CHROMA.
Ha sido utilizada la librería PyQt4.

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

## TODO

Falta probar con varios fondos de chroma. Ej: Probar con Chroma verde.

# IMG_Filters

El primer paso es instalar PyQt. Si utilizas linux puedes instalarlo en terminal con el comando:
```
sudo apt-get install python-qt4
```
