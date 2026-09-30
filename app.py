"""
Restaurant Sales & Operations Dashboard (Streamlit)

Repo layout expected on GitHub:
    app.py
    requirements.txt
    .streamlit/config.toml
    data/orders.csv, order_items.csv, menu.csv, platforms.csv, areas.csv
"""
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ---------------------------------------------------------------- Theme
NAVY, TEAL, PEACH = "#1B2A49", "#0F8B8D", "#F0906A"
COLORWAY = [NAVY, TEAL, PEACH, "#4A6FA5", "#3CBFB9", "#F6B08C", "#7C93B8"]
GRID = "#F3DDD0"

st.set_page_config(page_title="Restaurant Dashboard", page_icon="🍽️", layout="wide")

st.markdown(
    f"""
    <style>
    h1, h2, h3, h4 {{ color: {NAVY}; }}
    [data-testid="stMetric"] {{
        background: #FFFFFF; border-left: 5px solid {TEAL};
        padding: 12px 16px; border-radius: 6px;
        box-shadow: 0 1px 3px rgba(27, 42, 73, 0.10);
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


def style(fig, height=380):
    """Apply the navy / teal / peach look to a Plotly figure."""
    fig.update_layout(
        colorway=COLORWAY, height=height,
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=NAVY), title_font=dict(size=16, color=NAVY),
        margin=dict(l=10, r=10, t=50, b=10),
        legend=dict(title_text=""),
    )
    fig.update_xaxes(gridcolor=GRID, linecolor=NAVY, title_text=None)
    fig.update_yaxes(gridcolor=GRID, linecolor=NAVY)
    return fig


def aed(x):
    return f"AED {x:,.0f}"


# ---------------------------------------------------------------- Data
DT_COLS = ["order_datetime", "preparing_at", "ready_at", "dispatched_at", "completed_at"]
FILES = ["orders.csv", "order_items.csv", "menu.csv", "platforms.csv", "areas.csv"]


@st.cache_data(show_spinner="Loading data...")
def load_data():
    base = Path(__file__).parent
    folder = base / "data" if (base / "data" / "orders.csv").exists() else base
    missing = [f for f in FILES if not (folder / f).exists()]
    if missing:
        raise FileNotFoundError(f"Missing file(s) in {folder}: {', '.join(missing)}")
    orders = pd.read_csv(folder / "orders.csv", parse_dates=DT_COLS)
    items = pd.read_csv(folder / "order_items.csv")
    menu = pd.read_csv(folder / "menu.csv")
    platforms = pd.read_csv(folder / "platforms.csv")
    areas = pd.read_csv(folder / "areas.csv")
    return orders, items, menu, platforms, areas


try:
    orders, items, menu, platforms, areas = load_data()
except Exception as e:  # show a friendly message instead of a stack trace
    st.error(f"Could not load the data. {e}")
    st.stop()

# ---------------------------------------------------------------- Sidebar filters
st.sidebar.header("Filters")

min_d, max_d = orders.order_datetime.dt.date.min(), orders.order_datetime.dt.date.max()
date_range = st.sidebar.date_input("Order date", (min_d, max_d), min_value=min_d, max_value=max_d)
if isinstance(date_range, (tuple, list)):
    start_d, end_d = (date_range[0], date_range[-1]) if len(date_range) else (min_d, max_d)
else:
    start_d = end_d = date_range

channels = st.sidebar.multiselect("Channel", sorted(orders.channel_type.unique()),
                                  default=sorted(orders.channel_type.unique()))
plat_opts = sorted(orders[orders.channel_type.isin(channels)].platform.unique())
plats = st.sidebar.multiselect("Platform", plat_opts, default=plat_opts)
otypes = st.sidebar.multiselect("Order type", sorted(orders.order_type.unique()),
                                default=sorted(orders.order_type.unique()))

day = orders.order_datetime.dt.date
mask = (day >= start_d) & (day <= end_d) & orders.channel_type.isin(channels) \
    & orders.platform.isin(plats) & orders.order_type.isin(otypes)
df = orders[mask].copy()

if df.empty:
    st.warning("No orders match the selected filters.")
    st.stop()

delivered = df[df.status == "Delivered"].copy()
cancelled = df[df.status == "Cancelled"]
d_items = items[items.order_id.isin(delivered.order_id)]

st.sidebar.download_button("Download filtered orders (CSV)",
                           df.to_csv(index=False).encode("utf-8"),
                           file_name="filtered_orders.csv", mime="text/csv")
st.sidebar.caption("Revenue figures use Delivered orders only. "
                   "Net revenue = gross - platform commission.")

# ---------------------------------------------------------------- Header + KPIs
st.title("Restaurant Sales & Operations Dashboard")
st.caption(f"{start_d:%d %b %Y} to {end_d:%d %b %Y} | Dubai | {len(df):,} orders in selection")

gross = delivered.gross_amount.sum()
commission = delivered.commission_amount.sum()
net = delivered.net_revenue.sum()
aov = delivered.gross_amount.mean() if len(delivered) else 0
cancel_rate = len(cancelled) / len(df)

k = st.columns(4)
k[0].metric("Net revenue", aed(net))
k[1].metric("Gross sales", aed(gross))
k[2].metric("Commission paid", aed(commission),
            help="Share of gross sales paid to delivery platforms")
k[3].metric("Avg order value", aed(aov))
k = st.columns(4)
k[0].metric("Total orders", f"{len(df):,}")
k[1].metric("Delivered", f"{len(delivered):,}")
k[2].metric("Cancelled", f"{len(cancelled):,}")
k[3].metric("Cancel rate", f"{cancel_rate:.1%}")

if len(delivered) == 0:
    st.info("No delivered orders in this selection, so revenue charts are empty.")
    st.stop()

st.markdown("")
tab_over, tab_plat, tab_area, tab_menu, tab_ops = st.tabs(
    ["Overview", "Platforms", "Areas", "Menu", "Operations"])

# ---------------------------------------------------------------- Overview
with tab_over:
    daily = (delivered.set_index("order_datetime").net_revenue
             .resample("D").sum().reset_index())
    fig = px.line(daily, x="order_datetime", y="net_revenue", markers=True,
                  title="Daily net revenue (AED)", color_discrete_sequence=[TEAL])
    fig.update_yaxes(title_text="AED")
    st.plotly_chart(style(fig, 360))

    c1, c2 = st.columns(2)
    with c1:
        order = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        daily["weekday"] = daily.order_datetime.dt.strftime("%a")
        wk = daily.groupby("weekday").net_revenue.mean().reindex(order).reset_index()
        fig = px.bar(wk, x="weekday", y="net_revenue",
                     title="Avg daily net revenue by weekday (AED)",
                     color_discrete_sequence=[NAVY])
        fig.update_yaxes(title_text="AED")
        st.plotly_chart(style(fig))
    with c2:
        hourly = (delivered.groupby(delivered.order_datetime.dt.hour).size()
                  .reindex(range(24), fill_value=0).reset_index())
        hourly.columns = ["hour", "orders"]
        fig = px.bar(hourly, x="hour", y="orders", title="Delivered orders by hour of day",
                     color_discrete_sequence=[TEAL])
        fig.update_xaxes(dtick=2)
        st.plotly_chart(style(fig))

    peak_hour = int(hourly.loc[hourly.orders.idxmax(), "hour"])
    best_day = wk.loc[wk.net_revenue.idxmax(), "weekday"]
    st.markdown(f"**Peak hour:** {peak_hour}:00  |  **Strongest weekday:** {best_day}  |  "
                f"**Lost to cancellations:** {aed(cancelled.gross_amount.sum())} gross")

# ---------------------------------------------------------------- Platforms
with tab_plat:
    plat = (delivered.groupby("platform")
            .agg(orders=("order_id", "count"), gross=("gross_amount", "sum"),
                 commission=("commission_amount", "sum"), net=("net_revenue", "sum"))
            .reset_index()
            .merge(platforms[["platform", "channel_type", "commission_rate"]],
                   on="platform", how="left")
            .sort_values("gross", ascending=False))
    canc = (df.groupby("platform").status.apply(lambda s: (s == "Cancelled").mean())
            .rename("cancel_rate").reset_index())
    plat = plat.merge(canc, on="platform", how="left")

    c1, c2 = st.columns([3, 2])
    with c1:
        fig = go.Figure()
        fig.add_bar(name="Net revenue", x=plat.platform, y=plat.net, marker_color=TEAL)
        fig.add_bar(name="Commission", x=plat.platform, y=plat.commission, marker_color=PEACH)
        fig.update_layout(barmode="stack", title="Gross sales split: net vs commission (AED)")
        st.plotly_chart(style(fig))
    with c2:
        fig = px.pie(plat, names="platform", values="orders", hole=0.5,
                     title="Delivered orders by platform", color_discrete_sequence=COLORWAY)
        fig.update_traces(textinfo="percent", marker=dict(line=dict(color="#FFFFFF", width=2)))
        st.plotly_chart(style(fig))

    show = plat.assign(
        avg_net_per_order=(plat.net / plat.orders).round(1),
        commission_rate=(plat.commission_rate * 100).round(0).astype("Int64").astype(str) + "%",
        cancel_rate=(plat.cancel_rate * 100).round(1).astype(str) + "%",
    )[["platform", "channel_type", "orders", "commission_rate", "gross", "commission",
       "net", "avg_net_per_order", "cancel_rate"]].round({"gross": 0, "commission": 0, "net": 0})
    show.columns = ["Platform", "Channel", "Delivered orders", "Commission rate",
                    "Gross (AED)", "Commission (AED)", "Net (AED)",
                    "Avg net / order (AED)", "Cancel rate"]
    st.dataframe(show, hide_index=True)

    ot = (delivered.groupby("order_type")
          .agg(orders=("order_id", "count"), net=("net_revenue", "sum"),
               aov=("gross_amount", "mean")).reset_index())
    fig = px.bar(ot, x="order_type", y="orders", text="orders",
                 title="Delivery vs pickup (delivered orders)",
                 color_discrete_sequence=[NAVY])
    st.plotly_chart(style(fig, 300))

# ---------------------------------------------------------------- Areas
with tab_area:
    dlv = delivered[delivered.order_type == "Delivery"]
    if dlv.empty:
        st.info("No delivery orders in this selection.")
    else:
        ar = (dlv.groupby("area")
              .agg(orders=("order_id", "count"), net=("net_revenue", "sum"))
              .reset_index().merge(areas, on="area", how="left")
              .sort_values("orders", ascending=False))
        ar["net_per_order"] = (ar.net / ar.orders).round(1)

        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(ar, x="area", y="orders", title="Delivery orders by area",
                         color_discrete_sequence=[NAVY])
            st.plotly_chart(style(fig))
        with c2:
            fig = px.scatter(ar, x="distance_km", y="orders", size="net", text="area",
                             title="Distance vs orders (bubble = net revenue)",
                             color_discrete_sequence=[PEACH])
            fig.update_traces(textposition="top center", textfont=dict(color=NAVY))
            fig.update_xaxes(title_text="Distance (km)")
            st.plotly_chart(style(fig))

        tbl = ar[["area", "distance_km", "orders", "net", "net_per_order"]].copy()
        tbl.columns = ["Area", "Distance (km)", "Orders", "Net revenue (AED)", "Net / order (AED)"]
        tbl["Net revenue (AED)"] = tbl["Net revenue (AED)"].round(0)
        st.dataframe(tbl, hide_index=True)

# ---------------------------------------------------------------- Menu
with tab_menu:
    c1, c2 = st.columns(2)
    with c1:
        cu = d_items.groupby("cuisine").line_total.sum().reset_index()
        fig = px.pie(cu, names="cuisine", values="line_total", hole=0.5,
                     title="Revenue by cuisine (AED)", color_discrete_sequence=COLORWAY)
        fig.update_traces(textinfo="percent+label",
                          marker=dict(line=dict(color="#FFFFFF", width=2)))
        st.plotly_chart(style(fig))
    with c2:
        ca = (d_items.groupby("category").line_total.sum()
              .sort_values(ascending=False).reset_index())
        fig = px.bar(ca, x="category", y="line_total", title="Revenue by category (AED)",
                     color_discrete_sequence=[PEACH])
        fig.update_yaxes(title_text="AED")
        st.plotly_chart(style(fig))

    dishes = (d_items.groupby(["dish", "cuisine"])
              .agg(qty=("quantity", "sum"), revenue=("line_total", "sum"))
              .reset_index().sort_values("revenue", ascending=False))
    n = st.slider("Top dishes to show", 5, 20, 10)
    top = dishes.head(n).sort_values("revenue")
    fig = px.bar(top, x="revenue", y="dish", orientation="h", color="cuisine",
                 title=f"Top {n} dishes by revenue (AED)", color_discrete_sequence=COLORWAY)
    fig.update_yaxes(title_text=None)
    st.plotly_chart(style(fig, max(320, 30 * n + 100)))

    pop = dishes.merge(menu[["dish", "popularity", "prep_minutes", "price_aed"]],
                       on="dish", how="left")
    fig = px.scatter(pop, x="popularity", y="qty", size="revenue", color="cuisine",
                     hover_name="dish", title="Menu popularity score vs quantity sold",
                     color_discrete_sequence=COLORWAY)
    fig.update_xaxes(title_text="Popularity score (menu.csv)")
    fig.update_yaxes(title_text="Quantity sold")
    st.plotly_chart(style(fig))

# ---------------------------------------------------------------- Operations
with tab_ops:
    prep = (delivered.ready_at - delivered.preparing_at).dt.total_seconds() / 60
    transit = (delivered.completed_at - delivered.dispatched_at).dt.total_seconds() / 60
    total = (delivered.completed_at - delivered.order_datetime).dt.total_seconds() / 60

    k = st.columns(3)
    k[0].metric("Avg prep time", f"{prep.mean():.1f} min")
    k[1].metric("Avg dispatch to delivery", f"{transit.mean():.1f} min")
    k[2].metric("Avg order to complete", f"{total.mean():.1f} min")

    c1, c2 = st.columns(2)
    with c1:
        fig = px.histogram(total.dropna().rename("minutes").to_frame(), x="minutes", nbins=30,
                           title="Order-to-complete time (minutes)",
                           color_discrete_sequence=[TEAL])
        fig.update_yaxes(title_text="Orders")
        st.plotly_chart(style(fig))
    with c2:
        cr = (df.groupby("platform").status.apply(lambda s: (s == "Cancelled").mean() * 100)
              .sort_values(ascending=False).reset_index())
        cr.columns = ["platform", "cancel_rate"]
        fig = px.bar(cr, x="platform", y="cancel_rate", title="Cancellation rate by platform (%)",
                     color_discrete_sequence=[PEACH])
        fig.update_yaxes(title_text="%")
        st.plotly_chart(style(fig))

    dl = delivered[delivered.order_type == "Delivery"].assign(total_min=total)
    if not dl.empty:
        at = (dl.groupby("area").total_min.mean().sort_values(ascending=False)
              .round(1).reset_index())
        fig = px.bar(at, x="area", y="total_min", title="Avg order-to-complete time by area (min)",
                     color_discrete_sequence=[NAVY])
        fig.update_yaxes(title_text="Minutes")
        st.plotly_chart(style(fig))

st.caption("Data: orders, order_items, menu, platforms, areas CSV files.")
