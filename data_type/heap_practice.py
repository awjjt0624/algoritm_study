class HeapPractice():
    def __init__(self):
        self.heap = []
        self.heap.append(None)

    # 해당 노드가 부모 노드보다 큰지 비교
    def check_swap_up(self, idx):
        # 삽입한 모드의 부모 노드가 없을 경우
        if idx <= 1:
            return False

        parent_idx = idx // 2

        if self.heap[idx] > self.heap[parent_idx]:
            return True
        else:
            return False

    # 데이터 삽입
    def insert(self, data):
        self.heap.append(data)
        idx = len(self.heap) - 1

        # check_swap_up() 의 값이 참이라면 부모와 위치 바꾸기
        while self.check_swap_up(idx):
            parent_idx = idx // 2

            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx

        return True


if __name__ == '__main__':

    test_input = [9, 1, 10, 3, 4, 8]
    heap_practice = HeapPractice()
    for t in test_input:
        heap_practice.insert(t)
    print(heap_practice.heap)
