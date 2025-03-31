import pytest
from ..Queue import Queue

@pytest.mark.parametrize('num, valores', {
    (5, (1,2,3,4,5)),
    (10, (1,2,3,4,5,6,7,8,9,10))
})
def test_queue(num: int, valores: list[int]):
    q = Queue(num)
    assert q.is_empty() == True
    assert q.is_full() == False

    for value in valores:
        q.enqueue(value)

    assert q.is_empty() == False
    assert q.is_full() == True

    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.dequeue() == 5