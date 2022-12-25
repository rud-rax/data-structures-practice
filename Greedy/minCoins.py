

def minCoins(amount : int,coins : list) :

    # Sort the list of coins given in order to minimize the number of coins needed so as to derive the optimal solution
    coins.sort(reverse=True)

    coins_solution = []

    for coin in coins :
        # if amount == 0 :
        #     break

        # if amount < coin :
        #     continue

        n = amount // coin
        amount -= coin * n

        coins_solution.append(n)

    return coins_solution






if __name__ == "__main__" :
    print(minCoins(52 , [1,2,5,10]))