# https://www.infobursatil.com/listado-cedears/
lista = [
    { 'type': 'CEDEAR', 'id': 1,   'ticker': 'AAPL',	'ratio': 10,	'nombre': 'Apple Inc.'},
    { 'type': 'CEDEAR', 'id': 2,   'ticker': 'ABEV',	'ratio': 0.33,	'nombre': 'Ambev S.A.'},
    { 'type': 'CEDEAR', 'id': 3,   'ticker': 'ABT',	    'ratio': 2,	    'nombre': 'Abbott Laboratories'},
    { 'type': 'CEDEAR', 'id': 4,   'ticker': 'ADBE',	'ratio': 11,	'nombre': 'Adobe Inc.'},
    { 'type': 'CEDEAR', 'id': 5,   'ticker': 'AGRO',	'ratio': 40,	'nombre': 'Adecoagro S.A.'},
    { 'type': 'CEDEAR', 'id': 6,   'ticker': 'AIG',	    'ratio': 5,	    'nombre': 'American International Group, Inc.'},
    { 'type': 'CEDEAR', 'id': 7,   'ticker': 'AMD',	    'ratio': 0.5,	'nombre': 'Advanced Micro Devices, Inc.'},
    { 'type': 'CEDEAR', 'id': 8,   'ticker': 'AMGN',	'ratio': 5,	    'nombre': 'Amgen Inc.'},
    { 'type': 'CEDEAR', 'id': 9,   'ticker': 'AMX',	    'ratio': 1,	    'nombre': 'América Móvil, S.A.B. de C.V.'},
    { 'type': 'CEDEAR', 'id': 10,  'ticker': 'AMZN',	'ratio': 72,	'nombre': 'Amazon.com, Inc.'},
    { 'type': 'CEDEAR', 'id': 11,  'ticker': 'ARCO',	'ratio': 0.5,	'nombre': 'Arcos Dorados Holdings Inc.'},
    { 'type': 'CEDEAR', 'id': 12,  'ticker': 'AUY',	    'ratio': 1,	    'nombre': 'Yamana Gold Inc.'},
    { 'type': 'CEDEAR', 'id': 13,  'ticker': 'AXP',	    'ratio': 5,	    'nombre': 'American Express Company'},
    { 'type': 'CEDEAR', 'id': 14,  'ticker': 'BA',	    'ratio': 3,	    'nombre': 'The Boeing Company'},
    { 'type': 'CEDEAR', 'id': 15,  'ticker': 'BABA',	'ratio': 9,	    'nombre': 'Alibaba Group Holding Limited'},
    { 'type': 'CEDEAR', 'id': 16,  'ticker': 'BBD',	    'ratio': 1,	    'nombre': 'Banco Bradesco S.A.'},
    { 'type': 'CEDEAR', 'id': 17,  'ticker': 'BCS',	    'ratio': 1,	    'nombre': 'Barclays PLC'},
    { 'type': 'CEDEAR', 'id': 18,  'ticker': 'BHP',	    'ratio': 1,	    'nombre': 'BHP Group'},
    { 'type': 'CEDEAR', 'id': 19,  'ticker': 'BIDU',	'ratio': 11,	'nombre': 'Baidu, Inc.'},
    { 'type': 'CEDEAR', 'id': 20,  'ticker': 'BIIB',	'ratio': 13,	'nombre': 'Biogen Inc.'},
    { 'type': 'CEDEAR', 'id': 21,  'ticker': 'BMY',	    'ratio': 1,	    'nombre': 'Bristol-Myers Squibb Company'},
    { 'type': 'CEDEAR', 'id': 22,  'ticker': 'BP',	    'ratio': 5,	    'nombre': 'BP PLC'},
    { 'type': 'CEDEAR', 'id': 23,  'ticker': 'BRFS',	'ratio': 0.33,	'nombre': 'BRF S.A.'},
    { 'type': 'CEDEAR', 'id': 24,  'ticker': 'BSBR',	'ratio': 1,	    'nombre': 'Banco Santander (Brasil) S.A.'},
    { 'type': 'CEDEAR', 'id': 25,  'ticker': 'C',	    'ratio': 3,	    'nombre': 'Citigroup Inc.'},
    { 'type': 'CEDEAR', 'id': 26,  'ticker': 'CAT',	    'ratio': 5,	    'nombre': 'Caterpillar Inc.'},
    { 'type': 'CEDEAR', 'id': 27,  'ticker': 'CHL',	    'ratio': 3,	    'nombre': 'China Mobile Limited'},
    { 'type': 'CEDEAR', 'id': 28,  'ticker': 'CL',	    'ratio': 3,	    'nombre': 'Colgate-Palmolive Company'},
    { 'type': 'CEDEAR', 'id': 29,  'ticker': 'COST',	'ratio': 4,	    'nombre': 'Costco Wholesale Corporation'},
    { 'type': 'CEDEAR', 'id': 30,  'ticker': 'CRM',	    'ratio': 6,	    'nombre': 'salesforce.com, inc.'},
    { 'type': 'CEDEAR', 'id': 31,  'ticker': 'CS',	    'ratio': 1,	    'nombre': 'Credit Suisse Group AG'},
    { 'type': 'CEDEAR', 'id': 32,  'ticker': 'CSCO',	'ratio': 5,	    'nombre': 'Cisco Systems, Inc.'},
    { 'type': 'CEDEAR', 'id': 33,  'ticker': 'CVX',	    'ratio': 8,	    'nombre': 'Chevron Corporation'},
    { 'type': 'CEDEAR', 'id': 34,  'ticker': 'CX',	    'ratio': 1,	    'nombre': 'CEMEX, S.A.B. de C.V.'},
    { 'type': 'CEDEAR', 'id': 35,  'ticker': 'DD',	    'ratio': 5,	    'nombre': 'DuPont de Nemours, Inc.'},
    { 'type': 'CEDEAR', 'id': 36,  'ticker': 'DE',	    'ratio': 2,	    'nombre': 'Deere & Company'},
    { 'type': 'CEDEAR', 'id': 37,  'ticker': 'DESP',	'ratio': 1,	    'nombre': 'Despegar.com, Corp.'},
    { 'type': 'CEDEAR', 'id': 38,  'ticker': 'DIS',	    'ratio': 4,	    'nombre': 'The Walt Disney Company'},
    { 'type': 'CEDEAR', 'id': 39,  'ticker': 'EBAY',	'ratio': 1,	    'nombre': 'eBay Inc.'},
    { 'type': 'CEDEAR', 'id': 40,  'ticker': 'ERJ',	    'ratio': 1,	    'nombre': 'Embraer S.A.'},
    { 'type': 'CEDEAR', 'id': 41,  'ticker': 'FB',	    'ratio': 8,	    'nombre': 'Facebook, Inc.'},
    { 'type': 'CEDEAR', 'id': 42,  'ticker': 'FCX',	    'ratio': 1,	    'nombre': 'Freeport-McMoRan Inc.'},
    { 'type': 'CEDEAR', 'id': 43,  'ticker': 'FDX',	    'ratio': 2,	    'nombre': 'FedEx Corporation'},
    { 'type': 'CEDEAR', 'id': 44,  'ticker': 'FMX',	    'ratio': 2,	    'nombre': 'Fomento Económico Mexicano, S.A.B. de C.V.'},
    { 'type': 'CEDEAR', 'id': 46,  'ticker': 'GE',	    'ratio': 1,	    'nombre': 'General Electric Company'},
    { 'type': 'CEDEAR', 'id': 47,  'ticker': 'GGB',	    'ratio': 0.25,	'nombre': 'Gerdau S.A.'},
    { 'type': 'CEDEAR', 'id': 48,  'ticker': 'GILD',	'ratio': 4,	    'nombre': 'Gilead Sciences, Inc.'},
    { 'type': 'CEDEAR', 'id': 49,  'ticker': 'GLOB',	'ratio': 2,	    'nombre': 'Globant S.A.'},
    { 'type': 'CEDEAR', 'id': 50,  'ticker': 'GOLD',	'ratio': 1,	    'nombre': 'Barrick Gold Corporation'},
    { 'type': 'CEDEAR', 'id': 51,  'ticker': 'GOOGL',	'ratio': 29,	'nombre': 'Alphabet Inc.'},
    { 'type': 'CEDEAR', 'id': 52,  'ticker': 'GRMN',	'ratio': 3,	    'nombre': 'Garmin Ltd.'},
    { 'type': 'CEDEAR', 'id': 53,  'ticker': 'GS',	    'ratio': 13,	'nombre': 'The Goldman Sachs Group, Inc.'},
    { 'type': 'CEDEAR', 'id': 54,  'ticker': 'GSK',	    'ratio': 4,	    'nombre': 'GlaxoSmithKline plc'},
    { 'type': 'CEDEAR', 'id': 55,  'ticker': 'HD',	    'ratio': 4,	    'nombre': 'The Home Depot, Inc. '},
    { 'type': 'CEDEAR', 'id': 56,  'ticker': 'HMC',	    'ratio': 1,	    'nombre': 'Honda Motor Co., Ltd.'},
    { 'type': 'CEDEAR', 'id': 57,  'ticker': 'HMY',	    'ratio': 1,	    'nombre': 'Harmony Gold Mining Company Limited'},
    { 'type': 'CEDEAR', 'id': 58,  'ticker': 'HNP',	    'ratio': 1,	    'nombre': 'Huaneng Power International, Inc.'},
    { 'type': 'CEDEAR', 'id': 59,  'ticker': 'HPQ',	    'ratio': 1,	    'nombre': 'HP Inc.'},
    { 'type': 'CEDEAR', 'id': 60,  'ticker': 'HSBC',	'ratio': 2,	    'nombre': 'HSBC Holdings plc'},
    { 'type': 'CEDEAR', 'id': 61,  'ticker': 'HWM',	    'ratio': 1,	    'nombre': 'Howmet Aerospace Inc.'},
    { 'type': 'CEDEAR', 'id': 62,  'ticker': 'IBM',	    'ratio': 5,	    'nombre': 'International Business Machines Corporation'},
    { 'type': 'CEDEAR', 'id': 63,  'ticker': 'INFY',	'ratio': 1,	    'nombre': 'Infosys Limited'},
    { 'type': 'CEDEAR', 'id': 64,  'ticker': 'INTC',	'ratio': 5,	    'nombre': 'Intel Corporation'},
    { 'type': 'CEDEAR', 'id': 65,  'ticker': 'ITUB',	'ratio': 1,	    'nombre': 'Itau Unibanco Holding S.A.'},
    { 'type': 'CEDEAR', 'id': 66,  'ticker': 'JD',	    'ratio': 2,	    'nombre': 'JD.com, Inc. '},
    { 'type': 'CEDEAR', 'id': 67,  'ticker': 'JNJ',	    'ratio': 5,	    'nombre': 'Johnson & Johnson'},
    { 'type': 'CEDEAR', 'id': 68,  'ticker': 'JPM',	    'ratio': 5,	    'nombre': 'JPMorgan Chase & Co.'},
    { 'type': 'CEDEAR', 'id': 69,  'ticker': 'KMB',	    'ratio': 3,	    'nombre': 'Kimberly-Clark Corporation'},
    { 'type': 'CEDEAR', 'id': 70,  'ticker': 'KO',	    'ratio': 5,	    'nombre': 'The Coca-Cola Company'},
    { 'type': 'CEDEAR', 'id': 71,  'ticker': 'LMT',	    'ratio': 1,	    'nombre': 'Lockheed Martin Corporation'},
    { 'type': 'CEDEAR', 'id': 72,  'ticker': 'LVS',	    'ratio': 1,	    'nombre': 'Las Vegas Sands Corp.'},
    { 'type': 'CEDEAR', 'id': 73,  'ticker': 'LYG',	    'ratio': 2,	    'nombre': 'Lloyds Banking Group plc'},
    { 'type': 'CEDEAR', 'id': 74,  'ticker': 'MCD',	    'ratio': 4,	    'nombre': 'McDonald\'s Corporation'},
    { 'type': 'CEDEAR', 'id': 75,  'ticker': 'MDT',	    'ratio': 2,	    'nombre': 'Medtronic plc'},
    { 'type': 'CEDEAR', 'id': 76,  'ticker': 'MELI',	'ratio': 2,	    'nombre': 'Mercadolibre, Inc.'},
    { 'type': 'CEDEAR', 'id': 77,  'ticker': 'MMM',	    'ratio': 5,	    'nombre': '3M Company'},
    { 'type': 'CEDEAR', 'id': 78,  'ticker': 'MO',	    'ratio': 4,	    'nombre': 'Altria Group, Inc.'},
    { 'type': 'CEDEAR', 'id': 79,  'ticker': 'MRK',	    'ratio': 5,	    'nombre': 'Merck & Co., Inc.'},
    { 'type': 'CEDEAR', 'id': 80,  'ticker': 'MSFT',	'ratio': 5,	    'nombre': 'Microsoft Corporation'},
    { 'type': 'CEDEAR', 'id': 81,  'ticker': 'MSI',	    'ratio': 5,	    'nombre': 'Motorola Solutions, Inc.'},
    { 'type': 'CEDEAR', 'id': 82,  'ticker': 'NEM',	    'ratio': 1,	    'nombre': 'Newmont Corporation'},
    { 'type': 'CEDEAR', 'id': 83,  'ticker': 'NFLX',	'ratio': 16,	'nombre': 'Netflix, Inc. '},
    { 'type': 'CEDEAR', 'id': 84,  'ticker': 'NGG',	    'ratio': 2,	    'nombre': 'National Grid plc'},
    { 'type': 'CEDEAR', 'id': 85,  'ticker': 'NKE',	    'ratio': 3,	    'nombre': 'Nike, Inc.'},
    { 'type': 'CEDEAR', 'id': 86,  'ticker': 'NOK',	    'ratio': 1,	    'nombre': 'Nokia Corporation'},
    { 'type': 'CEDEAR', 'id': 87,  'ticker': 'NVDA',	'ratio': 12,	'nombre': 'NVIDIA Corporation'},
    { 'type': 'CEDEAR', 'id': 88,  'ticker': 'NVS',	    'ratio': 2,	    'nombre': 'Novartis AG'},
    { 'type': 'CEDEAR', 'id': 89,  'ticker': 'ORCL',	'ratio': 3,	    'nombre': 'Oracle Corporation'},
    { 'type': 'CEDEAR', 'id': 90,  'ticker': 'PBR',	    'ratio': 1,	    'nombre': 'Petróleo Brasileiro S.A. - Petrobras'},
    { 'type': 'CEDEAR', 'id': 91,  'ticker': 'PEP',	    'ratio': 2,	    'nombre': 'PepsiCo, Inc.'},
    { 'type': 'CEDEAR', 'id': 92,  'ticker': 'PFE',	    'ratio': 2,	    'nombre': 'Pfizer Inc.'},
    { 'type': 'CEDEAR', 'id': 93,  'ticker': 'PG',	    'ratio': 5,	    'nombre': 'The Procter & Gamble Company'},
    { 'type': 'CEDEAR', 'id': 94,  'ticker': 'PTR',	    'ratio': 4,	    'nombre': 'PetroChina Company Limited'},
    { 'type': 'CEDEAR', 'id': 95,  'ticker': 'PYPL',	'ratio': 4,	    'nombre': 'PayPal Holdings, Inc.'},
    { 'type': 'CEDEAR', 'id': 96,  'ticker': 'QCOM',	'ratio': 11,	'nombre': 'QUALCOMM Incorporated'},
    { 'type': 'CEDEAR', 'id': 97,  'ticker': 'RIO',	    'ratio': 4,	    'nombre': 'Rio Tinto Group'},
    { 'type': 'CEDEAR', 'id': 98,  'ticker': 'RTX',	    'ratio': 5,	    'nombre': 'Raytheon Technologies Corporation'},
    { 'type': 'CEDEAR', 'id': 99,  'ticker': 'SAN',	    'ratio': 0.25,	'nombre': 'Banco Santander, S.A.'},
    { 'type': 'CEDEAR', 'id': 100, 'ticker': 'SAP',	    'ratio': 3,	    'nombre': 'SAP SE'},
    { 'type': 'CEDEAR', 'id': 101, 'ticker': 'SBS',	    'ratio': 0.5,	'nombre': 'Companhia de Saneamento Básico do Estado de São Paulo'},
    { 'type': 'CEDEAR', 'id': 102, 'ticker': 'SBUX',	'ratio': 1,	    'nombre': 'Starbucks Corporation'},
    { 'type': 'CEDEAR', 'id': 103, 'ticker': 'SID',	    'ratio': 0.125,	'nombre': 'Companhia Siderurgica Nacional'},
    { 'type': 'CEDEAR', 'id': 104, 'ticker': 'SLB',	    'ratio': 3,	    'nombre': 'Schlumberger Limited'},
    { 'type': 'CEDEAR', 'id': 105, 'ticker': 'SNAP',	'ratio': 1,	    'nombre': 'Snap Inc.'},
    { 'type': 'CEDEAR', 'id': 106, 'ticker': 'SNE',	    'ratio': 2,	    'nombre': 'Sony Corporation'},
    { 'type': 'CEDEAR', 'id': 107, 'ticker': 'SNP',	    'ratio': 3,	    'nombre': 'China Petroleum & Chemical Corporation'},
    { 'type': 'CEDEAR', 'id': 108, 'ticker': 'T',	    'ratio': 3,	    'nombre': 'AT&T Inc.'},
    { 'type': 'CEDEAR', 'id': 109, 'ticker': 'TGT',	    'ratio': 4,	    'nombre': 'Target Corporation'},
    { 'type': 'CEDEAR', 'id': 110, 'ticker': 'TM',	    'ratio': 5,	    'nombre': 'Toyota Motor Corporation'},
    { 'type': 'CEDEAR', 'id': 111, 'ticker': 'TOT',	    'ratio': 3,	    'nombre': 'Total SE'},
    { 'type': 'CEDEAR', 'id': 112, 'ticker': 'TRIP',	'ratio': 2,	    'nombre': 'TripAdvisor, Inc.'},
    { 'type': 'CEDEAR', 'id': 113, 'ticker': 'TSLA',	'ratio': 15,	'nombre': 'Tesla, Inc.'},
    { 'type': 'CEDEAR', 'id': 114, 'ticker': 'TSM',	    'ratio': 0.33,	'nombre': 'Taiwan Semiconductor Manufacturing Company Limited'},
    { 'type': 'CEDEAR', 'id': 115, 'ticker': 'TSU',	    'ratio': 1,	    'nombre': 'TIM Participações S.A.'},
    { 'type': 'CEDEAR', 'id': 116, 'ticker': 'TWTR',	'ratio': 1,	    'nombre': 'Twitter, Inc.'},
    { 'type': 'CEDEAR', 'id': 117, 'ticker': 'TXN',	    'ratio': 5,	    'nombre': 'Texas Instruments Incorporated'},
    { 'type': 'CEDEAR', 'id': 118, 'ticker': 'UGP',	    'ratio': 1,	    'nombre': 'Ultrapar Participações S.A.'},
    { 'type': 'CEDEAR', 'id': 119, 'ticker': 'UN',	    'ratio': 3,	    'nombre': 'The Unilever Group'},
    { 'type': 'CEDEAR', 'id': 120, 'ticker': 'V',	    'ratio': 6,	    'nombre': 'Visa Inc.'},
    { 'type': 'CEDEAR', 'id': 121, 'ticker': 'VALE',	'ratio': 2,	    'nombre': 'Vale S.A.'},
    { 'type': 'CEDEAR', 'id': 122, 'ticker': 'VIST',	'ratio': 0.2,	'nombre': 'Vista Oil & Gas, S.A.B. de C.V.'},
    { 'type': 'CEDEAR', 'id': 123, 'ticker': 'VIV',	    'ratio': 1,	    'nombre': 'Telefônica Brasil S.A.'},
    { 'type': 'CEDEAR', 'id': 124, 'ticker': 'VOD',	    'ratio': 1,	    'nombre': 'Vodafone Group Plc'},
    { 'type': 'CEDEAR', 'id': 125, 'ticker': 'VRSN',	'ratio': 6,	    'nombre': 'Verisign, Inc.'},
    { 'type': 'CEDEAR', 'id': 126, 'ticker': 'VZ',	    'ratio': 2,	    'nombre': 'Verizon Communications Inc.'},
    { 'type': 'CEDEAR', 'id': 127, 'ticker': 'WFC',	    'ratio': 5,	    'nombre': 'Wells Fargo & Company'},
    { 'type': 'CEDEAR', 'id': 128, 'ticker': 'WMT',	    'ratio': 3,	    'nombre': 'Walmart Inc.'},
    { 'type': 'CEDEAR', 'id': 129, 'ticker': 'X',	    'ratio': 3,	    'nombre': 'United States Steel Corporation'},
    { 'type': 'CEDEAR', 'id': 130, 'ticker': 'XOM',	    'ratio': 5,	    'nombre': 'Exxon Mobil Corporation'},
    { 'type': 'CEDEAR', 'id': 131, 'ticker': 'YELP',	'ratio': 2,	    'nombre': 'Yelp Inc.'}
]
