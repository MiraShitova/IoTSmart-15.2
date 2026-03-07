import pytest

def get_pump_status(soil_moisture):
    """
    Повертає статус насоса залежно від вологості ґрунту.
    Логіка відповідає правилу simulation.rules: < 50% = ON, >= 50% = OFF.
    """
    if soil_moisture < 50.0:
        return "ON"
    else:
        return "OFF"

def test_pump_on_when_dry():
    assert get_pump_status(40.0) == "ON"

def test_pump_off_when_wet():
    assert get_pump_status(60.0) == "OFF"

def test_pump_threshold_boundary():
    assert get_pump_status(50.0) == "OFF"

def test_pump_very_dry():
    assert get_pump_status(0.0) == "ON"

def test_moisture_type_handling():
    with pytest.raises(TypeError):
        get_pump_status("не число")