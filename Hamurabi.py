import random

class Hammurabi:
    def __init__(self):
        self.population = 100
        self.bushels_stor = 2800
        self.acres_owned = 1000
        self.land_price = 19
        self.year = 1
        self.bushel_feed = 0
        self.starvation_stats = 0
        self.aliens = 0
        self.planted_grain = 0
        self.seed_yield = 0
        self.acre_yield = 0
        self.eaten_grain = 0
        self.people_fed = 0

    def time(self):
        self.year += 1

    def askHowManyAcresToBuy(self):
        while True:
            try:
                print("\nHow many acres will you buy, your highness? ")
                acres_to_buy = int(input("Enter the number of acres: "))
                total_price = self.land_price * acres_to_buy

                if total_price > self.bushels_stor:
                    print("\nYou can't afford that, lord.")
                else:
                    print(f"\nYou have purchased {acres_to_buy} acres of land.")
                    self.bushels_stor -= total_price
                    self.acres_owned += acres_to_buy
                    print(f"\nYou now have {self.acres_owned} acres in your kingdom good lord")
                    break
            except ValueError:
                print("\nPlease input a valid number")

    def askHowManyAcresToSell(self):
        while True:
            try:
                print("\nHow many acres will you sell, my liege?")
                acres_to_sell = int(input("Enter the number of acres: "))

                if acres_to_sell > self.acres_owned:
                    print("\nYou don't have enough land for that, lord.")
                else:
                    print(f"\nYou have sold {acres_to_sell} acres of land.")
                    self.acres_owned -= acres_to_sell
                    self.bushels_stor += acres_to_sell * self.land_price  # Add the price of sold acres to bushels storage
                    print(f"\nYou now have {self.acres_owned} acres in your kingdom good lord")
                    break
            except ValueError:
                print("\nPlease input a valid number")

    def askHowMuchGrainToFeedPeople(self):
        while True:
            try:
                print("\nMy king, how much grain should we spare on our citizens?")
                requested_bushel_feed = int(input("\nEnter the number of bushels: "))

                if requested_bushel_feed > self.bushels_stor:
                    print("\nWe don't have enough food for this lord")
                else:
                    self.bushel_feed = requested_bushel_feed
                    print("\nIt will be done at once my lord")
                    self.bushels_stor -= self.bushel_feed
                    print(f"\nWe now have {self.bushels_stor} bushels remaining in storage sire ")
                    break
            except ValueError:
                print("\nPlease input a valid number")

    def askHowManyAcresToPlant(self):
        while True:
            try:
                print("\nHow much grain should we plant wise lord?")
                planted_grain = int(input("\nEnter the number of bushels: "))

                if planted_grain > self.bushels_stor:
                    print("\nWe don't have enough grain for this lord")
                elif planted_grain > self.acres_owned:
                    print("\nWe don't have enough land for this lord ")
                elif planted_grain > self.population * 9:
                    print("\nWe don't have enough people for this lord")
                else:
                    self.planted_grain = planted_grain
                    print("\nRight away my king")
                    self.bushels_stor -= self.planted_grain
                    print(f"\nWe now have {self.bushels_stor} bushels remaining in storage sire ")
                    break
            except ValueError:
                print("\nPlease input a valid number")

    def harvest(self):
        acre_yield = random.randint(1, 6)
        seed_yield = acre_yield * self.planted_grain
        if self.planted_grain > 0:
            self.bushels_stor += seed_yield
            self.acre_yield = acre_yield
            self.seed_yield = seed_yield

    def plagueDeaths(self):
        plague = random.randint(1, 100)
        if plague <= 50:
            plague_report = self.population // 2
            print(f"\nA plague has decimated our population and killed {plague_report} citizens ")
            self.population //= 2

    def grainEatenByRats(self):
        rats = random.randint(1, 100)
        if rats <= 45:
            fl_eat_grain = self.bushels_stor * (random.randint(10, 30) / 100)
            self.eaten_grain = int(fl_eat_grain)
            self.bushels_stor -= self.eaten_grain

    def starvationDeaths(self):
        bushels_needed = self.population * 20
        if self.bushel_feed < bushels_needed:
            people_fed = self.bushel_feed // 20
            self.starvation_stats = self.population - people_fed
            self.population = people_fed
        else:
            self.starvation_stats = 0

    def uprising(self):
        if self.starvation_stats >= self.population * 0.45:
            print("\nMy lord the people are are revolting because too many of them starved D:")
            return True
        return False

    def immigrants(self):
        if self.starvation_stats == 0:
            aliens = int(20 * (self.acres_owned + self.bushels_stor) / (100 * self.population) + 1)
            self.population += aliens
            self.aliens = aliens

    def newCostOfLand(self):
        self.land_price = random.randint(17, 23)

    def game(self):
        for _ in range(10):
            if 0 < self.population and self.land_price < 900:
                print(f"\nGreat Hammurabi!\nYou are in year {self.year} of your ten-year rule.\nIn the previous year, {self.starvation_stats} people starved to death.\nIn the previous year, {self.aliens} people entered the kingdom.\nThe population is now {self.population}.\nWe harvested {self.planted_grain} bushels at {self.acre_yield} bushels per acre.\nRats destroyed {self.eaten_grain} bushels, leaving {self.bushels_stor} bushels in storage.\nThe city owns {self.acres_owned} acres of land.\nLand is currently worth {self.land_price} bushels per acre.")

                self.time()

                self.askHowManyAcresToBuy()
                self.askHowManyAcresToSell()
                self.askHowMuchGrainToFeedPeople()
                self.askHowManyAcresToPlant()
                self.harvest()
                self.plagueDeaths()
                self.grainEatenByRats()
                self.starvationDeaths()
                self.immigrants()
                self.newCostOfLand()

                if self.uprising():
                    break

            else:
                print(f"\nProverbs 16:18\nPride goes before destruction, a haughty spirit before a fall.\nYou have been dethroned!\nIn year {self.year} of your rule.\nIn the previous year, {self.starvation_stats} people starved to death.\nIn the previous year, {self.aliens} people entered the kingdom.\nThe population is now {self.population}.\nWe harvested {self.planted_grain} bushels at {self.acre_yield} bushels per acre.\nRats destroyed {self.eaten_grain} bushels, leaving {self.bushels_stor} bushels in storage.\nThe city owns {self.acres_owned} acres of land.\nLand is currently worth {self.land_price} bushels per acre.\nBetter luck in the next life")
                break

        if self.land_price > 900 or self.starvation_stats >= self.population * 0.45 or self.population < 1 or self.acres_owned < 1:
            print(f"\nProverbs 16:18\nPride goes before destruction, a haughty spirit before a fall.\nYou have been dethroned!\nIn year {self.year} of your rule.\nIn the previous year, {self.starvation_stats} people starved to death.\nIn the previous year, {self.aliens} people entered the kingdom.\nThe population is now {self.population}.\nWe harvested {self.planted_grain} bushels at {self.acre_yield} bushels per acre.\nRats destroyed {self.eaten_grain} bushels, leaving {self.bushels_stor} bushels in storage.\nThe city owns {self.acres_owned} acres of land.\nLand is currently worth {self.land_price} bushels per acre.\nBetter luck in the next life")
            
        elif self.acres_owned in range(900, 1100) or self.population in range(75, 110): 
            print(f"\nLuke 16:10\nWhoever can be trusted with very little can also be trusted with much, and whoever is dishonest with very little will also be dishonest with much\nCongratulations you win!\nYour unremarkable ten-year rule has come to a close.\nIn the previous year, {self.starvation_stats} people starved to death.\nIn the previous year, {self.aliens} people entered the kingdom.\nThe population is now {self.population}.\nWe harvested {self.planted_grain} bushels at {self.acre_yield} bushels per acre.\nRats destroyed {self.eaten_grain} bushels, leaving {self.bushels_stor} bushels in storage.\nThe city owns {self.acres_owned} acres of land.\nLand is currently worth {self.land_price} bushels per acre.")
        
        elif self.acres_owned < 900 or self.population < 75:
            print(f"\nProverbs 19:1\nBetter the poor whose walk is blameless than a fool whose lips are perverse.\nCongratulations you win, I guess...\nYour tumultuous ten-year rule has finally come to a close, the people rejoice.\nIn the previous year, {self.starvation_stats} people starved to death.\nIn the previous year, {self.aliens} people entered the kingdom.\nThe population is now {self.population}.\nWe harvested {self.planted_grain} bushels at {self.acre_yield} bushels per acre.\nRats destroyed {self.eaten_grain} bushels, leaving {self.bushels_stor} bushels in storage.\nThe city owns {self.acres_owned} acres of land.\nLand is currently worth {self.land_price} bushels per acre.")
        else:
            print(f"\nRevelation 19:16\nOn his robe and on his thigh he has this name written: king of kings and lord of lords.\nCongratulations you win !\nBenevolent lord, king of kings, your glorious ten-year rule has  come to a close.\nIn the previous year, {self.starvation_stats} people starved to death.\nIn the previous year, {self.aliens} people entered the kingdom.\nThe population is now {self.population}.\nWe harvested {self.planted_grain} bushels at {self.acre_yield} bushels per acre.\nRats destroyed {self.eaten_grain} bushels, leaving {self.bushels_stor} bushels in storage.\nThe city owns {self.acres_owned} acres of land.\nLand is currently worth {self.land_price} bushels per acre.\nLong live the king!")

if __name__ == "__main__":
    game = Hammurabi()
    game.game()