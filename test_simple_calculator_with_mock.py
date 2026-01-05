import pytest
from simple_calculator import SimpleCalculator
from unittest.mock import Mock

def test_add_with_mock_history_service():
    mock_history = Mock()
    
    calc = SimpleCalculator(history_service=mock_history)

    result = calc.add(5, 3)

    assert result == 8

    mock_history.save_operation.assert_called_once()
    mock_history.save_operation("add", 5, 3, 8)

def test_multiply_with_multiple_mocks():
    mock_history = Mock()
    
    calc = SimpleCalculator(history_service=mock_history)

    result = calc.multiply(5, 3)

    assert result == 15

    mock_history.save_operation.assert_called_once()
    mock_history.save_operation("multiply", 5, 3, 15)

def test_get_history_count_with_mock():
    pass