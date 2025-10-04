import sqlite3
import pandas as pd
def get_top_invoices_in_range(db_path, a, b, n):
    conn = sqlite3.connect(db_path)
    query = f"""
        SELECT InvoiceId, Total
        FROM Invoice
        WHERE Total BETWEEN {a} AND {b}
        ORDER BY Total DESC
        LIMIT {n};
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
def get_top_customers_by_invoice_count(db_path, n):
    conn = sqlite3.connect(db_path)
    query = f"""
        SELECT c.CustomerId, c.FirstName || ' ' || c.LastName AS CustomerName,
               COUNT(i.InvoiceId) AS InvoiceCount
        FROM Customer c
        JOIN Invoice i ON c.CustomerId = i.CustomerId
        GROUP BY c.CustomerId
        ORDER BY InvoiceCount DESC
        LIMIT {n};
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
def get_top_customers_by_total_value(db_path, n):
    conn = sqlite3.connect(db_path)
    query = f"""
        SELECT c.CustomerId, c.FirstName || ' ' || c.LastName AS CustomerName,
               SUM(i.Total) AS TotalSpent
        FROM Customer c
        JOIN Invoice i ON c.CustomerId = i.CustomerId
        GROUP BY c.CustomerId
        ORDER BY TotalSpent DESC
        LIMIT {n};
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
db_path = "../databases/Chinook_Sqlite.sqlite"

print("=== TOP 5 Invoice trong khoảng 5 -> 15 ===")
print(get_top_invoices_in_range(db_path, 5, 15, 5))

print("=== TOP 5 khách hàng có nhiều Invoice nhất ===")
print(get_top_customers_by_invoice_count(db_path, 5))

print("=== TOP 5 khách hàng có tổng giá trị cao nhất ===")
print(get_top_customers_by_total_value(db_path, 5))
