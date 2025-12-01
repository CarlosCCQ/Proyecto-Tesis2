from mpi4py import MPI
import cv2
import glob
import sys
import os
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if len(sys.argv) < 3:
    if rank == 0:
        print("Uso: python image_mpi.py <input_folder> <output_folder>")
    exit()

input_folder = sys.argv[1]
output_folder = sys.argv[2]

if rank == 0 and not os.path.exists(output_folder):
    os.makedirs(output_folder)

comm.Barrier()

files = sorted(glob.glob(f"{input_folder}/*.png"))
total_files = len(files)

chunk = total_files // size
start = rank * chunk
end = start + chunk if rank != size-1 else total_files

subset = files[start:end]

start_time = time.time()

for f in subset:
    img = cv2.imread(f)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    filename = os.path.basename(f)
    cv2.imwrite(f"{output_folder}/{rank}_{filename}", gray)

end_time = time.time()
elapsed = end_time - start_time

print(f"[Nodo {rank}] Tiempo: {elapsed:.4f} segundos, imágenes: {len(subset)}")

comm.Barrier()

if rank == 0:
    print("\nProcesamiento completado.")
    print(f"Total de imágenes: {total_files}")
    print(f"Nodos utilizados: {size}")
