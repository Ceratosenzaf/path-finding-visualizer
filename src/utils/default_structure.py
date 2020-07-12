class Default():
    """
        The default structure of all the algorithms I'll use
    """    


    def __init__(self, table):
        self.table = table
        self.path = []
        self.start = self.get_coordinates('start')
        self.goal = self.get_coordinates('end')


    def set_table(self, table):
        self.table = table
        self.__init__(table)

    
    def get_table(self):
        return(self.table)

    
    def get_coordinates(self, search):
        for i, line in enumerate(self.table):
            try:
                return (i, line.index(search))
            except:
                pass
