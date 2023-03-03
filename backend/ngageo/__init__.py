




class Continents:

    @classmethod
    def doesContinentExist(cls, continent: str):
        if continent.upper().replace(" ", "_") in Data.continents:
            return True
        else:
            return False

    @classmethod
    def getAreaInKM(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            areaTotal = 0
            for country in Data.continentToAlpha[continent.upper().replace(" ", "_")]:
                areaTotal += Countries.getAreaInKM(country)
            return areaTotal

    @classmethod
    def getAreaInMiles(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            areaTotal = 0
            for country in Data.continentToAlpha[continent.upper().replace(" ", "_")]:
                areaTotal += Countries.getAreaInKM(country)
            return math.ceil(int(areaTotal) / 2.59)

    @classmethod
    def getAreaRanking(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            areaDict = {}
            for continent2 in Data.continents:
                areaTotal = 0
                for country in Data.continentToAlpha[continent2]:
                    areaTotal += Countries.getAreaInKM(country)
                areaDict[continent2] = areaTotal
            newSorted = dict(sorted(areaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == continent.upper().replace(" ", "_"):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getAreaRankingDict(cls):
        areaDict = {}
        for continent2 in Data.continents:
            areaTotal = 0
            for country in Data.continentToAlpha[continent2]:
                if Countries.getAreaInKM(country) == 0:
                    pass
                else:
                    areaTotal += Countries.getAreaInKM(country)
            areaDict[continent2] = areaTotal
        return dict(sorted(areaDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getGDP(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            gdpTotal = 0
            for country in Data.continentToAlpha[continent.upper().replace(" ", "_")]:
                if Countries.getGDP(country) is None:
                    pass
                else:
                    gdpTotal += Countries.getGDP(country)
            return gdpTotal

    @classmethod
    def getGDPRanking(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            gdpDict = {}
            for region in Data.continents:
                gdpTotal = 0
                for country in Data.continentToAlpha[region]:
                    if Countries.getGDP(country) is None:
                        pass
                    else:
                        gdpTotal += Countries.getGDP(country)
                gdpDict[region] = gdpTotal
            newSorted = dict(sorted(gdpDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == continent.upper().replace(" ", "_"):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGDPRankingDict(cls):
        gdpDict = {}
        for continent in Data.continents:
            if Continents.getGDP(continent) is None:
                pass
            elif Continents.getGDP(continent) == 0:
                pass
            else:
                gdpDict[continent] = Continents.getGDP(continent)
        newSorted = dict(sorted(gdpDict.items(), key=lambda kv: kv[1], reverse=True))
        rank = 0
        rankingDict = {}
        for count, item in enumerate(newSorted):
            rankingDict[count + 1] = item
        return rankingDict

    @classmethod
    def getGdpPerCapita(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            return int(Continents.getGDP(continent) / Continents.getPopulation(continent))

    @classmethod
    def getGdpPerCapitaRanking(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            gdpPerCapitaDict = {}
            for continent2 in Data.continents:
                if Continents.getGdpPerCapita(continent2) == 0:
                    pass
                else:
                    gdpPerCapitaDict[continent2] = Continents.getGdpPerCapita(continent2)
            newSorted = dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == continent.upper().replace(" ", "_"):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGdpPerCapitaRankingDict(cls):
        gdpPerCapitaDict = {}
        for count, item in enumerate(Data.continents):
            if Continents.getGdpPerCapita(item) is None:
                pass
            elif Continents.getGdpPerCapita(item) == 0:
                pass
            else:
                gdpPerCapitaDict[item] = Continents.getGdpPerCapita(item)
        newSorted = dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))
        rank = 0
        rankingDict = {}
        for count, item in enumerate(newSorted):
            rankingDict[count + 1] = item
        return rankingDict

    @classmethod
    def getLargestCity(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            return Data.continentToLargestCity[continent.upper().replace(" ", "_")]

    @classmethod
    def getPopulation(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            populationTotal = 0
            for country in Data.continentToAlpha[continent.upper().replace(" ", "_")]:
                if Countries.getPopulation(country) is None:
                    pass
                else:
                    populationTotal += Countries.getPopulation(country)
            return populationTotal

    @classmethod
    def getPopulationRanking(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            populationDict = {}
            for continent2 in Data.continents:
                populationTotal = 0
                for country in Data.continentToAlpha[continent2]:
                    if Countries.getPopulation(country) is None:
                        pass
                    else:
                        populationTotal += Countries.getPopulation(country)
                populationDict[continent2] = populationTotal
            newSorted = dict(sorted(populationDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == continent.upper().replace(" ", "_"):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationRankingDict(cls):
        populationDict = {}
        for continent2 in Data.continents:
            populationTotal = 0
            for country in Data.continentToAlpha[continent2]:
                if Countries.getPopulation(country) is None:
                    pass
                else:
                    populationTotal += Countries.getPopulation(country)
            populationDict[continent2] = populationTotal
        return dict(sorted(populationDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getPopulationDensityInKM(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            population = Continents.getPopulation(continent)
            areaKM = Continents.getAreaInKM(continent)
            return float(round(population / areaKM, 2))

    @classmethod
    def getPopulationDensityInMiles(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            population = Continents.getPopulation(continent)
            areaMiles = Continents.getAreaInMiles(continent)
            return float(round(population / areaMiles, 2))

    @classmethod
    def getPopulationDensityRanking(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            populationDensityDict = {}
            for count, item in enumerate(Data.continents):
                if Continents.getPopulationDensityInKM(item) is None:
                    pass
                else:
                    populationDensityDict[item] = Continents.getPopulationDensityInKM(item)
            newSorted = dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == continent.upper().replace(" ", "_"):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationDensityRankingDict(cls):
        populationDensityDict = {}
        for count, item in enumerate(Data.continents):
            if Continents.getPopulationDensityInKM(item) is None:
                pass
            else:
                populationDensityDict[item] = Continents.getPopulationDensityInKM(item)
        return dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getCountries(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            return Data.continentToAlpha[continent.upper().replace(" ", "_")]


class Countries:

    @classmethod
    def doesCountryExist(cls, alpha3: str):
        if Countries.getRedirectedNameToAlpha3(alpha3) in Data.alpha3List:
            return True
        else:
            return False

    @classmethod
    def getAreaInKM(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToAreaKM[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getAreaInMiles(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return math.ceil(int(Data.alpha3ToAreaKM[Countries.getRedirectedNameToAlpha3(alpha3)]) / 2.59)

    @classmethod
    def getAreaRanking(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            areaDict = {}
            for count, item in enumerate(Data.alpha3List):
                if Countries.getAreaInKM(item) is None:
                    pass
                elif Countries.getAreaInKM(item) == 0:
                    pass
                else:
                    areaDict[item] = Countries.getAreaInKM(item)
            newSorted = dict(sorted(areaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == Countries.getRedirectedNameToAlpha3(alpha3):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getAreaRankingDict(cls):
        areaDict = {}
        for country in Data.alpha3List:
            if Countries.getAreaInKM(country) is None:
                pass
            elif Countries.getAreaInKM(country) == 0:
                pass
            else:
                areaDict[country] = Countries.getAreaInKM(country)
        return dict(sorted(areaDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getBorders(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            borders = Data.alpha3ToBorders[Countries.getRedirectedNameToAlpha3(alpha3)]
            if borders is None:
                return []
            else:
                return borders

    @classmethod
    def getCapital(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToCapital[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getContinent(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToContinent[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getFlagURL(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToFlagURL[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getGDP(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToGDP[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getGDPRanking(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            gdpDict = {}
            for count, item in enumerate(Data.alpha3List):
                try:
                    if Countries.getGDP(item) is None:
                        pass
                    elif Countries.getGDP(item) == 0:
                        pass
                    else:
                        gdpDict[item] = Countries.getGDP(item)
                except KeyError:
                    pass
            newSorted = dict(sorted(gdpDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == Countries.getRedirectedNameToAlpha3(alpha3):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGDPRankingDict(cls):
        gdpDict = {}
        for count, item in enumerate(Data.alpha3List):
            try:
                if Countries.getGDP(item) is None:
                    pass
                elif Countries.getGDP(item) == 0:
                    pass
                else:
                    gdpDict[item] = Countries.getGDP(item)
            except KeyError:
                pass
        newSorted = dict(sorted(gdpDict.items(), key=lambda kv: kv[1], reverse=True))
        return newSorted

    @classmethod
    def getGdpPerCapita(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            try:
                return int(Data.alpha3ToGDP[Countries.getRedirectedNameToAlpha3(alpha3)] / Data.alpha3ToPopulation[
                    Countries.getRedirectedNameToAlpha3(alpha3)])
            except ZeroDivisionError:
                return 0
            except TypeError:
                return None

    @classmethod
    def getGdpPerCapitaRanking(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            gdpPerCapitaDict = {}
            for count, item in enumerate(Data.alpha3List):
                try:
                    if Countries.getGdpPerCapita(item) is None:
                        pass
                    elif Countries.getGdpPerCapita(item) == 0:
                        pass
                    else:
                        gdpPerCapitaDict[item] = Countries.getGdpPerCapita(item)
                except KeyError:
                    pass
            newSorted = dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == Countries.getRedirectedNameToAlpha3(alpha3):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGdpPerCapitaRankingDict(cls):
        gdpPerCapitaDict = {}
        for count, item in enumerate(Data.alpha3List):
            try:
                if Countries.getGdpPerCapita(item) is None:
                    pass
                elif Countries.getGdpPerCapita(item) == 0:
                    pass
                else:
                    gdpPerCapitaDict[item] = Countries.getGdpPerCapita(item)
            except KeyError:
                pass
        newSorted = dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))
        return newSorted

    @classmethod
    def getHDI(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToHDI[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getHDIRanking(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            hdiDict = {}
            for count, item in enumerate(Data.alpha3List):
                try:
                    if Countries.getHDI(item) is None:
                        pass
                    elif Countries.getHDI(item) == 0:
                        pass
                    else:
                        hdiDict[item] = Countries.getHDI(item)
                except KeyError:
                    pass
            newSorted = dict(sorted(hdiDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == Countries.getRedirectedNameToAlpha3(alpha3):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getHDIRankingDict(cls):
        hdiDict = {}
        for count, item in enumerate(Data.alpha3List):
            try:
                if Countries.getHDI(item) is None:
                    pass
                elif Countries.getHDI(item) == 0:
                    pass
                else:
                    hdiDict[item] = Countries.getHDI(item)
            except KeyError:
                pass
        newSorted = dict(sorted(hdiDict.items(), key=lambda kv: kv[1], reverse=True))
        return newSorted

    @classmethod
    def getIsAnIsland(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            landlocked = Countries.getIsLandlocked(alpha3)
            borders = Countries.getBorders(alpha3)
            if landlocked is True:
                return False
            else:
                if landlocked is False and not borders:
                    return True
                else:
                    return False

    @classmethod
    def getIsLandlocked(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToLandlocked[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getLargestCity(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToLargestCity[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getLeaders(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            name = Countries.getName(alpha3)
            if alpha3 == "ABW":
                # Aruba
                pass

    @classmethod
    def getName(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToName[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getObesityRate(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToObesityRate[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getObesityRateRanking(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            obesityDict = {}
            for count, item in enumerate(Data.alpha3List):
                try:
                    if Countries.getObesityRate(item) is None:
                        pass
                    elif Countries.getObesityRate(item) == 0:
                        pass
                    else:
                        obesityDict[item] = Countries.getObesityRate(item)
                except KeyError:
                    pass
            newSorted = dict(sorted(obesityDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == Countries.getRedirectedNameToAlpha3(alpha3):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getObesityRateRankingDict(cls):
        obesityDict = {}
        for count, item in enumerate(Data.alpha3List):
            try:
                if Countries.getObesityRate(item) is None:
                    pass
                elif Countries.getObesityRate(item) == 0:
                    pass
                else:
                    obesityDict[item] = Countries.getObesityRate(item)
            except KeyError:
                pass
        newSorted = dict(sorted(obesityDict.items(), key=lambda kv: kv[1], reverse=True))
        return newSorted

    @classmethod
    def getPopulation(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            try:
                return Data.alpha3ToPopulation[Countries.getRedirectedNameToAlpha3(alpha3)]
            except KeyError:
                return None

    @classmethod
    def getPopulationRanking(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            populationDict = {}
            for count, item in enumerate(Data.alpha3List):
                try:
                    if Countries.getPopulation(item) is None:
                        pass
                    elif Countries.getPopulation(item) == 0:
                        pass
                    else:
                        populationDict[item] = Countries.getPopulation(item)
                except KeyError:
                    pass
            newSorted = dict(sorted(populationDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == Countries.getRedirectedNameToAlpha3(alpha3):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationRankingDict(cls):
        return dict(sorted(Data.alpha3ToPopulation.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getPopulationDensityInKM(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            population = Countries.getPopulation(alpha3)
            areaKM = Countries.getAreaInKM(alpha3)
            if population is None:
                return None
            else:
                return float(round(population / areaKM, 2))

    @classmethod
    def getPopulationDensityInMiles(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            population = Countries.getPopulation(alpha3)
            areaMiles = Countries.getAreaInMiles(alpha3)
            return float(round(population / areaMiles, 2))

    @classmethod
    def getPopulationDensityRanking(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            populationDensityDict = {}
            for count, item in enumerate(Data.alpha3List):
                if Countries.getPopulationDensityInKM(item) is None:
                    pass
                else:
                    populationDensityDict[item] = Countries.getPopulationDensityInKM(item)
            newSorted = dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == Countries.getRedirectedNameToAlpha3(alpha3):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationDensityRankingDict(cls):
        populationDensityDict = {}
        for count, item in enumerate(Data.alpha3List):
            if Countries.getPopulationDensityInKM(item) is None:
                pass
            else:
                populationDensityDict[item] = Countries.getPopulationDensityInKM(item)
        return dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getRedirectedNameToAlpha3(cls, name: str):
        if name is None:
            return None
        elif name.upper() in Data.alpha3List:
            return name.upper()
        elif name.upper() in Data.alpha2List:
            return Data.alpha2ToAlpha3[name.upper()]
        elif name.upper().replace(" ", "_") in Data.nameToAlpha3.keys():
            return Data.nameToAlpha3[name.upper().replace(" ", "_")]
        else:
            return None

    @classmethod
    def getRedirectedNameToAlpha2(cls, name: str):
        if name is None:
            return None
        elif name.upper() in Data.alpha3List:
            return Data.alpha3ToAlpha2[name.upper()]
        elif name.upper() in Data.alpha2List:
            return name.upper()
        elif name.title().replace("_", " ") in Data.countryNameList:
            alpha3 = Data.nameToAlpha3[name.upper().replace(" ", "_")]
            return Data.alpha3ToAlpha2[alpha3]
        else:
            return None
