from replit import clear
# HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
finish = False
bids = {}


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bidd_amount = bidding_record[bidder]
        if bidd_amount > highest_bid:
            highest_bid = bidd_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not finish:
    print(logo)
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price

    one_more = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if one_more == "yes":
        clear()
    else:
        finish = True
        clear()
        # OR max_key = max(bids, key=bids.get)
        # print(f"The winner is {max_key} with a bid ${bids[max_key]}.")
        find_highest_bidder(bidding_record=bids)
        