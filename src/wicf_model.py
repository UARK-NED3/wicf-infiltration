"""Screening model for buoyancy-driven WICF doorway exchange.

All temperatures are degrees C, pressure is Pa, enthalpy is kJ/kg dry air,
and load is kJ unless explicitly stated otherwise.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import exp, sqrt

G = 9.80665  # m/s2
R_DA = 287.055  # J/(kg K)
P_ATM = 101325.0  # Pa


@dataclass(frozen=True)
class AirState:
    temperature_c: float
    relative_humidity_pct: float
    pressure_pa: float = P_ATM


@dataclass(frozen=True)
class Doorway:
    width_m: float = 0.90
    height_m: float = 2.10
    discharge_coefficient: float = 0.60
    effective_exchange_multiplier: float = 0.40
    establishment_time_s: float = 3.0


def saturation_vapor_pressure_pa(temperature_c: float) -> float:
    """Buck-like saturation-pressure approximation, valid here for screening."""
    if temperature_c >= 0.0:
        return 611.21 * exp((18.678 - temperature_c / 234.5) * temperature_c / (257.14 + temperature_c))
    return 611.15 * exp((23.036 - temperature_c / 333.7) * temperature_c / (279.82 + temperature_c))


def humidity_ratio(state: AirState) -> float:
    vapor_pressure = state.relative_humidity_pct / 100.0 * saturation_vapor_pressure_pa(state.temperature_c)
    return 0.621945 * vapor_pressure / (state.pressure_pa - vapor_pressure)


def moist_air_enthalpy_kj_per_kg_da(state: AirState) -> float:
    w = humidity_ratio(state)
    return 1.006 * state.temperature_c + w * (2501.0 + 1.86 * state.temperature_c)


def moist_air_density_kg_per_m3(state: AirState) -> float:
    """Density of moist air, using dry-air partial pressure plus water-vapor pressure."""
    p_v = state.relative_humidity_pct / 100.0 * saturation_vapor_pressure_pa(state.temperature_c)
    p_da = state.pressure_pa - p_v
    return p_da / (R_DA * (state.temperature_c + 273.15)) + p_v / (461.495 * (state.temperature_c + 273.15))


def established_exchange_mass_flow_kg_s(outer: AirState, inner: AirState, door: Doorway) -> float:
    """Cold-side outflow for a symmetric neutral-plane exchange approximation.

    This is an analytical integration from the sill to H/2 of hydrostatic
    pressure difference. It is not a calibrated doorway-flow correlation.
    """
    rho_outer = moist_air_density_kg_per_m3(outer)
    rho_inner = moist_air_density_kg_per_m3(inner)
    if rho_inner <= rho_outer:
        return 0.0
    half_height = door.height_m / 2.0
    integral = (2.0 / 3.0) * half_height ** 1.5
    return (
        door.effective_exchange_multiplier
        * door.discharge_coefficient
        * door.width_m
        * rho_inner
        * sqrt(2.0 * G * (rho_inner - rho_outer) / rho_inner)
        * integral
    )


def exchange_ramp_factor(open_time_s: float, establishment_time_s: float) -> float:
    """Mean flow fraction for a linear 0-to-1 ramp over establishment time."""
    if open_time_s <= 0:
        return 0.0
    if open_time_s < establishment_time_s:
        return open_time_s / (2.0 * establishment_time_s)
    return 1.0 - establishment_time_s / (2.0 * open_time_s)


def door_open_load_kj(outer: AirState, inner: AirState, door: Doorway, open_time_s: float) -> float:
    """Refrigeration load from incoming outdoor/room air for one door-open event."""
    delta_h = max(0.0, moist_air_enthalpy_kj_per_kg_da(outer) - moist_air_enthalpy_kj_per_kg_da(inner))
    mass_flow = established_exchange_mass_flow_kg_s(outer, inner, door)
    dry_air_fraction = 1.0 / (1.0 + humidity_ratio(outer))
    exchanged_moist_air = mass_flow * open_time_s * exchange_ramp_factor(open_time_s, door.establishment_time_s)
    return exchanged_moist_air * dry_air_fraction * delta_h
