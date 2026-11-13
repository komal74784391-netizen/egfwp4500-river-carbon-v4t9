"""Catchment-scale carbon export integration."""

from dataclasses import dataclass

import numpy as np


@dataclass
class CatchmentFluxModel:
    area_km2: float
    runoff_mm: float

    def dissolved_export(self, concentration_mg_l: np.ndarray) -> np.ndarray:
        """Return monthly dissolved carbon export in kg (concentration in mg/L)."""
        discharge_m3 = self.runoff_mm * 1e-3 * self.area_km2 * 1e6 / 12.0
        return concentration_mg_l * 1e-6 * discharge_m3 * 1e3

    def annual_budget(self, monthly_concentration: np.ndarray) -> float:
        if monthly_concentration.size != 12:
            raise ValueError("expected twelve monthly concentrations")
        return float(np.sum(self.dissolved_export(monthly_concentration)))
