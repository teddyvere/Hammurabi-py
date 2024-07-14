import random




def time(year):
    return year + 1
    
def askHowManyAcresToBuy(land_price, bushels_stor, acres_owned):
    print("\nHow many acres will you buy, your highness? ")
    acres_to_buy = int(input("Enter the number of acres: "))
    total_price = land_price * acres_to_buy
    
    if total_price > bushels_stor:
        print("\nYou can't afford that, lord.")
    else:
        print(f"\nYou have purchased {acres_to_buy} acres of land.")
        bushels_stor -= total_price
        acres_owned += acres_to_buy
        print(f"\nYou now have {acres_owned} acers in you kingdom good lord" )
    return bushels_stor, acres_owned
          
def askHowManyAcresToSell(acres_owned, bushels_stor, land_price):
    print("\nHow many acres will you sell, my liege?")
    acres_to_sell = int(input("Enter the number of acres: "))

    if acres_to_sell > acres_owned:
        print("\nYou don't have enough land for that, lord.")
    else:
        print(f"\nYou have sold {acres_to_sell} acres of land.")
        acres_owned -= acres_to_sell
        bushels_stor += acres_to_sell * land_price  # Add the price of sold acres to bushels storage
        print(f"\nYou now have {acres_owned} acers in you kingdom good lord" )
        
    return bushels_stor, acres_owned

def askHowMuchGrainToFeedPeople(bushels_stor, bushel_feed):
    print("\nMy king, how much grain should we spare on our citizens?")
    bushel_feed = int(input("\nEnter the number of bushels: "))
    
    if bushel_feed > bushels_stor:
        print("\nwe don't have enough food for this lord")
    else:
        print("\nIt will be done at once my lord")
        bushels_stor -= bushel_feed
        print(f"\nWe now have {bushels_stor} bushels reemaining in storage sire ")
    return bushels_stor, bushel_feed

def askHowManyAcresToPlant(bushels_stor):
    print("\n How much grain should we plant wise lord?")
    planted_grain = int(input("\n Enter the number of grain: "))
    if planted_grain > bushels_stor:
        print("\nwe don't have enough grain for this lord")
    else:
        print("\nRight away my king")
        bushels_stor -= planted_grain
        print(f"\nWe now have {bushels_stor} bushels reemaining in storage sire ")
    return bushels_stor

def plagueDeaths(population):
    plauge_report = population / 2
    plague = random.randint(1,100) 
    if plague <= 15:
        print(f"\nA plauge has decimated our population and killed {plauge_report} citizens ")
        return population / 2
    else:
        return population
 
def starvationDeaths(population, bushel_feed):
    bushels_needed = population * 20
    bushels_needed -= bushel_feed
    starvation_stats = bushels_needed / 20
    if bushel_feed <= bushels_needed:
        print(f"\n {starvation_stats} people starved to death O king")
        population = bushel_feed / 20
        starvation_stats = bushels_needed / 20
        return population, starvation_stats
    elif bushel_feed >= bushels_needed:
        return population, starvation_stats
       
def uprising(population, starvation_stats):
    if starvation_stats >= population * 0.45:
        print("\nMy lord the people are are revolting because too many of them starved D:")
        return 999
    return None


            
    


def game():
    global population, bushels_stor, acres_owned, land_price, year
    population = 100
    bushels_stor = 2800
    acres_owned = 1000
    land_price = 19
    year = 1
    bushel_feed = 0
    starvation_stats = 0
    
    for i in range(10):
        if 0 < population and land_price < 900:
            print(f"\nGreat Hammurabi!\nYou are in year {year} of your ten-year rule.\nIn the previous year, {starvation_stats} people starved to death.\nIn the previous year, 0 people entered the kingdom.\nThe population is now {population}.\nWe harvested 0 bushels at 0 bushels per acre.\nRats destroyed 0 bushels, leaving {bushels_stor} bushels in storage.\nThe city owns {acres_owned} acres of land.\nLand is currently worth {land_price} bushels per acre.")
        
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
        
            results = askHowManyAcresToPlant(bushels_stor)
            if results:
                bushels_stor = results
        
            population = plagueDeaths(population)
        
            results = starvationDeaths(population, bushel_feed)
            if results:
                population, starvation_stats = results
                
            results = uprising(population, starvation_stats)
            if results:
                land_price = results   
            
        else:
            print(f"\nYou have been dethroned!!\nIn year {year} of your rule.\nIn the previous year, {starvation_stats} people starved to death.\nIn the previous year, 0 people entered the kingdom.\nThe population is now {population}.\nWe harvested 0 bushels at 0 bushels per acre.\nRats destroyed 0 bushels, leaving {bushels_stor} bushels in storage.\nThe city owns {acres_owned} acres of land.\nLand is currently worth {land_price} bushels per acre.\nBetter luck in the next life")
            break
        
if __name__ == "__main__":
    game()