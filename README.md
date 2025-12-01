## Add parallel image grayscale conversion using MPI

Implementa un script MPI que distribuye el procesamiento de imágenes PNG
de una carpeta de entrada, convierte cada imagen a escala de grises usando
OpenCV y guarda los resultados en una carpeta de salida.

- Cada proceso (rank) procesa un subconjunto equilibrado de archivos
- Se crea la carpeta de salida solo desde el proceso raíz
- Se usan barreras para sincronización
- Se imprime tiempo de ejecución por nodo y estadísticas finales