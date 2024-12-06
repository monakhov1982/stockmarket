# The Stock Market
import random

## Parameters
initial_cash = 100000

company_names = [
    "Lumora Biotech Inc.",
    "Vertexion Systems",
    "GreenSprout Innovations",
    "Auralis Pharmaceuticals",
    "DeepCore Analytics",
    "NexTech Nexus",
    "CryoFusion Dynamics",
    "Velociti Robotics",
    "BioMorph Therapeutics",
    "SkyNetra Solutions",
    "EcoSynthetics Labs",
    "QuantumGrid Energy",
    "NovaSphere Technologies",
    "AgriVantage Global",
    "BlueHorizon Materials",
    "NeuraGenomics Inc.",
    "SynthCor Medical",
    "Pinnacle AI Systems",
    "BioHaven Enterprises",
    "CoreX Innovations"
]

ticker_symbols = [
    "LMB",
    "VTX",
    "GRS",
    "AUR",
    "DCA",
    "NX",
    "CFD",
    "VL",
    "BM",
    "SKY",
    "ECS",
    "QG",
    "NS",
    "AG",
    "BLU",
    "NR",
    "SC",
    "PN",
    "BH",
    "CXI"
]

investment_entities = [
    "Apex Growth Partners",
    "SilverWave Ventures",
    "NorthStar Equity Group",
    "SummitPoint Capital",
    "BlueStone Asset Management",
    "Momentum Growth Fund",
    "Golden Arc Investments",
    "EverGreen Capital Partners",
    "Vanguard Horizon Fund",
    "NovaCrest Ventures",
    "Zenith Peak Advisors",
    "CoreVision Capital",
    "Sapphire Ridge Investments",
    "IronBridge Equity Partners",
    "Skyline Growth Fund",
    # "Crimson Tide Ventures",
    # "EcoSphere Investments",
    # "Prime Meridian Capital",
    # "Global Nexus Fund",
    # "UnityBridge Investors",
    # "Ascendia Partners",
    # "Titanium Horizon Ventures",
    # "QuantumEdge Capital",
    # "Verdant Valley Growth Fund",
    # "BrightFuture Investments",
    # "AnchorStone Equity",
    # "InfinityPath Ventures",
    # "Aurora Gate Capital",
    # "ElevateEdge Partners",
    # "BoldStrive Investments",
    # "Cobalt Spring Fund",
    # "RadiantCore Advisors",
    # "CedarPoint Ventures",
    # "NextAxis Capital",
    # "StellarBloom Growth Partners",
    # "TrailBlazer Equity Group",
    # "HorizonAxis Fund",
    # "PinnacleField Investments",
    # "VertexEdge Partners",
    "LatticeBridge Ventures"
]


share_price_rise_descriptions = [
    "shares surged after better-than-expected quarterly earnings.",
    "shares climbed on news of a major acquisition deal.",
    "shares spiked amid positive market sentiment and high trading volume.",
    "shares rallied following optimistic guidance from the company.",
    "shares rose sharply as analysts upgraded their ratings.",
    "shares gained after a key product received regulatory approval.",
    "shares advanced on strong demand in the sector.",
    "shares appreciated following an announcement of increased dividends.",
    "shares jumped on reports of robust revenue growth.",
    "shares increased after the company announced a major partnership agreement."
]

share_price_decline_descriptions = [
    "shares fell sharply after disappointing quarterly earnings.",
    "shares dropped amid concerns over regulatory scrutiny.",
    "shares slid following weaker-than-expected sales results.",
    "shares declined as market sentiment turned negative.",
    "shares tumbled after the company issued a profit warning.",
    "shares dipped on news of a significant executive departure.",
    "shares lost ground as analysts downgraded their ratings.",
    "shares sank following unfavorable economic data.",
    "shares retreated after a missed revenue target.",
    "shares plunged amid fears of increasing competition in the sector."
]

