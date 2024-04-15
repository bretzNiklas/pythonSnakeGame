import time
from multiprocessing import shared_memory


def snake():
    data = b"d"
    shm = shared_memory.SharedMemory(name="latenz_test")

    shm.buf[:len(data)] = data
    res = 0

    for i in range(1000):
        start_time = time.perf_counter()
        while True:
            received_data = shm.buf[:].tobytes().decode()

            if received_data != "d":
                end_time = time.perf_counter()
                elapsed = end_time - start_time

                res += elapsed

                shm.buf[:len(data)] = b"d"
                break

    print(res / 1000)

