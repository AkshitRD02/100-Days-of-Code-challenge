import art
print(art.logo)




loop_over=False
auction_bids={}
while not loop_over:
    name=input("Enter your name: ").capitalize()
    bid=int(input("Enter your bid: "))
    auction_bids[name]=bid
    continue_loop=input("Anyone else to bid? (Yes/No): ").lower()
    if continue_loop=="yes":
        loop_over=False
        print("\n"*100)
    if continue_loop=="no":
        loop_over=True





highest_bid=0
auction_winner=""
for name in auction_bids:
    if auction_bids[name]>highest_bid:
        highest_bid=auction_bids[name]
        auction_winner=name
print(f"{auction_winner} has won the auction with a bid of ${highest_bid}")



