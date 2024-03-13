from interface import *
import time

class investiment_market(Subject):
    _observersList = []
    _listOfPercentages = []
    def attach(self, observer,nameSubject):
        self._observersList.append(observer)
        observer.show = True
        observer.check = True
        
    def detach(self, observer,nameSubject):
        self._observersList.remove(observer)
        observer.check = False
        observer.show = False

    def notify(self):
        for observer in self._observersList:
            observer.check = True

    def addpercentage(self,value):
        self._listOfPercentages.append(value)
        self.notify()

    def info_investiment(self):
        i = 0
        j = 0
        total_positive = 0
        total_negative = 0
        for percentage in self._listOfPercentages:
            if percentage < 0:
                total_negative += percentage
                i += 1
            elif percentage > 0:
                total_positive += percentage
                j += 1
        if j > 0:
            media_positive = total_positive / j
            texto = f"People who opted for investment lately received a gain of {round(media_positive,2)}%\n"
        else:
            texto = f"People who chose investment lately did not receive gain\n"
        if i > 0:
            media_negative = total_negative / i
            texto2 = f"People who opted for investment recently received a loss of {round(media_negative,2)}%"
        else:
            texto2 = "People who chose to invest recently did not receive any losses"
        return texto + texto2