# Restaurant Sales & Operations Dashboard

> Period: **30 Aug 2026 - 28 Sep 2026** | Data: `orders`, `order_items`, `menu`, `platforms`, `areas` (Dubai)
> Revenue figures use **Delivered** orders only. Net revenue = gross - platform commission.

![Net Revenue](https://img.shields.io/badge/Net%20Revenue-AED%20520,348-0F8B8D?style=for-the-badge&labelColor=1B2A49) ![Gross Sales](https://img.shields.io/badge/Gross%20Sales-AED%20622,663-1B2A49?style=for-the-badge&labelColor=0F8B8D) ![Commission](https://img.shields.io/badge/Commission-AED%20102,315-F0906A?style=for-the-badge&labelColor=1B2A49)
![Orders](https://img.shields.io/badge/Orders-6,336-1B2A49?style=for-the-badge&labelColor=0F8B8D) ![Cancel Rate](https://img.shields.io/badge/Cancel%20Rate-5.0%25-F0906A?style=for-the-badge&labelColor=1B2A49) ![Avg Order](https://img.shields.io/badge/Avg%20Order-AED%20103-0F8B8D?style=for-the-badge&labelColor=1B2A49)

---

## 1. Key Metrics

| Total Orders | Delivered | Cancelled | Cancel Rate | Gross Sales | Commission Paid | Net Revenue | Avg Order Value |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **6,336** | **6,020** | **316** | **5.0%** | **AED 622,663** | **AED 102,315** | **AED 520,348** | **AED 103** |

**Quick insights**
- Aggregators bring **69%** of delivered orders and carry **100%** of the commission bill: **AED 102,315** in total, or 16.4% of gross sales.
- Cancelled orders represent **AED 31,878** of lost gross sales.
- Peak ordering hour is **20:00**; the strongest day of the week is **Sat**.

---

## 2. Operations Speed (minutes, delivered orders)

| Avg Prep Time | Avg Dispatch-to-Delivery | Avg Order-to-Complete |
|:-:|:-:|:-:|
| **19.0** | **13.1** | **38.1** |

---

## 3. Sales Trend

```mermaid
%%{init: {"theme": "base", "themeVariables": {"xyChart": {"backgroundColor": "#FFF7F1", "titleColor": "#1B2A49", "xAxisLabelColor": "#1B2A49", "xAxisTitleColor": "#1B2A49", "xAxisTickColor": "#1B2A49", "xAxisLineColor": "#1B2A49", "yAxisLabelColor": "#1B2A49", "yAxisTitleColor": "#1B2A49", "yAxisTickColor": "#1B2A49", "yAxisLineColor": "#1B2A49", "plotColorPalette": "#0F8B8D"}}}}%%
xychart-beta
    title "Daily Net Revenue (AED)"
    x-axis ["30 Aug", "31 Aug", "01 Sep", "02 Sep", "03 Sep", "04 Sep", "05 Sep", "06 Sep", "07 Sep", "08 Sep", "09 Sep", "10 Sep", "11 Sep", "12 Sep", "13 Sep", "14 Sep", "15 Sep", "16 Sep", "17 Sep", "18 Sep", "19 Sep", "20 Sep", "21 Sep", "22 Sep", "23 Sep", "24 Sep", "25 Sep", "26 Sep", "27 Sep", "28 Sep"]
    y-axis "AED" 0 --> 28531
    line [18282.0, 17612.6, 13774.8, 12394.2, 17008.3, 17889.7, 21480.7, 19241.1, 13824.4, 14739.4, 13651.1, 18366.9, 19607.6, 21374.0, 16623.7, 13046.7, 12713.9, 16831.9, 19315.1, 24809.9, 21324.5, 20285.4, 15245.9, 13204.5, 16710.6, 16301.6, 20393.5, 20432.1, 18621.0, 15240.7]
```

```mermaid
%%{init: {"theme": "base", "themeVariables": {"xyChart": {"backgroundColor": "#FFF7F1", "titleColor": "#1B2A49", "xAxisLabelColor": "#1B2A49", "xAxisTitleColor": "#1B2A49", "xAxisTickColor": "#1B2A49", "xAxisLineColor": "#1B2A49", "yAxisLabelColor": "#1B2A49", "yAxisTitleColor": "#1B2A49", "yAxisTickColor": "#1B2A49", "yAxisLineColor": "#1B2A49", "plotColorPalette": "#1B2A49"}}}}%%
xychart-beta
    title "Avg Daily Net Revenue by Weekday (AED)"
    x-axis ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    y-axis "AED" 0 --> 24326
    bar [14994.1, 13608.1, 14897.0, 17748.0, 20675.2, 21152.8, 18610.6]
```

```mermaid
%%{init: {"theme": "base", "themeVariables": {"xyChart": {"backgroundColor": "#FFF7F1", "titleColor": "#1B2A49", "xAxisLabelColor": "#1B2A49", "xAxisTitleColor": "#1B2A49", "xAxisTickColor": "#1B2A49", "xAxisLineColor": "#1B2A49", "yAxisLabelColor": "#1B2A49", "yAxisTitleColor": "#1B2A49", "yAxisTickColor": "#1B2A49", "yAxisLineColor": "#1B2A49", "plotColorPalette": "#0F8B8D"}}}}%%
xychart-beta
    title "Delivered Orders by Hour of Day"
    x-axis ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
    y-axis "Orders" 0 --> 905
    bar [193.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 199.0, 489.0, 606.0, 430.0, 250.0, 202.0, 307.0, 413.0, 629.0, 787.0, 704.0, 485.0, 326.0]
```

---

## 4. Channels & Platforms

```mermaid
%%{init: {"theme": "base", "themeVariables": {"background": "#FFF7F1", "pie1": "#1B2A49", "pie2": "#0F8B8D", "pie3": "#F0906A", "pie4": "#4A6FA5", "pie5": "#3CBFB9", "pie6": "#F6B08C", "pie7": "#7C93B8", "pieTitleTextColor": "#1B2A49", "pieSectionTextColor": "#FFFFFF", "pieLegendTextColor": "#1B2A49", "pieStrokeColor": "#FFFFFF", "pieOuterStrokeColor": "#1B2A49", "pieOpacity": "1"}}}%%
pie showData title Delivered Orders by Platform
    "Talabat" : 1944.0
    "Deliveroo" : 1008.0
    "App" : 721.0
    "Careem" : 704.0
    "Phone" : 630.0
    "Website" : 540.0
    "Noon Food" : 473.0
```

| Platform | Channel | Orders | Cancel % | Commission rate | Gross (AED) | Commission (AED) | Net (AED) | Avg net / order (AED) |
|---|---|---|---|---|---|---|---|---|
| Talabat | Aggregator | 2048 | 5.1% | 25% | 197,386 | 49,346 | 148,040 | 76.2 |
| Phone | Phone | 655 | 3.8% | 0% | 76,485 | 0 | 76,485 | 121.4 |
| Deliveroo | Aggregator | 1060 | 4.9% | 27% | 103,187 | 27,860 | 75,327 | 74.7 |
| App | Direct | 754 | 4.4% | 0% | 73,032 | 0 | 73,032 | 101.3 |
| Careem | Aggregator | 750 | 6.1% | 22% | 70,500 | 15,510 | 54,990 | 78.1 |
| Website | Direct | 566 | 4.6% | 0% | 54,082 | 0 | 54,082 | 100.2 |
| Noon Food | Aggregator | 503 | 6.0% | 20% | 47,991 | 9,598 | 38,393 | 81.2 |

```mermaid
%%{init: {"theme": "base", "themeVariables": {"background": "#FFF7F1", "pie1": "#1B2A49", "pie2": "#0F8B8D", "pie3": "#F0906A", "pie4": "#4A6FA5", "pie5": "#3CBFB9", "pie6": "#F6B08C", "pie7": "#7C93B8", "pieTitleTextColor": "#1B2A49", "pieSectionTextColor": "#FFFFFF", "pieLegendTextColor": "#1B2A49", "pieStrokeColor": "#FFFFFF", "pieOuterStrokeColor": "#1B2A49", "pieOpacity": "1"}}}%%
pie showData title Commission Paid by Platform (AED)
    "Talabat" : 49346.5
    "Deliveroo" : 27860.5
    "Careem" : 15510.0
    "Noon Food" : 9598.2
```

**Delivery vs Pickup**

| Order type | Orders | Gross (AED) | Net (AED) | Avg order (AED) | Share |
|---|---|---|---|---|---|
| Delivery | 5361 | 551,973 | 453,950 | 103 | 89.1% |
| Pickup | 659 | 70,690 | 66,398 | 107 | 10.9% |

---

## 5. Delivery Areas

```mermaid
%%{init: {"theme": "base", "themeVariables": {"xyChart": {"backgroundColor": "#FFF7F1", "titleColor": "#1B2A49", "xAxisLabelColor": "#1B2A49", "xAxisTitleColor": "#1B2A49", "xAxisTickColor": "#1B2A49", "xAxisLineColor": "#1B2A49", "yAxisLabelColor": "#1B2A49", "yAxisTitleColor": "#1B2A49", "yAxisTickColor": "#1B2A49", "yAxisLineColor": "#1B2A49", "plotColorPalette": "#1B2A49"}}}}%%
xychart-beta
    title "Delivery Orders by Area"
    x-axis ["Al Barsha", "JLT", "Barsha Heights", "Dubai Marina", "JVC", "Al Quoz", "Umm Suqeim", "Jumeirah", "Business Bay", "Downtown Dubai"]
    y-axis "Orders" 0 --> 1096
    bar [953.0, 809.0, 741.0, 700.0, 616.0, 410.0, 340.0, 315.0, 258.0, 219.0]
```

| Area | Distance (km) | Orders | Net revenue (AED) | Net / order (AED) |
|---|---|---|---|---|
| Al Barsha | 2 | 953 | 80,541 | 84.5 |
| JLT | 5 | 809 | 66,860 | 82.6 |
| Barsha Heights | 3 | 741 | 62,788 | 84.7 |
| Dubai Marina | 6 | 700 | 60,310 | 86.2 |
| JVC | 7 | 616 | 53,520 | 86.9 |
| Al Quoz | 5 | 410 | 34,447 | 84.0 |
| Umm Suqeim | 5 | 340 | 28,485 | 83.8 |
| Jumeirah | 9 | 315 | 26,562 | 84.3 |
| Business Bay | 13 | 258 | 20,735 | 80.4 |
| Downtown Dubai | 14 | 219 | 19,702 | 90.0 |

---

## 6. Menu Performance

```mermaid
%%{init: {"theme": "base", "themeVariables": {"background": "#FFF7F1", "pie1": "#1B2A49", "pie2": "#0F8B8D", "pie3": "#F0906A", "pie4": "#4A6FA5", "pie5": "#3CBFB9", "pie6": "#F6B08C", "pie7": "#7C93B8", "pieTitleTextColor": "#1B2A49", "pieSectionTextColor": "#FFFFFF", "pieLegendTextColor": "#1B2A49", "pieStrokeColor": "#FFFFFF", "pieOuterStrokeColor": "#1B2A49", "pieOpacity": "1"}}}%%
pie showData title Revenue by Cuisine (AED)
    "Indian" : 149923.0
    "Arabic" : 148209.0
    "Italian" : 129651.0
    "Continental" : 122052.0
    "Chinese" : 72828.0
```

```mermaid
%%{init: {"theme": "base", "themeVariables": {"xyChart": {"backgroundColor": "#FFF7F1", "titleColor": "#1B2A49", "xAxisLabelColor": "#1B2A49", "xAxisTitleColor": "#1B2A49", "xAxisTickColor": "#1B2A49", "xAxisLineColor": "#1B2A49", "yAxisLabelColor": "#1B2A49", "yAxisTitleColor": "#1B2A49", "yAxisTickColor": "#1B2A49", "yAxisLineColor": "#1B2A49", "plotColorPalette": "#F0906A"}}}}%%
xychart-beta
    title "Revenue by Category (AED)"
    x-axis ["Main", "Starter", "Beverage", "Side", "Dessert"]
    y-axis "AED" 0 --> 489303
    bar [425481.0, 72170.0, 54070.0, 38932.0, 32010.0]
```

**Top 10 dishes by revenue**

| # | Dish | Cuisine | Qty sold | Revenue (AED) |
|---|---|---|---|---|
| 1 | Mixed Grill | Arabic | 389 | 29,175 |
| 2 | Chicken Biryani | Indian | 665 | 27,930 |
| 3 | Butter Chicken | Indian | 599 | 26,955| Deliveroo | Aggregator | 1060 | 4.9% | 27% | 103,187 | 27,860 | 75,327 | 74.7 |
| App | Direct | 754 | 4.4% | 0% | 73,032 | 0 | 73,032 | 101.3 |
| Careem | Aggregator | 750 | 6.1% | 22% | 70,500 | 15,510 | 54,990 | 78.1 |
| Website | Direct | 566 | 4.6% | 0% | 54,082 | 0 | 54,082 | 100.2 |
| Noon Food | Aggregator | 503 | 6.0% | 20% | 47,991 | 9,598 | 38,393 | 81.2 |

```mermaid
pie showData title Commission Paid by Platform (AED)
    "Talabat" : 49346.5
    "Deliveroo" : 27860.5
    "Careem" : 15510.0
    "Noon Food" : 9598.2
```

**Delivery vs Pickup**

| Order type | Orders | Gross (AED) | Net (AED) | Avg order (AED) | Share |
|---|---|---|---|---|---|
| Delivery | 5361 | 551,973 | 453,950 | 103 | 89.1% |
| Pickup | 659 | 70,690 | 66,398 | 107 | 10.9% |

---

## 5. Delivery Areas

```mermaid
xychart-beta
    title "Delivery Orders by Area"
    x-axis ["Al Barsha", "JLT", "Barsha Heights", "Dubai Marina", "JVC", "Al Quoz", "Umm Suqeim", "Jumeirah", "Business Bay", "Downtown Dubai"]
    y-axis "Orders" 0 --> 1096
    bar [953.0, 809.0, 741.0, 700.0, 616.0, 410.0, 340.0, 315.0, 258.0, 219.0]
```

| Area | Distance (km) | Orders | Net revenue (AED) | Net / order (AED) |
|---|---|---|---|---|
| Al Barsha | 2 | 953 | 80,541 | 84.5 |
| JLT | 5 | 809 | 66,860 | 82.6 |
| Barsha Heights | 3 | 741 | 62,788 | 84.7 |
| Dubai Marina | 6 | 700 | 60,310 | 86.2 |
| JVC | 7 | 616 | 53,520 | 86.9 |
| Al Quoz | 5 | 410 | 34,447 | 84.0 |
| Umm Suqeim | 5 | 340 | 28,485 | 83.8 |
| Jumeirah | 9 | 315 | 26,562 | 84.3 |
| Business Bay | 13 | 258 | 20,735 | 80.4 |
| Downtown Dubai | 14 | 219 | 19,702 | 90.0 |

---

## 6. Menu Performance

```mermaid
pie showData title Revenue by Cuisine (AED)
    "Indian" : 149923.0
    "Arabic" : 148209.0
    "Italian" : 129651.0
    "Continental" : 122052.0
    "Chinese" : 72828.0
```

```mermaid
xychart-beta
    title "Revenue by Category (AED)"
    x-axis ["Main", "Starter", "Beverage", "Side", "Dessert"]
    y-axis "AED" 0 --> 489303
    bar [425481.0, 72170.0, 54070.0, 38932.0, 32010.0]
```

**Top 10 dishes by revenue**

| # | Dish | Cuisine | Qty sold | Revenue (AED) |
|---|---|---|---|---|
| 1 | Mixed Grill | Arabic | 389 | 29,175 |
| 2 | Chicken Biryani | Indian | 665 | 27,930 |
| 3 | Butter Chicken | Indian | 599 | 26,955 |
| 4 | Lamb Mandi | Arabic | 434 | 26,908 |
| 5 | Chicken Shawarma Plate | Arabic | 617 | 23,446 |
| 6 | Classic Beef Burger | Continental | 470 | 22,560 |
| 7 | Margherita Pizza | Italian | 470 | 21,150 |
| 8 | Pepperoni Pizza | Italian | 398 | 20,696 |
| 9 | Grilled Salmon | Continental | 250 | 19,500 |
| 10 | Mutton Biryani | Indian | 362 | 18,824 |

---

## 7. Cancellations

```mermaid
xychart-beta
    title "Cancellation Rate by Platform (%)"
    x-axis ["Careem", "Noon Food", "Talabat", "Deliveroo", "Website", "App", "Phone"]
    y-axis "%" 0 --> 7
    bar [6.1, 6.0, 5.1, 4.9, 4.6, 4.4, 3.8]
```

---

## Data Files

| File | Description |
|---|---|
| `orders.csv` | One row per order: channel, platform, area, status, amounts, timestamps |
| `order_items.csv` | Line items per order: dish, cuisine, category, qty, price |
| `menu.csv` | Dish master: price, prep minutes, popularity |
| `platforms.csv` | Platform commission rates and mix assumptions |
| `areas.csv` | Delivery areas with distance and order weight |
