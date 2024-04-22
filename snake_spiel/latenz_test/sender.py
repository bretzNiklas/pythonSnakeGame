
from multiprocessing import shared_memory

def main():
    data = b"u"

    shm = shared_memory.SharedMemory(name="latenz_test", create=True, size=len(data))

    while True:
        shm.buf[:len(data)] = data


if __name__ == "__main__":
    main()