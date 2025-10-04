class MyStatistic:
    def find_orders_within_range(self, df, minValue, maxValue, sortType=True):
        # Tính tổng tiền cho từng OrderID
        order_totals = df.groupby('OrderID').apply(
            lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum()
        )

        # Lọc các đơn hàng nằm trong khoảng
        orders_within_range = order_totals[(order_totals >= minValue) & (order_totals <= maxValue)]

        # Sắp xếp theo SortType (True = tăng dần, False = giảm dần)
        orders_sorted = orders_within_range.sort_values(ascending=sortType)

        # Trả về list các tuple (OrderID, TotalValue)
        result = list(zip(orders_sorted.index.tolist(), orders_sorted.values.tolist()))
        return result
