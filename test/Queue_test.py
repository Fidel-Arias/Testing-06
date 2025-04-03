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

def test_initialization():
    """Verifica que la cola se inicialice correctamente"""
    # TC-001: Creación con tamaño válido
    q = Queue(5)
    assert q.max == 5
    assert q.head == 0
    assert q.tail == 0
    assert q.size == 0
    assert len(q.data) == 5
    
    # TC-002: Creación con tamaño inválido (debe lanzar excepción)
    try:
        q = Queue(0)
        assert False, "Debería haber lanzado excepción"
    except AssertionError:
        assert True

def test_empty_full_conditions():
    """Verifica los métodos isEmpty e isFull en diferentes estados"""
    # TC-003: Cola recién creada está vacía
    q = Queue(3)
    assert q.is_empty()
    assert not q.is_full()
    
    # TC-004: Cola llena
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert not q.is_empty()
    assert q.is_full()
    
    # TC-005: Cola ni vacía ni llena
    q = Queue(3)
    q.enqueue(1)
    assert not q.is_empty()
    assert not q.is_full()

def test_enqueue_operations():
    """Verifica el comportamiento de enqueue"""
    # TC-006: Enqueue básico
    q = Queue(3)
    assert q.enqueue(10) == True
    assert q.size == 1
    assert q.tail == 1
    
    # TC-007: Enqueue hasta llenar
    q = Queue(2)
    q.enqueue(1)
    q.enqueue(2)
    try:
        q.enqueue(3)
        assert False, "Debería haber lanzado excepción"
    except:
        assert True
    
    # TC-008: Enqueue con wraparound
    q = Queue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue() # head ahora en 1
    q.enqueue(4) # tail debería volver a 0
    assert q.tail == 0
    assert q.size == 3

def test_dequeue_operations():
    """Verifica el comportamiento de dequeue"""
    # TC-009: Dequeue básico
    q = Queue(3)
    q.enqueue(10)
    q.enqueue(20)
    assert q.dequeue() == 10
    assert q.size == 1
    assert q.head == 1
    
    # TC-010: Dequeue en cola vacía
    q = Queue(2)
    try:
        q.dequeue()
        assert False, "Debería haber lanzado excepción"
    except:
        assert True
    
    # TC-011: Dequeue con wraparound
    q = Queue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    q.dequeue()
    q.enqueue(4)
    assert q.dequeue() == 3
    assert q.head == 2