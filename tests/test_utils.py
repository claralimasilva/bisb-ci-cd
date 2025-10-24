import pytest
from app.utils import average_ticket, top_clients_by_revenue

def test_average_ticket_basic_case():
    services = [{"price": 100.0}, {"price": 200.0}, {"price": 300.0}]
    result = average_ticket(services)
    # média = (100 + 200 + 300) / 3 = 600 / 3 = 200
    assert result == 200.0

def test_average_ticket_raises_on_empty_list():
    with pytest.raises(ValueError):
        average_ticket([])

def test_average_ticket_raises_on_negative_price():
    with pytest.raises(ValueError):
        average_ticket([{"price": -50.0}])

def test_average_ticket_raises_on_missing_field():
    with pytest.raises(ValueError):
        average_ticket([{}])


def test_top_clients_by_revenue_basic():
    sales = [
        {"client_id": "Maria", "value": 200.0},
        {"client_id": "Joao",  "value": 150.0},
        {"client_id": "Maria", "value": 100.0},
        {"client_id": "Ana",   "value": 50.0},
    ]
    result = top_clients_by_revenue(sales, limit=2)
    # Maria = 300, Joao = 150, Ana = 50
    assert result == [("Maria", 300.0), ("Joao", 150.0)]

def test_top_clients_by_revenue_ignores_invalid_entries():
    sales = [
        {"client_id": "Maria", "value": 100.0},
        {"client_id": "Maria", "value": "bad"},  # ignora
        {"client_id": None,    "value": 999.0},  # ignora
        {"client_id": "Ana",   "value": -10.0},  # ignora
    ]
    result = top_clients_by_revenue(sales, limit=5)
    assert ("Maria", 100.0) in result
    # não deve ter cliente None nem valores negativos somados
    assert all(client_id is not None for client_id, _ in result)
