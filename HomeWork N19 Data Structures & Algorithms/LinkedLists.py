class Node:
    def __init__(self, data=None):  # როდესაც კვანძს ვქმნით მას რაღაც მონაცემი უნდა ჰქონდეს და ის უნა იყოს ნანი
        self.data = data
        self.next = None  # ნექსთიც მომდევნო კვანძის ჰედი გამოდის, რომელიც თავიდან ასევე ნალ მნიშვნელობის ტიპისა


class LinkedList:
    def __init__(self):
        self.head = None  # ეს არის კვანძის ჰედერი რომელიც საწყისი არის ამ კვანძის და არი ნულ ტიპის ასევე

    def append(self, data):  # მეთოდი რომელიც ლისტის ბოლოში ამატებს დატას
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head  # აქ ვამოწმებთ ამ ნოუდს თუ აქ ბოლო ელემენტი სადაც დატა იქნება
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def remove(self, data):  # მოკლედ ეს არის წაშლის მეთოდი რომელიც იშლება არა ინდექსით, არამედ გადაცემული Date თი
        if self.head is None:  # აქ თავიდანვე ვამოწმებ, რომ თუ ეს ჯაჭვი თავიდანვე ცარიელია, გააჩეროს იგი
            return

        if self.head.data == data:  # აქ ვამოწმებ, არის თუ არა საწყის ნოუდში მონაცემი, რათა იგი მომდევნო მონაცემით
            # შევავსო
            self.head = self.head.next  # აქ რაც ხდება ზემოთაც ვახსენე უკვე
            return

        current_node = self.head  # აქ ამჟამინდელი ნოუდი ჰედი ანუ ნანი ხდება
        while current_node.next:  # მანამ სანამ გვაქ შემდეგი ნოუდი
            if current_node.next.data == data:  # ამოწმებს მომდევნო კვანძის მონაცემს
                current_node.next = current_node.next.next  # აკავშირებს მიმდინარე კვანძს შემდეგ კვანძთან
                return
            current_node = current_node.next  # ამჟამინდელი ნოუდის დათა უნდა გახდეს შემდეგი

    def display(self):  # დისპლეის დახმარებით შეგვიძლია დავინახოთ ჩვენი ნოუდი როგორ აირს აწყობილი
        current_node = self.head
        while current_node is not None:  # აქ ვამოწმებთ მანამ სანამ ცარიელი ნოუის უჯრა არა დაპრინტოს => - ეს
            # თვალსაჩინოებისთვის
            print(current_node.data, end=' => ')
            current_node = current_node.next  # აქ კიდევ ვეუბნევით, რომ ბოლო ნოუდი უნდა გახდეს შემდეგი ნოუდი,
            # მანამ სანამ ნან გახდება


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
print(linked_list.display())

linked_list.remove(2)
print("\nAfter removing 2:")
linked_list.display()
