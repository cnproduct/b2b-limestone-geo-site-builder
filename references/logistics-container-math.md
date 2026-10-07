# Natural Stone Heavy Cargo Container Logistics & Packing Math

天然石材属于国际海运中的典型**重货（Heavy Cargo / Deadweight Cargo）**。集装箱的装载瓶颈永远是**重量上限（Weight Limit）**，而非体积（Volume）。

---

## 1. 物理常数与重量推导模型

1. **石灰石密度基准值 ($\rho$):**
   天涯高密度海相生物碎屑石灰石实测体积密度为：
   $$\rho = 2,620 \text{ kg/m}^3 = 2.62 \text{ g/cm}^3$$
2. **单位面积净重公式:**
   $$\text{Weight per } \text{m}^2 = \rho \times \text{Thickness (m)}$$
   - **$20\text{ mm}$ 厚度标板:** $2,620 \times 0.02 = \mathbf{52.4 \text{ kg/m}^2}$
   - **$30\text{ mm}$ 厚度厚板:** $2,620 \times 0.03 = \mathbf{78.6 \text{ kg/m}^2}$
   - **$15\text{ mm}$ 厚度室内板:** $2,620 \times 0.015 = \mathbf{39.3 \text{ kg/m}^2}$

---

## 2. 20GP 集装箱载重规范与港口限重要求

国际标准 20 尺普柜（20' GP）内部容积约为 $33.1\text{ m}^3$，最大理论载重为 $28,180\text{ kg}$。然而在实际外贸操作中，受到国内公路限重、厦门港装载安全规程及目的港公路限重要求（如美国公路 44,000 lbs 限重，澳洲公路 26t 限重）：

- **厦门港标准配载毛重上限:** **$26,500\text{ kg} \sim 27,000\text{ kg}$**（含集装箱自重及木托木架皮重）。
- **熏蒸出口木箱皮重 (Crate Tare Weight):** 约 $50\text{ kg} \sim 60\text{ kg}$/箱（符合 ISPM 15 热处理标准，带高强度钢带及防潮内衬膜）。

---

## 3. 标准装箱与单柜装载量核算

| 石材厚度 | 单木箱装载面积 (m²/crate) | 单箱毛重 (含木架) | 单柜最多装载木箱数 (20GP) | 单柜实际装载面积 (m²/20GP) | 单柜总毛重 (Gross Weight) |
|---|---|---|---|---|---|
| **20 mm** | 22 – 24 m² | ~1,200 – 1,300 kg | **20 – 21 箱** (两层地铺排布) | **480 – 504 m²** | ~26,200 – 26,800 kg |
| **30 mm** | 15 – 16 m² | ~1,220 – 1,300 kg | **20 – 21 箱** | **315 – 336 m²** | ~26,100 – 26,700 kg |
| **法式四拼 (20mm)** | 23.04 m² (16套) | ~1,260 kg | **21 箱** (336套) | **483.84 m²** | ~26,460 kg |

---

## 4. 自动化测算 CLI：`scripts/design_math.py stone-container`

系统内置了标准库 Python 测算工具，直接输出项目级配载方案：

```bash
# 测算 500 平方米 20mm 谷雨滚磨石板所需集装箱：
$ python3 scripts/design_math.py stone-container --area 500 --thickness 20

# 输出：
{
  "input_specification": {
    "requested_area_m2": 500.0,
    "thickness_mm": 20.0,
    "density_kg_m3": 2620.0,
    "unit_weight_kg_m2": 52.4
  },
  "packaging_summary": {
    "total_crates": 21,
    "m2_per_crate": 24.0,
    "total_net_stone_weight_kg": 26200.0,
    "total_gross_weight_kg": 27250.0,
    "total_stone_volume_m3": 10.0
  },
  "shipping_estimates": {
    "required_20gp_containers": 2,
    "limiting_factor": "Weight (Heavy Cargo Limit)",
    "weight_utilization_pct": 51.4,
    "max_safe_m2_per_single_20gp": 486,
    "export_port": "Xiamen International Port (28 km from Shuitou factory)"
  }
}
```
