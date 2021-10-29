# программа обработки модели
# Sams https://www.samsung.com/ru/support/mobile-devices/where-can-i-see-serial-number-and-production-year-of-my-samsung-tv/
Samsung_triger = ['QE','UE','LE','PS','PE']
Samsung_model_type = [["A",2008,"Orsey"],
                      ["B",2009,"Orsey"],
                      ["C",2010,"Orsey"],
                      ["D",2011,"Orsey"],
                      ["E",2012,"Orsey"],
                      ["F",2013,"Orsey"],
                      ["H",2014,"Orsey"],
                      ["J",2015,"Tizen"],
                      ["K",2016,"Tizen"],
                      ["M",2017,"Tizen"],
                      ["Q",2017,"Tizen"],
                      ["L",2017,"Tizen"],
                      ["N",2018,"Tizen"],
                      ["R",2019,"Tizen"],
                      ["T",2020,"Tizen"]]

# LG https://ru.tab-tv.com/?page_id=2555
LG_triger = ['LG','NANO','QNED','OLED']
LG_model_type_classic = [["K",2018,"Webos"],
                         ["M",2019,"Webos"],
                         ["N",2020,"Webos"],
                         ["P",2021,"Webos"],
                         ["v",2011,"Netcast"],
                         ["W",2012,"Netcast"],
                         ["M",2012,"Netcast"],
                         ["S",2012,"Netcast"],
                         ["N",2013,"Netcast"],
                         ["A",2013,"Netcast"],
                         ["B",2014,"Netcast or Webos"],
                         ["C",2014,"Netcast or Webos"],
                         ["F",2015,"Webos"],
                         ["G",2015,"Webos"],
                         ["H",2016,"Webos"],
                         ["J",2017,"Webos"]]
LG_model_type_oled = [["6",2016,"Webos"],
                      ["7",2017,"Webos"],
                      ["8",2018,"Webos"],
                      ["9",2019,"Webos"],
                      ["X",2020,"Webos"],
                      ["I",2021,"Webos"]]
LG_model_type_nano = [["N",2020,"Webos"],
                      ["P",2021,"Webos"]]

NUM_triger = '0123456789'

def who_is_vendor (a): # определили вендора
    find = None
    for x in range(len(Samsung_triger)): # нашли самс
        if Samsung_triger[x] in a and 'OLED' not in a:
            vendor = 'Samsung'
            print(f'Vendor-{vendor} model-{a}')
            vendor_is_samsung(Samsung_triger[x])
            find = True
    for x in range(len(LG_triger)):      # нашли лыжу
        if LG_triger[x] in a:
            vendor = 'LG'
            print(f'Vendor-{vendor} model-{a}')
            vendor_is_lg(LG_triger[x])
            find = True
    if find is None:                     # исключение
        vendor = 'another'
        print(f'Vendor-{vendor} model-{a}')
    return vendor,a

# For Panasonic
# For Philips
# For Sony



def vendor_is_samsung (a): # маска для samsung - https://www.samsung.com/ru/support/mobile-devices/where-can-i-see-serial-number-and-production-year-of-my-samsung-tv/
    b = SmartTV.find(a)
    mask = SmartTV[b:]
    for x in range(len(Samsung_model_type)):
        if mask[4] == Samsung_model_type[x][0]:
            print(f'Symbol-{Samsung_model_type[x][0]} year- {Samsung_model_type[x][1]} OS- {Samsung_model_type[x][2]}')

def vendor_is_lg (a):  # маска для LG - https://ru.tab-tv.com/?page_id=2555
    find = None
    if a == 'LG':
        for x in range(len(SmartTV)):
            if SmartTV[x] in NUM_triger and SmartTV[x+1] in NUM_triger:
                for e in range(len(LG_model_type_classic)):
                    if SmartTV[x+3] == LG_model_type_classic[e][0]:
                        print(f'Symbol-{LG_model_type_classic[e][0]} year- {LG_model_type_classic[e][1]} OS- {LG_model_type_classic[e][2]}')
                        find = True
                        break
            if find:
                break

    elif a == 'OLED':
        for x in range(len(SmartTV)):
            if SmartTV[x] in NUM_triger and SmartTV[x+1] in NUM_triger:
                for e in range(len(LG_model_type_oled)):
                    if SmartTV[x + 3] == LG_model_type_oled[e][0]:
                        print(f'Symbol-{LG_model_type_oled[e][0]} year- {LG_model_type_oled[e][1]} OS- {LG_model_type_oled[e][2]}')
                        find = True
                        break
            if find:
                break
    else:  # nano and qned
        b = SmartTV.find(a)
        for x in range(len(LG_model_type_nano)):
            if SmartTV[b+7] == LG_model_type_nano[x][0]:
                print(f'Symbol-{LG_model_type_nano[x][0]} year- {LG_model_type_nano[x][1]} OS- {LG_model_type_nano[x][2]}')
                find = True
                break

def vendor_is_Panasonic ():
    print('a')

def vendor_is_Philips ():
    print('a')

def vendor_is_Sony ():
    print('a')

# тело проги
while True:
    SmartTV = str.upper(input('Ведите модель устройства, для выхода введите break :'))
    if SmartTV == 'BREAK':
        break
    who_is_vendor(SmartTV)

