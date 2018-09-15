
#main controller for all e-commerce crawler
#Used to sort and modify scraped data so that user could modify the ui search
class process:
    def __init__(self,searchTerm):
        searchTerm=""

    def searching(self, searchTerm):
        self.searchTerm=searchTerm

    def getSearchTerm(self):
        return self.searchTerm
    

    


