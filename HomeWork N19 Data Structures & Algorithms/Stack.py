class Node: # ვქმნით კლასს ნოუდს რომლის დატა და შემდეეგი ელემენტი ნანი იქნება როგორც ეს ლინკდლისტების დროს იყო
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack: # აქ ვქმნით კლას სტოკს სადაც ტოპ ნოუდი ნანი გვექნება და ამ სტექის სიგრძეც ასევე 0 იქნება თავიდანვე და შემდეგში თუ რამეს დავამატებთ ამასაც გავზრდით
    def __init__(self):
        self.top_node = None
        self.length = 0

    def empty(self): # ეს არის ცარიელი მეთოდი რითიც ვამოწმებთ ატის თუ არა ჩვენი ტოპ ნოუდი ანუ ბოლოს დამატრბული  ელემნეტი თავიდან ცარიელი
        return self.top_node is None

    def size(self): # ეს არის სიგრძის მეთოდი, რომლითაც სტექის სიგრძეს ვაბრუნებთ
        return self.length

    def push(self, data): # ეს არის სტექის ასე ვთქვათ ჯაჭვში აითემის დამატების მეთოდი
        new_node = Node(data) # თავიდან ვქმინთ ახალ ცვლადს სადაც შევინახავთ დათას
        new_node.next = self.top_node # აქ მომდევნო დათა არის სტაკის ტოპ ნოუდი უკვე
        self.top_node = new_node # და უკვე ახალ დამატებული დათა ხდება უკვე ტოპ ნოუდის დათა
        self.length += 1 # აქ კიდე სიგრძეს ვზრდით იმიტომ რომ სტაქის ჯაჭვი გაგვეზარდოს +1
        return new_node # აქ ვაბურნებთ ამ ნოუდს

    def top(self): # ეს არის ტოპ მეთოდი რომელიც ამოწმებს გვაქ თუ არა ტოპ სტაკიქს დატა
        if not self.empty():
            return self.top_node.data
        else:
            raise IndexError('Stack is empty') # თუ არა ერორი აღძრას

    def pop(self): # ეს არის წაკითხვა ამოშლისი მეთოდი
        if not self.empty(): # თუ ცარიელი არა
            popped_item = self.top_node.data # წაკითხული დატა უნდა ამოიშალოს
            self.top_node = self.top_node.next # და წაკითხული დატას წინ მდებარე დატა უნდა გახდეს ტოპ ნოუდი
            self.length -= 1 # აქ კიდე სტაქის ჯაჭვს ვაკლებთ -1 სიგრძეში ეს ერთი დატა არი რომლეიც ყველაზე პირველი დაემატა და წაიშალა
            return popped_item # აქ ამ წაკითხულ დათას ვაბრუნებთ
        else:
            raise IndexError('Stack is empty') # და თუ აღარ დაგვრჩა ამ სტაქში დატა, ვძრავთ შეცდომას რომ არ დაგვრჩა დატა სტაკის ჯაჭვში


stack = Stack()

print(f'Stack is empty: {stack.empty()}')
print(f'Stack size: {stack.size()}')

stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)

print(f'Stack is empty: {stack.empty()}')
print(f'Stack size: {stack.size()}')

print(stack.pop())
print(f'Stack size: {stack.size()}')
print(stack.pop())
print(f'Stack size: {stack.size()}')