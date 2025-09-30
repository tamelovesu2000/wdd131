from pytest import approx
import pytest
from water_flow import (
    water_column_height,
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction,
    kpa_to_psi # Added for enhancement testing
)


def test_water_column_height():
    """Verify water_column_height works correctly."""
    # Test cases from project instructions:
    # (tower_height, tank_height) -> Expected water column height
    assert water_column_height(0.0, 0.0) == approx(0.0)
    assert water_column_height(0.0, 10.0) == approx(7.5)
    assert water_column_height(25.0, 0.0) == approx(25.0)
    assert water_column_height(48.3, 12.8) == approx(57.9)


def test_pressure_gain_from_water_height():
    """Verify pressure_gain_from_water_height works correctly."""
    # Test cases from project instructions:
    # (height) -> Expected Pressure (kPa)
    assert pressure_gain_from_water_height(0.0) == approx(0.0, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)


def test_pressure_loss_from_pipe():
    """Verify pressure_loss_from_pipe works correctly."""
    # Test cases from project instructions:
    # (d, L, f, v) -> P (kPa)
    assert pressure_loss_from_pipe(0.048692, 0.000, 0.018, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)


def test_pressure_loss_from_fittings():
    """Verify pressure_loss_from_fittings works correctly."""
    # Test cases from project instructions:
    # (v, n) -> P (kPa)
    assert pressure_loss_from_fittings(0.0, 3) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)


def test_reynolds_number():
    """Verify reynolds_number works correctly."""
    # Test cases from project instructions:
    # (d, v) -> R
    assert reynolds_number(0.048692, 0.00) == approx(0, abs=1)
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert reynolds_number(0.286870, 1.65) == approx(471729, abs=1)
    assert reynolds_number(0.286870, 1.75) == approx(500318, abs=1)


def test_pressure_loss_from_pipe_reduction():
    """Verify pressure_loss_from_pipe_reduction works correctly."""
    # Test cases from project instructions:
    # (D, v, R, d) -> P (kPa)
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)


def test_kpa_to_psi():
    """Verify kpa_to_psi works correctly (Enhancement)."""
    # Test cases using the conversion factor (0.145038)
    assert kpa_to_psi(0.0) == approx(0.0, abs=0.001)
    assert kpa_to_psi(6.89476) == approx(1.0, abs=0.01) # Approx 6.89476 kPa = 1 psi
    assert kpa_to_psi(100.0) == approx(14.504, abs=0.001)
    assert kpa_to_psi(158.7) == approx(23.0, abs=0.1)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
