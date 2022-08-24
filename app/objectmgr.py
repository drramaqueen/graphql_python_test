import queue


class Resource:
    """ Some resource that clients need to use. Integer in our case. """

    def __init__(self, number):
        self.__value = number

    def reset(self):
        self.__value = 0

    def set_value(self, number):
        self.__value = number

    def get_value(self):
        return self.__value

    def __str__(self):
        return str(self.__value)


class ObjectMgr:
    """ We need only one instance of the pool for the whole app """
    __instance = None

    """ We create an instance of ObjectMgr class only once """
    @classmethod
    def get_manager_instance(cls, size):
        if cls.__instance is None:
            cls.__instance = ObjectMgr(size)
        return ObjectMgr.__instance

    """ Usually Resource has a complex construction process,
        so we need to reuse once created resources. """

    def __init__(self, size):
        """
        We need a thread-safe structure with O(1) efficiency of getting and putting values
        because we will have a lot of these operations. So we can use std module queue for this purpose.
        """
        self.__pool = queue.Queue()
        for i in range(size):
            self.__pool.put(Resource(i + 1))

    def get_object(self):
        """ We do not wait for the element if the pool is empty, otherwise the request will be blocked
        until a new element will be enqueued. """

        try:
            return self.__pool.get_nowait()
        except queue.Empty:
            return Resource(0)

    def free_object(self, number):
        """ We will wait until the element will be enqueued. """
        self.__pool.put(Resource(number))

    def is_empty(self):
        return self.__pool.empty()

    def available_count(self):
        return self.__pool.qsize()
