"""Analyse the relationship between strap tension, pressure, and correction."""

from pathlib import Path

import matplotlib

# Use a non-interactive backend so the script also runs on headless systems.
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress

DATA_PATH = Path("data") / "processed" / "P2_donnees.tab"
RESULTS_DIR = Path("results")
FIGURES_DIR = Path("figures")

# Each dependent variable is modelled as a linear function of strap tension.
MODELS = [
    ("Pression_thor", "Pression thoracique", "kPa"),
    ("Pression_lomb", "Pression lombaire", "kPa"),
    ("Angle_Cobb_thor", "Angle de Cobb thoracique", "°"),
    ("Angle_Cobb_lomb", "Angle de Cobb lombaire", "°"),
]

PRESSURE_MODELS = MODELS[:2]
COBB_MODELS = MODELS[2:]


def fit_linear_models(df: pd.DataFrame) -> pd.DataFrame:
    """Fit one linear regression per response variable against strap tension."""
    rows = []
    for variable, label, unit in MODELS:
        x = df["Tension"]
        y = df[variable]
        fit = linregress(x, y)

        # linregress returns r; R^2 is the coefficient of determination.
        r_squared = fit.rvalue**2
        if r_squared < 1:
            t_statistic = fit.rvalue * np.sqrt((len(df) - 2) / (1 - r_squared))
        else:
            t_statistic = np.inf

        rows.append(
            {
                "response": variable,
                "label": label,
                "unit": unit,
                "slope": fit.slope,
                "intercept": fit.intercept,
                "r_squared": r_squared,
                "t_statistic": t_statistic,
                "p_value": fit.pvalue,  # Two-sided test of the slope.
                "n": len(df),
            }
        )
    return pd.DataFrame(rows)


def plot_regressions(
    df: pd.DataFrame,
    models: list[tuple[str, str, str]],
    title: str,
    y_label: str,
    output_path: Path,
) -> None:
    """Plot observations and fitted regression lines for a group of variables."""
    fig, ax = plt.subplots(figsize=(7, 4.5))

    for variable, label, unit in models:
        x = df["Tension"]
        y = df[variable]
        fit = linregress(x, y)
        r_squared = fit.rvalue**2

        ax.scatter(x, y, label=f"{label} (observations)")
        x_fit = np.linspace(x.min(), x.max(), 100)
        ax.plot(
            x_fit,
            fit.intercept + fit.slope * x_fit,
            label=f"{label} : pente = {fit.slope:.3f} {unit}/N, R² = {r_squared:.3f}",
        )

    ax.set_title(title)
    ax.set_xlabel("Tension de sangle (N)")
    ax.set_ylabel(y_label)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)


def main() -> None:
    if not DATA_PATH.exists():
        raise SystemExit(
            f"Processed data not found at {DATA_PATH}. Run scripts/preprocess.py first."
        )

    df = pd.read_csv(DATA_PATH, sep="\t", encoding="utf-8-sig")
    df = df.apply(pd.to_numeric, errors="raise")

    results = fit_linear_models(df)

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    results.to_csv(RESULTS_DIR / "regression_results.csv", index=False)

    plot_regressions(
        df,
        PRESSURE_MODELS,
        "Pression appliquée par le corset en fonction de la tension",
        "Pression (kPa)",
        FIGURES_DIR / "pression_vs_tension.png",
    )
    plot_regressions(
        df,
        COBB_MODELS,
        "Angles de Cobb en fonction de la tension",
        "Angle de Cobb (°)",
        FIGURES_DIR / "cobb_vs_tension.png",
    )

    print(results.to_string(index=False, float_format=lambda value: f"{value:.4f}"))
    print(f"\nResults written to {RESULTS_DIR / 'regression_results.csv'}")
    print(f"Figures written to {FIGURES_DIR}")


if __name__ == "__main__":
    main()
