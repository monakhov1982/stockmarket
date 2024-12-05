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
                
    def __repr__(self):
        description = "{name} ({symbol}) shares cost ${price}. It's latest revenue is ${revenue} and market capitalization is ${marketcap}.\n".format(name=self.name,symbol=self.symbol, price=str(round(self.price,1)), revenue=str(self.revenue), marketcap=str(round(self.market_cap)))
        return description
        
    def update_price(self):
        random_number = random.gauss(0, self.price/10)
        self.price += round(random_number,1)
        self.market_cap = self.shares_total*self.price
        
    def update_revenue(self):
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
        if qty*price>self.cash:
            print("Not enough cash!\n")
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
        print("{name} purchased {n} shares of {symbol} at ${price}.\n".format(name=self.name, symbol=symbol, n=str(qty), price=str(price)))
        
    def sell(self, symbol, qty, price):
        if not symbol in self.portfolio:
            print("{} can't sell {},it is not in portfolio of (short selling is not implemented yet...).\n".format(self.name, symbol))
            return
        if qty > self.portfolio[symbol][0]:
            print("Can't sell! {} does not have enough shares of stock {}.\n".format(self.name,symbol))
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
        idx = sorted(range(len(values)), key=lambda k: values[k], reverse=True) # https://stackoverflow.com/questions/7851077/how-to-return-index-of-a-sorted-list
        print("Holings of {}:\r".format(self.name))
        for h in idx:
            print("{}\t${}\r".format(symbols[h], str(round(values[h])) ))
        print("Cash ${} \n".format(str(round(self.cash))))
        
        
    
# Initialize companies
companies = []
comp_dict = {}
for i in range(len(company_names)):
    companies.append(Company(company_names[i], ticker_symbols[i], round(random.uniform(10, 200), 1), round(random.uniform(100000, 100000)), round(random.uniform(1000000, 1000000)), round(random.uniform(1000000, 1000000))))
    comp_dict[ticker_symbols[i]] = companies[i] # create a dictionary of companies for easy lookup
    
# Initialize investors
investors = []
for i in range(len(investment_entities)):
    investors.append(Investor(investment_entities[i], round(random.uniform(100000, 100000)), {}))
    
    
# Test methods

# i = investors[0]
# c = companies[0]
# print(c.symbol)
# print(i)
# print(c)
# i.buy(ticker_symbols[0],100,100)
# print(i)
# print(c)
# i.sell(ticker_symbols[0],10,100)
# print(i)
# print(c)
# c.update_price()
# print(c)
# c.update_revenue()
# i.get_value()
# print(i)
# print(c)

# simulate multiple rounds of buying
for i in investors:
    for j in range(100):
        c = random.choice(companies)
        c.update_price()
        i.buy(c.symbol, random.randint(10,100), c.price)
    
# check portfolios:
for i in investors:
    i.get_value()
    print(i)
    i.print_portfolio()
    
# rank investors
names = []
values = []
for i in investors:
    names.append(i.name)
    values.append(i.value)
# print(values)
idx = sorted(range(len(values)), key=lambda k: values[k], reverse=True)
print("Best investors are:\r")
for j in range(10):
    print("{}\t{}\t${}\r".format(str(j+1), names[idx[j]], str(round(values[idx[j]]))))
    
    
    
# i = investors[2]
# print(i)   
# for j in range(10):
    # c = random.choice(companies)
    # print(c)
    # i.buy(c.symbol, random.randint(10,20), c.price) 
    # print(i)
    # print(i.portfolio)