politics_economy_statements = [
    "Markets rally after politicians actually agree on something for the first time in years.",
    "Investors cautiously optimistic as government promises to 'definitely' avoid a shutdown this time.",
    "Global stocks rise as a major summit ends with more handshakes than arguments.",
    "Markets tumble after a surprise tweet sends economists scrambling for their sanity.",
    "Wall Street celebrates as lawmakers pass a bill that doesn't have 'crisis' in the title.",
    "Energy stocks spike after leaders discover solar panels work better when installed in sunny places.",
    "Markets wobble as central bank hints at raising interest rates 'eventually, maybe, we’ll see.'",
    "Tech stocks soar after regulators declare they 'kind of understand' how the internet works now.",
    "Investors rejoice as the latest inflation numbers are described as 'only mildly terrifying.'",
    "Currency markets react to a government official's bold claim that 'money is still important.'",
    "Economic growth forecasts climb after a global trade deal avoids using the word 'tariff.'",
    "Markets dip as a politician confidently announces a plan to 'fix the economy by Friday.'",
    "Analysts struggle to explain market movements after a speech about 'economic vibes.'",
    "Stock futures rise as a new bipartisan committee agrees to 'agree later' on fiscal policy.",
    "Global markets slump after a surprise tax proposal is revealed to be written on a napkin.",
    "Investors retreat to safe havens after a press conference described as 'ambitiously vague.'",
    "Currency valuations swing wildly after leaders introduce the concept of 'digital wooden nickels.'",
    "Markets cheer as labor reports show record hiring in 'whatever it is people do on TikTok.'",
    "Stocks wobble as a top official promises the economy is 'almost definitely not doomed.'",
    "Investors brace for turbulence as lawmakers debate whether recessions are 'just a mindset.'"
]


dollar_art = """
 $$$$$$$   $$$$$$$   $$$$$$$
$$     $$ $$     $$ $$     $$
$$        $$        $$
 $$$$$$    $$$$$$    $$$$$$
      $$       $$       $$
$$     $$ $$     $$ $$     $$
 $$$$$$$   $$$$$$$   $$$$$$$
"""

rising_stock_plot = """
Price ^
      |
      |            *
      |          *
      |        *
      |      *
      |    *
      |  *
      | *
      +--------------------> Time
"""

divider_line = "################################################\r"



## Classes
class Company:
    def __init__(self, name, symbol, price):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.trend = random.gauss(self.price*0.002, self.price*0.001) # where the price tends to go
        self.bankrupt = False
                
    def __repr__(self):
        if self.bankrupt==False:
            description = f"{self.name} ({self.symbol}) shares cost ${self.price:,}.\n"
        else:
            description = f"{self.name} ({self.symbol}) was good, but it went bankrupt.\n"
        return description
        
    def update_price(self):
        if self.bankrupt==True:
            return
        change = random.gauss(0, self.price/5) + self.trend 
        self.price += round(change,1)
        if self.price<=0:
            self.price = 0
            self.bankrupt = True
            print("Bankrupt\r")
            print(f"Company {self.name} went bankrupt!\n")
        
        
