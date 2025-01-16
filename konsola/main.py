from random import randint

class SortableList:
    def __init__(self, values:list) -> None:
        self._list:list = values

    def selection_sort(self,descending:bool=True) -> None:
        if len(self._list) <= 1:
            print(f"List too short to sort, length = {len(self._list)}")
            return

        if descending:
            for index in range(len(self._list)):
                minIndex = index

                for comparingIndex in range(index+1, len(self._list)):
                    if self._list[comparingIndex] > self._list[minIndex]:
                        minIndex = comparingIndex

                self._list[index], self._list[minIndex] = self._list[minIndex], self._list[index]
        else:
            for index in range(len(self._list)):
                minIndex = index

                for comparingIndex in range(index+1, len(self._list)):
                    if self._list[comparingIndex] < self._list[minIndex]:
                        minIndex = comparingIndex

                self._list[index], self._list[minIndex] = self._list[minIndex], self._list[index]

    def highest_value(self) -> int:
        self.selection_sort()
        return self.get_list()[0]

    def get_list(self) -> list:
        return self._list
    
    def set_list(self, values:list) -> None:
        self._list = values

if __name__ == "__main__":
    list1:SortableList = SortableList([randint(1,100) for i in range(10)])
    list1.selection_sort()
    print(list1.get_list())
    print(list1.highest_value())