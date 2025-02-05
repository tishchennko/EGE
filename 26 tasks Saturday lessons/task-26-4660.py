with open('input2.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices, reverse=True)

every_4 = sum([prices[i] for i in range(3, N, 4)])
client_price = sum(prices) - every_4 + every_4 / 2
store_price = sum(prices[:3 * N // 4]) + sum(prices[3 * N // 4:]) / 2

print(client_price, store_price)












