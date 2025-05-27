with open('26_4629.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices, reverse=True)


client_price = sum(prices[: N // 4])/ 2 + sum(prices[ N // 4:])
store_price = sum(prices[:3 * N // 4]) + sum(prices[3 * N // 4:]) / 2

print(client_price, store_price)