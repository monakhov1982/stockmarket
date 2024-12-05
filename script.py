# The Stock Market
import random
import numpy

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
    "Crimson Tide Ventures",
    "EcoSphere Investments",
    "Prime Meridian Capital",
    "Global Nexus Fund",
    "UnityBridge Investors",
    "Ascendia Partners",
    "Titanium Horizon Ventures",
    "QuantumEdge Capital",
    "Verdant Valley Growth Fund",
    "BrightFuture Investments",
    "AnchorStone Equity",
    "InfinityPath Ventures",
    "Aurora Gate Capital",
    "ElevateEdge Partners",
    "BoldStrive Investments",
    "Cobalt Spring Fund",
    "RadiantCore Advisors",
    "CedarPoint Ventures",
    "NextAxis Capital",
    "StellarBloom Growth Partners",
    "TrailBlazer Equity Group",
    "HorizonAxis Fund",
    "PinnacleField Investments",
    "VertexEdge Partners",
    "LatticeBridge Ventures"
]


print("\nHello! Welcome to The Stock Market!\n")
print("Here you can make tons of money by trading stocks of companies such as {}, {} and many others.\n".format(random.choice(company_names),random.choice(company_names)))
print("You will be competing with other investors including {}, {} and {}. \n".format(random.choice(investment_entities),random.choice(investment_entities),random.choice(investment_entities)))
print("You start with ${}.\n".format(str(initial_cash)))

class Company:
    def __init__(self, name, symbol, price, shares_total, revenue, revenue_est):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.shares_total = shares_total
        self.shares_outstanding = shares_total
        self.revenue = revenue
        self.revenue_est = revenue_est
        self.market_cap = self.shares_total*self.price
        self.trend = random.gauss(0, self.price*0.001) # where the price tends to go
        self.bankrupt = False
                
    def __repr__(self):
        if self.bankrupt==False:
            description = "{name} ({symbol}) shares cost ${price}. It's latest revenue is ${revenue} and market capitalization is ${marketcap}.\n".format(name=self.name,symbol=self.symbol, price=str(round(self.price,1)), revenue=str(self.revenue), marketcap=str(round(self.market_cap)))
        else:
            description = "{self.name} ({self.symbol}) was good, but it went bankrupt.\n"
        return description
        
    def update_price(self):
        if self.bankrupt==True:
            return
        change = random.gauss(0, self.price/10) + self.trend 
        self.price += round(change,1)
        if self.price<=0:
            self.price = 0
            self.bankrupt = True
            self.market_cap = 0
            self.revenue = 0
            self.revenue_est = 0
            print("Company {} went bankrupt!\n".format(self.name))
            return
        self.market_cap = self.shares_total*self.price # update Market Capital too
        
    def update_revenue(self):
        if self.bankrupt==True:
            return    
        random_number = random.gauss(0, self.revenue/10)
        self.revenue += round(random_number,1)        
        
        
class Investor:
    def __init__(self, name, cash, portfolio):
        self.name = name
        self.cash = cash
        self.portfolio = portfolio # this is dictionary
        self.value = self.cash
        
    def __repr__(self):
        return "Investment firm {name} has ${cash} in cash. Its total portfolio value is ${value}\n".format(name=self.name, cash=str(round(self.cash)), value=str(round(self.value)))
        
    def buy(self, symbol, qty, price):
        if comp_dict[symbol].bankrupt==True:
            print("{} is bankrupt, can't buy their stock.\r".format(symbol))
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
        print("{name} purchased {n} shares of {symbol} at ${price}.\r".format(name=self.name, symbol=symbol, n=str(qty), price=str(round(price,1))))
        
    def sell(self, symbol, qty, price):
        if comp_dict[symbol].bankrupt==True:
            print("{symbol} is bankrupt, can't sell their stock.\r")
            return    
        if not symbol in self.portfolio:
            print("{} can't sell {},it is not in portfolio of (short selling is not implemented yet...).\r".format(self.name, symbol))
            return
        if qty > self.portfolio[symbol][0]:
            print("Can't sell! {} does not have enough shares of stock {}.\r".format(self.name,symbol))
            return
        self.portfolio[symbol][0] -= qty
        self.cash += qty*price
        #comp_dict[symbol].shares_outstanding += qty
        print("{name} has sold {n} shares of {symbol} at ${price}.\n".format(name=self.name, symbol=symbol, n=str(qty), price=str(price)))    

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
            # print(price)
        idx = sorted(range(len(values)), key=lambda k: values[k], reverse=True) # https://stackoverflow.com/questions/7851077/how-to-return-index-of-a-sorted-list
        print("Holings of {}:\r".format(self.name))
        for h in idx:
            print("{}\t${:,}\r".format(symbols[h], round(values[h])))
        print("Cash ${:,} \n".format((round(self.cash))))
        
# show companies
def show_companies():
    symbols = []
    names = []
    prices = []
    for c in companies:
        symbols.append(c.symbol)
        names.append(c.name)
        prices.append(c.price)
    idx = sorted(range(len(names)), key=lambda k: names[k])
    print('\nCompanies and their stock prices:\r')
    print("Company (symbol)\t Price \t Day change \t Week change\r")
    for j in idx:
        c = companies[j]
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
        print("{} ({})\t${:,}\t{:+.2f}\t{:+.2f}\r".format(c.name, c.symbol, round(c.price,2), day_change, week_change))
    print("\n")
        
        
# rank investors
def show_investors():
    names = []
    values = []
    for i in investors:
        names.append(i.name)
        values.append(i.value)
    # print(values)
    idx = sorted(range(len(values)), key=lambda k: values[k], reverse=True)
    print("Most successful investors are:\r")
    for j in range(10):
        print("{}\t{}\t${:,}\r".format(str(j+1), names[idx[j]], round(values[idx[j]])))
    print("\n")
    
# Initialize companies
companies = []
comp_dict = {}
for i in range(len(company_names)):
    companies.append(Company(company_names[i], ticker_symbols[i], round(random.uniform(10, 200), 1), round(random.uniform(100000, 100000)), round(random.uniform(1000000, 1000000)), round(random.uniform(1000000, 1000000))))
    comp_dict[ticker_symbols[i]] = companies[i] # create a dictionary of companies for easy lookup
history_c = {c.symbol:[c.price] for c in companies}
# print(history_c)
    
# Initialize investors
investors = []
for i in range(len(investment_entities)):
    investors.append(Investor(investment_entities[i], initial_cash, {}))
history_i = {i.name:[initial_cash] for i in investors}

    
    
# Test methods
username = input("Please enter your name.\n")
u = Investor(username, initial_cash, {})
print(f"Welcome, {username}! You start with ${initial_cash:,}\r")
userinput = input("To show the list of companies press C.\n To show the leaderboard of investors press I \n Then press Enter.\n")
if userinput.upper()=="C":
    show_companies()
elif userinput.upper()=="I":
    show_investors()
    


# simulate multiple rounds of buying
for t in range(1):
    for c in companies:
        c.update_price()
        
        history_c[c.symbol].append(c.price)
    for i in investors:
        i.get_value()
        history_i[i.name].append(i.value)
        c = random.choice(companies)
        qty = random.randint(10,100)
        if i.cash > qty*c.price:
            i.buy(c.symbol, qty, c.price)
        
        
    
# check portfolios:
for i in investors:
    i.get_value()
    print(i)
    i.print_portfolio()
    

    
    

    
