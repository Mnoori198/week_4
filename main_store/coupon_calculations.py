def calculate_price(price, cash_coupen, percent_coupen):
    shipping_vp_to_ten = 5.95
    shipping_ten_to_thrity = 7.95
    shipping = 0
    tax = 0.06

    price_after_cash_coupen = price - cash_coupen
    price_after_percent_coupen = price_after_cash_coupen - (price_after_cash_coupen* percent_coupen)
    price_with_tax = price_after_percent_coupen + (price_after_percent_coupen* tax)

    if price_after_percent_coupen < 10:
        total_prince = price_with_tax + shipping_vp_to_ten
        print(total_prince)
        return total_prince





if __name__ == '__main__':
    calculate_price(6, 5, 12)
