class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k+1):
            temp_prices = prices.copy()
            for source, destination, price in flights:
                if prices[source] != float('inf'):
                    temp_prices[destination] = min(temp_prices[destination], prices[source]+price)
            prices = temp_prices

        return prices[dst] if prices[dst] != float('inf') else -1