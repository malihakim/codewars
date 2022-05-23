class PaginationHelper:
    
    def __init__(self, collection, items_per_page):
        self.collection = collection                  
        self.items = items_per_page                 
      
    def item_count(self):                            
        return len(self.collection)

    def page_count(self):
        if self.item_count()%self.items == 0:       
            return self.item_count()//self.items            #8//4 = 2      
        else:
            return (self.item_count()//self.items) + 1      #6//4 = 1+1 = 2

    #returns the number of items on the current page
    def page_item_count(self, page_index):
        if page_index >= self.page_count() or page_index < 0:   #4 or page5 > 2 pages or page -7
            return -1
        elif page_index == self.page_count() - 1:               #last page[3 or 4th page == 4-1 pages](page index starting from 0 == total pages - 1)  
            return self.item_count()%self.items  or self.items  # ***
        else:                                                   #every other page
            return self.items
 
#*** -  return _ or _: returns first _ unless False, 0, None, ''
#       return 8%4 == 0 or [4]
#       return [6%4 == 2] or 4
#       if divisible = 0, return items
#       if no divisible, return remainder

    def page_index(self, item_index):
        if item_index >= self.item_count() or item_index < 0:   #lower or higher than number of items
            return -1
        else:                                                   #in range
            return item_index // self.items                     #2//4 = 0 - item 3 is on page 1
                                                                #5//4 = 1 - item 6 is on page 2 

        
            
helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)

print('Items in collection: ', helper.item_count())
print('Items per page : ', helper.items) 
print('Total pages: ', helper.page_count())
print('Page Index of Item 4 is: ', helper.page_index(3))
print('Items in page 1: ', helper.page_item_count(0))      
print('Items in page 2: ', helper.page_item_count(1))     
print('Items in page 4: ', helper.page_item_count(3))
print('Items in page -7: ', helper.page_item_count(-7))

