from AlgorithmImports import *

class VCAlgoInjection(QCAlgorithm):

    def Initialize(self):
        self.SetCash(100000)  # Set your initial cash balance
        self.SetStartDate(2023, 10, 7)  # Set your desired start date
        self.SetEndDate(2024, 10, 7)  # Set your desired end date
        
        self.stocks = ["AAPL","GOOG","MSFT","TSLA","JPMC","AMZN", "F"]

        for stock in self.stocks:
            self.AddStock(stock, Resolution.Daily)
        
        for stock in self.stocks:
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(10, 0), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(10, 15), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(10, 30), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(10, 45), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(11, 0), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(11, 15), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(11, 30), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(11, 45), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(12, 0), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(12, 15), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(12, 30), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(12, 45), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(13, 0), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(13, 15), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(13, 30), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(13, 45), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(14, 0), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(14, 15), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(14, 30), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(14, 45), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(15, 0), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(15, 15), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(15, 30), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(15, 45), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(16, 0), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(16, 15), self.Invest)
            self.Schedule.On(self.DateRules.EveryDay(stock), self.TimeRules.At(16, 30), self.Invest)

    def Invest(self):
        # Calculate average growth rates for the past week and month for each stock
        stock_data = {}
        for stock in self.stocks:
            # Use the History method to fetch historical data
            try:
                history = self.History(stock, timedelta(30), Resolution.Daily)
                
                if history is not None and len(history) > 0:
                    # Calculate average growth rates
                    week_growth = (history["close"].pct_change() + 1).prod() - 1
                    month_growth = (history["close"].pct_change(periods=30) + 1).prod() - 1
                    
                    # Store the growth rates
                    stock_data[stock] = {"week_growth": week_growth, "month_growth": month_growth}
            except Exception as e:
                self.Debug(f"Error fetching data for {stock}: {str(e)}")

        # Rank stocks based on the weighted formula
        ranked_stocks = pd.DataFrame.from_dict(stock_data, orient='index')
        ranked_stocks["score"] = 0.7 * ranked_stocks["week_growth"] + 0.3 * ranked_stocks["month_growth"]
        ranked_stocks = ranked_stocks.sort_values(by="score", ascending=False)

        #injection of portion of portfolio into certain businesses 
        # to be held for a given amount of time
        
        injections = ["GOOGL", "AMZN", "F"]
        weights = [0.05, 0.03, 0.04]
        injection_amts = [injections, weights]

        top_stock = None
        for stock in ranked_stocks.index:
            if not stock.endswith(ranked_stocks.index[0].split("/")[1]):
                top_stock = stock
                break

        if top_pair is not None:
        # Invest in the highest-ranked stocks
            top_stock = ranked_stocks.index[0]
            second_stock = ranked_stocks.index[1]
            third_stock = ranked_stocks.index[2]
            fourth_stock = ranked_stocks.index[3]
            if top_stock in injections:
                topStockIndex = injections.index(top_stock)
                self.SetHoldings(top_stock, 0.2 + weights[topStockIndex])
            else:
                self.SetHoldings(top_stock, 0.2)

            if second_stock in injections:
                secondStockIndex = injections.index(second_stock)
                self.SetHoldings(second_stock, 0.15 + weights[secondStockIndex])
            else:
                self.SetHoldings(second_stock, 0.15)

            if third_stock in injections:
                thirdStockIndex = injections.index(third_stock)
                self.SetHoldings(third_stock, 0.1 + weights[thirdStockIndex])
            else:
                self.SetHoldings(third_stock, 0.1)

            if fourth_stock in injections:
                fourthStockIndex = injections.index(fourth_stock)
                self.SetHoldings(fourth_stock, 0.05 + weights[fourthStockIndex])
            else:
                self.SetHoldings(fourth_stock, 0.05)

    def OnData(self, data: Slice):
        pass

