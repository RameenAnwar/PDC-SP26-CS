import addTask

if __name__ == '__main__':
    # Dispatch the add task asynchronously using delay()
    result = addTask.add.delay(5, 5)