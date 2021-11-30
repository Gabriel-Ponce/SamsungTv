from controller import Controller


def main():
    controller = Controller()
    

    while controller.isrunning:
        controller.execute()
       


if __name__ == "__main__":
    main()