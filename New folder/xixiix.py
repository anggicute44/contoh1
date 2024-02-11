
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLLNC:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            AAA = self.head
            while AAA.next:
                AAA = AAA.next
            AAA.next = new_node

    def LIST(self, LIST):
        AAA = self.head
        KATA = []
        while AAA:
            KATA.append(AAA.data)
            AAA = AAA.next
        for index in LIST:
            if index <= len(KATA):
                print(KATA[index - 1], end=" ")
        print()

def main():
    linked_list = SLLNC()
    KATA= input("Masukkan kata-kata: ").split()
    
    for word in KATA:
        linked_list.insert(word)

    indices = list(map(int, input("Masukkan no urut: ").split()))
    print("Hasil:", end=" ")
    linked_list.LIST(indices)

if __name__ == "__main__":
    main()
