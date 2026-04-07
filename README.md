# Collatz Conjecture: Numerical Analysis & 90,902-Digit Integrity Deficit

This repository contains a suite of **CUDA-accelerated kernels** and high-precision verification scripts designed to analyze the bit-density degradation and numerical stability of the Collatz Conjecture at extreme scales.

The research identifies a specific **Integrity Deficit of 90,902 digits** using High-Performance Computing (HPC) methods, exploring the boundary where Diophantine approximations and GPU floating-point precision limits intersect.

## 🚀 Research Overview

The project is based on the **Law of Dissipation**, which suggests that any high-energy integer (high bit density) inevitably decays toward a thermal equilibrium ($\rho \approx 0.5$). By using the RTX 3060 architecture, we have scanned for resonance zones where the balance between $L$ (even steps) and $k$ (odd steps) reaches critical thresholds.

### Key Discovery
- **Critical Resonance:** Identification of a 90,902-digit deficit in the balance equation $2^L - 3^k$.
- **Dissipation Constant ($\lambda$):** Statistical validation of the universal decay constant across massive datasets.

## 📂 Repository Structure

| File | Description |
| :--- | :--- |
| `cuda_resonance_precision_verifier.py` | **Main Script:** GPU-based resonance search followed by 200-dps verification. |
| `cuda_critical_zone_scanner.py` | Massively parallel scanner for Diophantine critical points using PyTorch/CUDA. |
| `cuda_resistance_stress_test.py` | Identifies "worst-case" numbers with maximum survival margin. |
| `visualize_decay_law.py` | Generates the dissipation trajectory and the "Escape Threshold" plot. |
| `steiner_lagarias_algebraic_analysis.py` | Algebraic verification of the Steiner-Lagarias equation for non-trivial cycles. |
| `cuda_parallel_drift_kernel.py` | Numba-accelerated kernel for simultaneous drift analysis of 10^5 integers. |

## 🛠️ Requirements

- **GPU:** NVIDIA RTX 30 Series or higher (Tested on RTX 3060 12GB).
- **Environment:**
  - Python 3.9+
  - CUDA Toolkit 11.x/12.x
  - `torch` (PyTorch)
  - `numba`
  - `mpmath` (for high-precision verification)
  - `matplotlib` & `numpy`

## 📊 How to Run

1. **Verify the 90k Digit Deficit:**
   ```bash
   python cuda_resonance_precision_verifier.py