class Investor:
    def __init__(self, name, cash, portfolio):
        self.name = name
        self.cash = cash
        self.portfolio = portfolio # this is dictionary
        self.value = self.cash
        
    def __repr__(self):
        return f"Investment firm {self.name} has ${round(self.cash):,} in cash. Its total portfolio value is ${round(self.value):,}.\r"
        
    def buy(self, symbol, qty, price, print_transaction=True):
        if comp_dict[symbol].bankrupt==True:
            print(f"{symbol} is bankrupt, can't buy their stock.\r")
            return
        if qty*price>self.cash:
            print("Not enough cash!\r")
            return
        if not symbol in self.portfolio:
            self.portfolio[symbol] = [0, 0] # qty, price (cost basis)
        
        # calculate new cost basis
        old_cost_basis = self.portfolio[symbol][1]
        old_qty = self.portfolio[symbol][0]
        total_qty = old_qty + qty
        new_cost_basis = (old_cost_basis*old_qty + price*qty)/total_qty
        
        # update attributes
        self.cash -= qty*price
        self.portfolio[symbol][0] += qty
        self.portfolio[symbol][1] = new_cost_basis
        if print_transaction==True:
            print(f"{self.name} purchased {qty} shares of {symbol} at ${round(price,2):,}.\r")
        
    def sell(self, symbol, qty, price, print_transaction=True):
        if comp_dict[symbol].bankrupt==True:
            print(f"{symbol} is bankrupt, can't sell their stock.\r")
            return    
        if not symbol in self.portfolio:
            print(f"{self.name} can't sell {symbol},it is not in portfolio of (short selling is not implemented yet...).\r")
            return
        if qty > self.portfolio[symbol][0]:
            print(f"Can't sell! {self.name} does not have enough shares of stock {symbol}.\r")
            return
        self.portfolio[symbol][0] -= qty
        self.cash += qty*price
        if print_transaction==True:
            print(f"{self.name} has sold {qty} shares of {symbol} at ${round(price,2):,}.\n")

    def get_value(self):
        value = self.cash
        for symbol,pos in self.portfolio.items():
            value += pos[0] * comp_dict[symbol].price
        self.value = value
        return value
        
    def print_portfolio(self):
        symbols = []
        qties = []
        prices = []
        values = []
        for k,v in self.portfolio.items():
            symbols.append(k)
            qties.append(v[0])
            price = comp_dict[k].price
            prices.append(price)
            values.append(price*v[0])
        idx = idx_sorted(values)
        print(f"Current holdings of {self.name}:\r")
        for h in idx:
            print(f"{symbols[h]}\t${round(values[h]):,}\r")
        print(f"Cash ${round(self.cash):,} \n")
        
        
## Functions
        
# Show companies info
def show_companies():
    symbols = []
    names = []
    prices = []
    for c in companies:
        symbols.append(c.symbol)
        names.append(c.name)
        prices.append(c.price)
    idx = idx_sorted(names, reverse=False) # 'False' because I'm sorting them by alphabet
    print(divider_line)
    print('\n Companies and their stock prices:\r')
    print("Company \t\t Symbol \t Price \t Day change \t Week change\r")
    for j in idx:
        c = companies[j]
        if c.bankrupt==False:
            if len(history_c[c.symbol])>=2:
                last_price = history_c[c.symbol][-2]
            else:
                last_price = c.price
            if len(history_c[c.symbol])>=7:
                last_week_price = history_c[c.symbol][-7]
            else:
                last_week_price = c.price
            day_change = (c.price - last_price)/last_price
            week_change = (c.price-last_week_price)/last_week_price        
        else:
            day_change = 0
            week_change = 0
        print(f"{c.name.ljust(30)} {c.symbol.ljust(4)}\t ${round(c.price,2):,}\t\t{day_change:+.2f}\t\t{week_change:+.2f}\r")
    print("\n")
        
        
# Show investors ranking
def show_investors():
    names = []
    values = []
    for i in investors:
        names.append(i.name)
        values.append(i.value)
    idx = idx_sorted(values)
    print("Current investors ranking:\r")
    for j in range(len(investors)):
        k = idx[j]
        name = names[k]
        if k==(len(investors)-1): # highlight player's name in the list
            name = "*** " + name
        name = name.ljust(30)
        print(f"{j+1}\t{name}\t${round(values[k]):,}\r")
    print("\n")
    return idx
    

