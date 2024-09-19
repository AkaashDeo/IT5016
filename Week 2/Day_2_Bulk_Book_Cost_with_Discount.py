
"""
Calculate the wholesale cost for 60 copies of a book.

Author: Akaash Deo

"""

# INPUT
book_cover_price = 24.95                                  # The price of a single book cover
discount = 40 / 100                                       # The discount rate applied to the book price (40%)
copies = 60                                               # The number of copies to be purchased
# PROCESS
book_discount_price = book_cover_price * discount         # Calculate the discount amount per book
unit_price = book_cover_price - book_discount_price       # Determine the price of each book after applying the discount
total_book = unit_price * copies                          # Calculate the total cost for all copies of the book after discount
shipping = 3 + 0.75 * (copies - 1)                        # Calculate the shipping cost, Base shipping cost is $3, plus $0.75 for each additional book (beyond the first)
grand_total = total_book + shipping                       # Calculate the grand total, which is the sum of the total book cost and the shipping cost
# OUTPUT
print(grand_total)                                        # Print the grand total cost to the console

