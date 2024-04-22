from multiprocessing import shared_memory
from threading import Thread

from snake import Snake
from input_sender import InputSender


def main():



    thread = Thread(target=InputSender.sendInputs)
    thread2 = Thread(target=Snake.snake)

    thread.start()
    thread2.start()


if __name__ == "__main__":
    main()