# simulate multiple rounds of buying and selling by other investors, update stock prices and investors portfolios values
def update_market(n_iter=1, print_info=True):
    global day
    for time_step in range(n_iter):
        day += 1
    
        # Update companies
        change = [] # day change of price
        for c in companies:
            if c.bankrupt==False:
                last_price = c.price
                c.update_price()
                current_price = c.price
                price_change = (current_price-last_price)/last_price
            else:
                current_price = 0
                price_change = 0
            history_c[c.symbol].append(current_price)
            change.append(price_change)
            
        # Print some news about the market, top day gainers and loosers
        if print_info==True:
            idx = idx_sorted(change)
            gainer = companies[idx[0]]
            gain = change[idx[0]]
            loser = companies[idx[-1]]
            loss = change[idx[-1]]
            print("*** Market news ***\r")
            print(f"{random.choice(politics_economy_statements)}")
            print(f"{gainer.name} {random.choice(share_price_rise_descriptions)} ")
            print(f"{loser.name} {random.choice(share_price_decline_descriptions)}\r")
        
        # Update investors
        if print_info==True:
            print("\n *** Other investors make their moves *** \r")
        for i in investors:
            i.get_value()
            history_i[i.name].append(i.value)
            if i != user: # don't do anything for the user
                # Buying
                c = random.choice(companies)
                qty = random.randint(10,100)
                if i.cash > qty*c.price:
                    i.buy(c.symbol, qty, c.price, print_info)
                # Selling
                if i.cash < 0.1*initial_cash:
                    symbol = random.choice(list(i.portfolio.keys()))
                    qty = i.portfolio[symbol][0]
                    i.sell(symbol, qty, comp_dict[symbol].price, print_info)

# View one or more investor's details
def view_investor(n):
    i = investors[n]
    i.get_value()
    print(i)
    i.print_portfolio()
    print("\n")
    
# Get indices of sorted list
def idx_sorted(values, reverse=True):    
    return sorted(range(len(values)), key=lambda k: values[k], reverse=reverse) # https://stackoverflow.com/questions/7851077/how-to-return-index-of-a-sorted-list
    
# Check if user entered valid quantity and convert to integer
def process_qty(qty):
    try:
        qty = int(qty)
    except ValueError:
        print(divider_line)
        print("The quantity must be a positive integer.\r")   
        userinput = main_menu()
    if qty<=0:
        print(divider_line)
        print("The quantity must be a positive integer.\r")   
        userinput = main_menu()
    return qty
    
    
