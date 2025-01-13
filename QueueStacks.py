class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            self.stack2.pop()

    def front(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2[-1]
        return None


def process_queries(queries):
    queue = QueueUsingTwoStacks()
    results = []

    for query in queries:
        if query[0] == 1:  
            queue.enqueue(query[1])
        elif query[0] == 2:  
            queue.dequeue()
        elif query[0] == 3:  
            results.append(queue.front())

    return results


q = int(input())  
queries = []
for i in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

result = process_queries(queries)

for res in result:
    print(res)
