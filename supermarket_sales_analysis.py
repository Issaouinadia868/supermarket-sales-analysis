"""Supermarket Sales Analysis
Run: python supermarket_sales_analysis.py
Expected input: supermarket_sales.csv in the project root.
"""
from pathlib import Path
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "supermarket_sales.txt"
OUTPUT_DIR = ROOT / "outputs" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams.update({"figure.figsize": (10, 6), "axes.titlesize": 15})


def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {path}\n"
            "Add your CSV file as 'supermarket_sales.csv' in the project root."
        )
    df = pd.read_csv(path)
    required = {"Branch", "City", "Product line", "Total", "Date", "Time", "Payment"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Total"] = pd.to_numeric(df["Total"], errors="coerce")
    df = df.dropna(subset=["Date", "Total"]).copy()
    df["Hour"] = pd.to_datetime(df["Time"], format="%H:%M", errors="coerce").dt.hour
    return df


def save_bar(series: pd.Series, title: str, xlabel: str, filename: str,
             horizontal: bool = False, color: str = "#2878B5") -> None:
    fig, ax = plt.subplots(figsize=(11, 6))
    ordered = series.sort_values(ascending=True if horizontal else False)
    if horizontal:
        ordered.plot(kind="barh", ax=ax, color=color)
    else:
        ordered.plot(kind="bar", ax=ax, color=color)
        ax.tick_params(axis="x", rotation=25)
    ax.set_title(title, pad=14, weight="bold")
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Total sales")
    ax.grid(axis="y" if not horizontal else "x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / filename, dpi=180, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    df = load_data(DATA_PATH)

    total_sales = df["Total"].sum()
    average_sale = df["Total"].mean()
    highest_sale = df["Total"].max()
    category_sales = df.groupby("Product line")["Total"].sum().sort_values(ascending=False)
    city_sales = df.groupby("City")["Total"].sum().sort_values(ascending=False)
    branch_sales = df.groupby("Branch")["Total"].sum().sort_values(ascending=False)
    payment_counts = df["Payment"].value_counts()
    payment_pct = df["Payment"].value_counts(normalize=True).mul(100).round(1)
    hourly_sales = df.groupby("Hour")["Total"].sum().dropna().sort_index()
    daily_sales = df.groupby("Date")["Total"].sum().sort_index()
    branch_category = df.pivot_table(
        index="Product line", columns="Branch", values="Total", aggfunc="sum"
    )

    print("\n========== KEY PERFORMANCE INDICATORS ==========")
    print(f"Transactions: {len(df):,}")
    print(f"Total sales: {total_sales:,.2f}")
    print(f"Average transaction value: {average_sale:,.2f}")
    print(f"Highest single transaction: {highest_sale:,.2f}")
    print(f"\nSales by product line:\n{category_sales.round(2).to_string()}")
    print(f"\nSales by city:\n{city_sales.round(2).to_string()}")
    print(f"\nSales by branch:\n{branch_sales.round(2).to_string()}")
    print(f"\nPayment counts:\n{payment_counts.to_string()}")
    print(f"\nPayment percentages:\n{payment_pct.to_string()}")
    if not hourly_sales.empty:
        print(f"\nTop sales hour: {int(hourly_sales.idxmax()):02d}:00 "
              f"({hourly_sales.max():,.2f})")
    if not daily_sales.empty:
        print(f"Best sales date: {daily_sales.idxmax().date()} "
              f"({daily_sales.max():,.2f})")

    save_bar(category_sales, "Total Sales by Product Line", "Product line",
             "sales_by_product_line.png", horizontal=True, color="#2364AA")
    save_bar(city_sales, "Total Sales by City", "City",
             "sales_by_city.png", horizontal=True, color="#2A9D8F")
    save_bar(branch_sales, "Total Sales by Branch", "Branch",
             "sales_by_branch.png", color="#457B9D")
    save_bar(hourly_sales, "Total Sales by Hour", "Hour of the day",
             "sales_by_hour.png", color="#3A86A8")

    fig, ax = plt.subplots(figsize=(9, 6))
    payment_counts.plot(kind="pie", autopct="%1.1f%%", startangle=90,
                        ax=ax, ylabel="", wedgeprops={"edgecolor": "white"})
    ax.set_title("Payment Method Distribution", weight="bold", pad=14)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "payment_methods.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(12, 6))
    daily_sales.plot(ax=ax, marker="o", linewidth=1.5, markersize=3, color="#2364AA")
    ax.set_title("Daily Sales Trend", weight="bold", pad=14)
    ax.set_xlabel("Date")
    ax.set_ylabel("Total sales")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "daily_sales_trend.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(branch_category, annot=True, fmt=".0f", cmap="Blues",
                linewidths=0.5, ax=ax)
    ax.set_title("Sales by Product Line and Branch", weight="bold", pad=14)
    ax.set_xlabel("Branch")
    ax.set_ylabel("Product line")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "product_line_by_branch_heatmap.png",
                dpi=180, bbox_inches="tight")
    plt.close(fig)

    print(f"\nCharts saved to: {OUTPUT_DIR}")
    print("Analysis completed successfully.")


if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, ValueError) as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        sys.exit(1)