# UI    
def main_menu():
    print("\n# MAIN MENU #\r")
    print(f"This is day {day}.\r")
    print("(press one of the keys (upper or lower case - doesn't matter) and then Enter)\r")
    userinput = input("\r Options:\n C\t Show the list of companies and trade stocks  \n I\t Show the leaderboard of investors (and view individual investors info)  \n U\t Pass and let other investors make their moves  \n P\t View your portfolio  \n E\t Exit the game . \n").upper()
    if userinput=="C":
        show_companies()
        print("Trading menu:\r")
        userinput = input("\n To buy a stock press B \n To sell a stock press S \n To return to main menu press M (or any other key). \n").upper()
        
        # Buying
        if userinput=="B":
            symbol = input("Enter stock symbol and press Enter.\n").upper()
            if symbol in comp_dict:
                price = comp_dict[symbol].price
                if comp_dict[symbol].bankrupt==False:
                    qty = input("Enter number of shares and press Enter. \n")
                    qty = process_qty(qty)
                    total = round(price*qty,2)
                    if total > user.cash:
                        print(divider_line)
                        print(f"You don't have enough cash. You have only ${round(user.cash,2):,}, but the order total is ${total:,}\r")
                        userinput = main_menu()
                    else:
                        print(f"You are about to place market buy order for {qty} shares of {symbol}. The price is ${round(price,2):,}, total is ${total:,}. \r")
                        confirmation = input("Press Y to confirm, N to cancel.\n").upper()
                        if confirmation=="Y":
                            print(divider_line)
                            user.buy(symbol, qty, price)
                            print("\n")
                            update_market()                            
                            userinput = main_menu()
                        elif confirmation=="N":
                            print(divider_line)
                            print("Order canceled.\r")
                            userinput = main_menu()
                else:
                    print(divider_line)
                    print("That company is bankrupt!\n")
                    userinput = main_menu()
            else:
                print(divider_line)
                print(f"Symbol {symbol} is not available. Check the list of available companies.\n")
                userinput = main_menu()   
            
        # Selling
        elif userinput=="S":
            symbol = input("Enter stock symbol and press Enter.\n").upper()
            if symbol in user.portfolio:
                price = comp_dict[symbol].price
                if comp_dict[symbol].bankrupt==False:
                    qty_available = user.portfolio[symbol][0]
                    print(f"You have {qty_available} shares of {symbol}.\r")
                    qty = input("Enter number of shares and press Enter. \n")
                    qty = process_qty(qty)                    
                    if qty > qty_available:
                        print(divider_line)
                        print("You don't have enough shares. Check your portfolio to see how many shares you own. \r")
                        userinput = main_menu()
                    else:
                        total = round(price*qty,2)
                        cost_basis = round(user.portfolio[symbol][1])
                        print(f"You are about to place market sell order for {qty} shares of {symbol}. The price is ${round(price,2):,}, total is ${total:,}. The cost basis is ${cost_basis:,}. \r")
                        confirmation = input("Press Y to confirm, N to cancel. Then press Enter. \n").upper()
                        if confirmation=="Y":
                            print(divider_line)
                            user.sell(symbol, qty, price)
                            print("\n")
                            update_market()
                            userinput = main_menu()
                        elif confirmation=="N":
                            print(divider_line)
                            print("Order canceled.\r")
                            userinput = main_menu()
                else:
                    print(divider_line)
                    print("That company is bankrupt!\n")
                    userinput = main_menu()
            else:
                print(divider_line)
                print(f"You don't have any {symbol} in your portfolio (shot selling is not available in this version of the game). Check your portfolio to see what you can sell.\n")
                userinput = main_menu()                
        else:
            userinput = main_menu()
            
    elif userinput=="I":
        print(divider_line)
        idx = show_investors()
        userinput = input("To view the portfolio of one of investors enter its number from the table above (and then Enter)\n To return to main menu press M (or any other key) \n")
        allowed_values = [str(num) for num in range(len(investors))]
        print("\n")
        if userinput in allowed_values:
            print(divider_line)
            view_investor(idx[int(userinput)-1])
            userinput = main_menu()
        else:
            print(divider_line)
            print("Enter valid number from the table.\r")
            userinput = main_menu()
    elif userinput=="U":
        print(divider_line)
        update_market()
        userinput = main_menu()  
    elif userinput=="P":
        print("\n")
        print(divider_line)
        view_investor(-1) # the user is the last investor in the list
        userinput = main_menu()  
    elif userinput=="E":
        print(divider_line+'Good bye!\r')
        print(rising_stock_plot)
        quit()
    else:
        print(divider_line+"User input not recognized. Please refer to the menu. \r")
        userinput = main_menu()  
    return userinput    
       
    
# Initialize companies
companies = []
comp_dict = {}
for i in range(len(company_names)):
    companies.append(Company(company_names[i], ticker_symbols[i], round(random.uniform(10, 200), 1)))
    comp_dict[ticker_symbols[i]] = companies[i] # create a dictionary of companies for easy lookup
history_c = {c.symbol:[c.price] for c in companies}
   
    
# Initialize investors
investors = []
for i in range(len(investment_entities)):
    investors.append(Investor(investment_entities[i], initial_cash, {}))
history_i = {i.name:[initial_cash] for i in investors}
    
    
# Initialize user and start the game
print(divider_line+"\nHello! Welcome to The Stock Market!\n")
print(dollar_art)
print("Here you can make money by trading stocks of companies such as {}, {} and many others.\n".format(random.choice(company_names),random.choice(company_names)))
print("You will be competing with other investors including {}, {} and {}. \n".format(random.choice(investment_entities),random.choice(investment_entities),random.choice(investment_entities)))
day = 1
username = input("Please enter your name.\n")
# username = "Misha"
user = Investor(username, initial_cash, {})
investors.append(user)
history_i[user.name] = [initial_cash]
update_market(n_iter=3, print_info=False) # run few rounds of simulation to accumulate differences between investors and changes of stock prices 
day=1 # reset the 'day' variable, so the user will start with Day 1
print(divider_line)
print(f"Welcome, {username}! You start with ${initial_cash:,}\r")
userinput = main_menu()