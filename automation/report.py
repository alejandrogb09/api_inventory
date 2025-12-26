from fetch_data import get_products
from datetime import datetime

def generate_stock_report():
    products = get_products()
    date = datetime.now().strftime("%Y-%m-%d")

    filename = f"stock_report_{date}.txt"

    with open(filename, "W") as file:
        file.write(f"REPORTE DE STOCK - {date}\n\n")

        for product in products:
            file.write(
                f"{product['name']} - Stock: {product['stock']}\n"
            )

    print(f"Reporte generado: {filename}")

if __name__ == "__main__":
    generate_stock_report()