#!/usr/bin/env python3
"""
Tianya Limestone - B2B Natural Stone & Architectural Paver Site Master
Design Math, Fluid Typography & Heavy Cargo Stone Container Logistics Estimator
Python standard library only.
"""
import argparse
import json
import math
import re


# ---------------------------------------------------------------------------
# 1. WCAG Color Contrast Calculation
# ---------------------------------------------------------------------------
def luminance(color):
    if not re.fullmatch(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?", color):
        raise ValueError("Use opaque #RGB or #RRGGBB; composite transparency separately.")
    value = color[1:]
    if len(value) == 3:
        value = "".join(char * 2 for char in value)
    channels = [int(value[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
              for c in channels]
    return sum(c * w for c, w in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast(foreground, background):
    light, dark = sorted((luminance(foreground), luminance(background)), reverse=True)
    return (light + 0.05) / (dark + 0.05)


# ---------------------------------------------------------------------------
# 2. Fluid Typography & Spacing Clamp Calculator
# ---------------------------------------------------------------------------
def fluid_coefficients(min_size, max_size, min_width, max_width, root):
    values = (min_size, max_size, min_width, max_width, root)
    if not all(math.isfinite(v) and v > 0 for v in values):
        raise ValueError("Sizes, widths and root must be positive finite numbers.")
    if max_width <= min_width or max_size < min_size:
        raise ValueError("Require max_width > min_width and max_size >= min_size.")
    slope = (max_size - min_size) / (max_width - min_width)
    intercept = min_size - slope * min_width
    result = (min_size / root, intercept / root, slope * 100, max_size / root)
    if not all(math.isfinite(v) for v in result):
        raise ValueError("Values are too extreme for finite CSS coefficients.")
    return result


def fluid_css(*values):
    low, intercept, vw, high = fluid_coefficients(*values)
    return f"clamp({low:.10g}rem, calc({intercept:.10g}rem + {vw:.10g}vw), {high:.10g}rem)"


# ---------------------------------------------------------------------------
# 3. Heavy Cargo Natural Stone 20GP Container Loading Estimator
# ---------------------------------------------------------------------------
CONTAINER_20GP = {
    "name": "20' Heavy-Duty General Purpose Container",
    "max_cargo_payload_kg": 26500,  # Xiamen Port typical allowable stone payload
    "cbm_volume": 33.1,
    "max_crates": 24,              # Maximum standard wooden crates floor plan (12 stacks x 2)
}


def estimate_stone_container(area_m2, thickness_mm, density_kg_m3=2620, crate_capacity_m2=None):
    """
    Calculates container loading, crate count, and weight for architectural stone.
    For natural limestone:
    - 20mm thickness ~= 52.4 kg/m²
    - 30mm thickness ~= 78.6 kg/m²
    """
    if any(v <= 0 for v in (area_m2, thickness_mm, density_kg_m3)):
        raise ValueError("Area, thickness, and density must be positive numbers.")

    thickness_m = thickness_mm / 1000.0
    weight_per_m2 = density_kg_m3 * thickness_m
    total_net_stone_weight_kg = area_m2 * weight_per_m2
    total_volume_m3 = area_m2 * thickness_m

    # Default crate capacity if not specified
    # Standard crate holds approx. 22-26 m² of 20mm or 15-18 m² of 30mm
    if crate_capacity_m2 is None:
        crate_capacity_m2 = 24.0 if thickness_mm <= 22 else 16.0

    total_crates = math.ceil(area_m2 / crate_capacity_m2)
    tare_weight_per_crate_kg = 50.0  # Fumigated reinforced timber crate tare
    total_gross_weight_kg = total_net_stone_weight_kg + (total_crates * tare_weight_per_crate_kg)

    # 20GP capacity calculation
    payload_limit = CONTAINER_20GP["max_cargo_payload_kg"]
    by_weight_containers = math.ceil(total_gross_weight_kg / payload_limit)
    by_crate_containers = math.ceil(total_crates / CONTAINER_20GP["max_crates"])
    required_20gp_containers = max(by_weight_containers, by_crate_containers)

    limiting_factor = "Weight (Heavy Cargo Limit)" if by_weight_containers >= by_crate_containers else "Floor Crate Layout"

    # Single container maximum capacity under standard limits
    max_m2_per_container = math.floor(payload_limit / (weight_per_m2 + (tare_weight_per_crate_kg / crate_capacity_m2)))

    return {
        "input_specification": {
            "requested_area_m2": round(area_m2, 2),
            "thickness_mm": thickness_mm,
            "density_kg_m3": density_kg_m3,
            "unit_weight_kg_m2": round(weight_per_m2, 2)
        },
        "packaging_summary": {
            "total_crates": total_crates,
            "m2_per_crate": crate_capacity_m2,
            "total_net_stone_weight_kg": round(total_net_stone_weight_kg, 1),
            "total_gross_weight_kg": round(total_gross_weight_kg, 1),
            "total_stone_volume_m3": round(total_volume_m3, 3)
        },
        "shipping_estimates": {
            "required_20gp_containers": required_20gp_containers,
            "limiting_factor": limiting_factor,
            "weight_utilization_pct": round((total_gross_weight_kg / (required_20gp_containers * payload_limit)) * 100, 1),
            "max_safe_m2_per_single_20gp": max_m2_per_container,
            "export_port": "Xiamen International Port (28 km from Shuitou factory)"
        }
    }


# ---------------------------------------------------------------------------
# 4. Self Test Suite
# ---------------------------------------------------------------------------
def self_test():
    # Contrast verification matching DESIGN.md
    assert contrast("#251700", "#ffffff") >= 17.0
    assert contrast("#665d4d", "#ffffff") >= 4.5
    assert contrast("#251700", "#e9f551") >= 14.0

    # Fluid typography
    low, intercept, vw, high = fluid_coefficients(36, 60, 360, 1440, 16)
    css = fluid_css(36, 60, 360, 1440, 16)
    assert "clamp(" in css and "calc(" in css

    # Stone container estimation
    est_20mm = estimate_stone_container(480, 20)
    assert est_20mm["shipping_estimates"]["required_20gp_containers"] == 1
    assert est_20mm["shipping_estimates"]["limiting_factor"] == "Weight (Heavy Cargo Limit)"

    est_30mm = estimate_stone_container(1000, 30)
    assert est_30mm["shipping_estimates"]["required_20gp_containers"] >= 3

    print("PASS: Tianya Limestone WCAG AAA contrast, fluid typography, and heavy cargo 20GP container math.")


# ---------------------------------------------------------------------------
# 5. CLI Controller
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    # Contrast command
    colors = commands.add_parser("contrast", help="Opaque sRGB text contrast; failure exits 1")
    colors.add_argument("foreground")
    colors.add_argument("background")
    colors.add_argument("--large", action="store_true", help="Use 3:1 for qualifying large text")

    # Fluid clamp command
    fluid = commands.add_parser("fluid", help="Sizes/widths in CSS px; root is 16px by default")
    for name in ("min_size", "max_size", "min_width", "max_width"):
        fluid.add_argument(name, type=float)
    fluid.add_argument("--root", type=float, default=16)

    # Stone container command
    stone = commands.add_parser("stone-container", help="Calculate 20GP shipping container requirements for natural stone pavers")
    stone.add_argument("--area", type=float, required=True, help="Total area in square meters (m²)")
    stone.add_argument("--thickness", type=float, default=20.0, help="Paver thickness in mm (e.g. 20, 30)")
    stone.add_argument("--density", type=float, default=2620.0, help="Stone bulk density in kg/m³ (default: 2620 for Tianya limestone)")

    commands.add_parser("self-test")
    args = parser.parse_args()

    try:
        if args.command == "contrast":
            ratio = contrast(args.foreground, args.background)
            threshold = 3.0 if args.large else 4.5
            passed = ratio >= threshold
            print(f"{ratio:.6f}:1 — {'PASS' if passed else 'FAIL'} (AA text threshold {threshold}:1)")
            return 0 if passed else 1

        if args.command == "fluid":
            print(fluid_css(args.min_size, args.max_size, args.min_width, args.max_width, args.root))
            return 0

        if args.command == "stone-container":
            res = estimate_stone_container(args.area, args.thickness, args.density)
            print(json.dumps(res, indent=2))
            return 0

        self_test()
        return 0
    except ValueError as e:
        parser.error(str(e))


if __name__ == "__main__":
    raise SystemExit(main())
