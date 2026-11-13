"""Bayesian end-member mixing model for stream carbon fractions."""

from dataclasses import dataclass
from typing import Sequence

import numpy as np


@dataclass
class EndMember:
    name: str
    delta13c: float
    delta14c: float
    uncertainty: float


class BayesianMixer:
    """Estimate fractional contributions of dissolved carbon end members."""

    def __init__(self, end_members: Sequence[EndMember], iterations: int = 2000):
        if len(end_members) < 2:
            raise ValueError("at least two end members are required")
        self.end_members = list(end_members)
        self.iterations = iterations

    def _log_likelihood(self, fractions: np.ndarray, observation: np.ndarray) -> float:
        predicted = np.zeros_like(observation, dtype=float)
        for weight, member in zip(fractions, self.end_members):
            predicted += weight * np.array([member.delta13c, member.delta14c])
        residual = observation - predicted
        sigma = max(self.end_members[0].uncertainty, 1e-9)
        return -0.5 * float(np.sum((residual / sigma) ** 2))

    def sample(self, observations: np.ndarray, seed: int = 0) -> np.ndarray:
        rng = np.random.default_rng(seed)
        n = len(self.end_members)
        draws = rng.dirichlet(np.ones(n), size=self.iterations)
        weights = np.zeros(self.iterations)
        for i, fractions in enumerate(draws):
            weights[i] = self._log_likelihood(fractions, observations)
        weights -= weights.max()
        posterior = np.exp(weights)
        posterior /= posterior.sum()
        return draws[np.argmax(posterior)]

    def posterior_mean(self, observations: np.ndarray, seed: int = 0) -> np.ndarray:
        fractions = self.sample(observations, seed=seed)
        return fractions / fractions.sum()
