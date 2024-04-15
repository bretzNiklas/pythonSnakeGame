import time
from multiprocessing import shared_memory

class InputSender:
    @staticmethod
    def sendInputs():

        data = [b"u", b"l", b"d", b"r"]

        # Create a shared memory block
        #shm = shared_memory.SharedMemory(name="snake_input")
        shm = shared_memory.SharedMemory(name="snake_input", create=True, size=len(data[0]))

        i = 1
        while True:
            # Write data to the shared memory
            shm.buf[:len(data)] = data[i]

            print(data[i])

            i += 1
            i %= 4

            # Sleep for a short interval
            time.sleep(0.5)

