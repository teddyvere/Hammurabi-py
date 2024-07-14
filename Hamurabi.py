import random




def time(year):
    return year + 1
    
def askHowManyAcresToBuy(land_price, bushels_stor, acres_owned):
    while True:
        try:
            print("\nHow many acres will you buy, your highness? ")
            acres_to_buy = int(input("Enter the number of acres: "))
            total_price = land_price * acres_to_buy
    
            if total_price > bushels_stor:
                print("\nYou can't afford that, lord.")
            else:
                print(f"\nYou have purchased {acres_to_buy} acres of land.")
                bushels_stor -= total_price
                acres_owned += acres_to_buy
                print(f"\nYou now have {acres_owned} acres in you kingdom good lord" )
                return bushels_stor, acres_owned
        except ValueError:
            print("\nPlease input a valid number")
          
def askHowManyAcresToSell(acres_owned, bushels_stor, land_price):
    while True:
        try:
            print("\nHow many acres will you sell, my liege?")
            acres_to_sell = int(input("Enter the number of acres: "))

            if acres_to_sell > acres_owned:
                print("\nYou don't have enough land for that, lord.")
            else:
                print(f"\nYou have sold {acres_to_sell} acres of land.")
                acres_owned -= acres_to_sell
                bushels_stor += acres_to_sell * land_price  # Add the price of sold acres to bushels storage
                print(f"\nYou now have {acres_owned} acres in you kingdom good lord" )
                return bushels_stor, acres_owned
        except ValueError:
            print("\nPlease input a valid number")

def askHowMuchGrainToFeedPeople(bushels_stor, bushel_feed):
    while True:
        try:
            print("\nMy king, how much grain should we spare on our citizens?")
            bushel_feed = int(input("\nEnter the number of bushels: "))
    
            if bushel_feed > bushels_stor:
                print("\nwe don't have enough food for this lord")
            else:
                print("\nIt will be done at once my lord")
            bushels_stor -= bushel_feed
            print(f"\nWe now have {bushels_stor} bushels remaining in storage sire ")
            return bushels_stor, bushel_feed
        except ValueError:
            print("\nPlease input a valid number")
def askHowManyAcresToPlant(bushels_stor, population, acres_owned):
    while True:
        try:
            print("\nHow much grain should we plant wise lord?")
            planted_grain = int(input("\nEnter the number of grain: "))

            if planted_grain > bushels_stor:
                print("\nWe don't have enough grain for this lord")
            elif planted_grain > acres_owned:
                print("\nWe don't have enough land for this lord ")
            elif planted_grain > population * 9:
                print("\nWe don't have enough people for this lord")
            else:
                print("\nRight away my king")
                bushels_stor -= planted_grain
                print(f"\nWe now have {bushels_stor} bushels remaining in storage sire ")
                return bushels_stor, planted_grain
        except ValueError:
            print("\nPlease input a valid number")
        
def harvest(planted_grain, bushels_stor):
    acre_yield = random.randint(1,6)
    seed_yield = acre_yield * planted_grain
    if planted_grain > 0:
        bushels_stor += seed_yield
        return bushels_stor, seed_yield, acre_yield
    return None
    
    
def plagueDeaths(population):
    plague_report = population / 2
    plague = random.randint(1,100) 
    if plague <= 15:
        print(f"\nA plague has decimated our population and killed {plague_report} citizens ")
        return population / 2
    else:
        return population
    
def grainEatenByRats(bushels_stor, eaten_grain):
    rats = random.randint(1,100)
    if rats <= 45:
        fl_eat_grain = bushels_stor * (random.randint(10,30) / 100)
        eaten_grain = int(fl_eat_grain)
        bushels_stor -= eaten_grain
        return bushels_stor, eaten_grain
    return bushels_stor, 0

def starvationDeaths(population, bushel_feed):
    bushels_needed = population * 20
    if bushel_feed < bushels_needed:
        people_fed = bushel_feed // 20
        starvation_stats = population - people_fed
        population = people_fed
        return population, starvation_stats
    else:
        starvation_stats = 0
        return population, starvation_stats 
       
def uprising(population, starvation_stats):
    if starvation_stats >= population * 0.45:
        print("\nMy lord the people are are revolting because too many of them starved D:")
        return 999
    return None

def immigrants(population, acres_owned, bushels_stor, starvation_stats):
    if starvation_stats == 0:
        aliens = int(20 * (acres_owned + bushels_stor) / (100 * population) + 1)
        population += aliens
        return aliens, population
    return None

def newCostOfLand(land_price):
    land_price = random.randint(17,23)
    return land_price



    
           
    


def game():
    global population, bushels_stor, acres_owned, land_price, year
    population = 100
    bushels_stor = 2800
    acres_owned = 1000
    land_price = 19
    year = 1
    bushel_feed = 0
    starvation_stats = 0
    aliens = 0
    planted_grain = 0
    seed_yield = 0
    acre_yield = 0
    eaten_grain = 0
    people_fed = 0
    
    for i in range(10):
        if 0 < population and land_price < 900:
            print(f"\nGreat Hammurabi!\nYou are in year {year} of your ten-year rule.\nIn the previous year, {starvation_stats} people starved to death.\nIn the previous year, {aliens} people entered the kingdom.\nThe population is now {population}.\nWe harvested {planted_grain} bushels at {acre_yield} bushels per acre.\nRats destroyed {eaten_grain} bushels, leaving {bushels_stor} bushels in storage.\nThe city owns {acres_owned} acres of land.\nLand is currently worth {land_price} bushels per acre.")
        
            year = time(year)
        
            results = askHowManyAcresToBuy(land_price, bushels_stor,acres_owned)
            if results:
                bushels_stor, acres_owned = results
        
            results = askHowManyAcresToSell(acres_owned, bushels_stor, land_price)
            if results:
                bushels_stor, acres_owned = results
        
            results = askHowMuchGrainToFeedPeople(bushels_stor, bushel_feed)
            if results:
                bushels_stor, bushel_feed = results
        
            results = askHowManyAcresToPlant(bushels_stor, population, acres_owned)
            if results:
                bushels_stor, planted_grain = results
            
            results = harvest(planted_grain, bushels_stor)
            if results:
                bushels_stor, planted_grain, acre_yield = results
            
            results = plagueDeaths(population)
            if results:
                population = results

            results = grainEatenByRats(bushels_stor, eaten_grain)
            if results:
                bushels_stor, eaten_grain = results
        
            results = starvationDeaths(population, bushel_feed)
            if results:
                population, starvation_stats= results
                
            results = immigrants(population, acres_owned, bushels_stor, starvation_stats) 
            if results:
                aliens, population = results
                
            results = newCostOfLand(land_price)
            if results:
                land_price = results    
                
            results = uprising(population, starvation_stats)
            if results:
                land_price = results      
            
        else:
            print(f"\nYou have been dethroned!!\nIn year {year} of your rule.\nIn the previous year, {starvation_stats} people starved to death.\nIn the previous year, {aliens} people entered the kingdom.\nThe population is now {population}.\nWe harvested {planted_grain} bushels at {acre_yield} bushels per acre.\nRats destroyed {eaten_grain} bushels, leaving {bushels_stor} bushels in storage.\nThe city owns {acres_owned} acres of land.\nLand is currently worth {land_price} bushels per acre.\nBetter luck in the next life")
            break
        
if __name__ == "__main__":
    game()