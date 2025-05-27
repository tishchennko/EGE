with open('26_4684.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices, reverse=True)

every_6 = sum([prices[i] for i in range(5, N, 6)])
client_price = sum(prices) - every_6 / 2
store_price = sum(prices[:5 * N // 6]) + sum(prices[5 * N // 6:]) / 2

print(client_price, store_price)