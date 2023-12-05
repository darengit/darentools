

import os
import sys
import pandas as pd
from datetime import datetime

base = '/home/centos'


def isKeyDate(s):
    if len(s) != 7:
        return False

    if s[0] not in ['A', 'E', 'S']:
        return False

    if not s[1:6].isnumeric():
        return False

    return True


def convertDate(s,c):
    if s[0] != c:
        return ''

    if not s[1:].isdigit():
        return ''

    s = '20' + s[1:]
    return datetime.strptime(s, '%Y%m%d').date()

def upComing(name, aDate, eDate):
    tDate = date.today()
    if name[:3] == 'AS ' and datetime.now().hour > 11:
        tDate += pd.tseries.offsets.BDay(1)

    if eDate == tDate:
        return 'Today'
    elif aDate == tDate + pd.tseries.offsets.BDay(1):
        return 'Today'
    elif eDate == tDate + pd.tseries.offsets.BDay(1):
        return 'Soon'
    elif aDate == tDate + pd.tseries.offsets.BDay(2):
        return 'Soon'


def genTargetInputData():
    data = {
        "InputSlice(bps)": [0,0],
        "Micro": [108,109],
        "Portfolio": ["FRESVOL","LTM12M1M"],
    }

    return pd.DataFrame(data)

def genHtml(dataDf, fname):
    inputCols = [col for col in dataDf.columns if "Input" in col]
    for inputCol in inputCols:
        dataDf[inputCol] = dataDf[inputCol].apply(lambda val: f'<input type="text" value="{val}" style="text-align:right;">')
    dataDf.columns = dataDf.columns.str.replace('Input','')

    currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    titleHtml = f"Generated on: {currentTime}"


    with open(fname + '.html', "w") as f:
        f.write(titleHtml + dataDf.to_html(escape=False, index=False))
    print("DAREN DEBUG target-input.html written")

def genTargetInput():
    targetInputData = genTargetInputData()
    genHtml(targetInputData, "target-input")

def genTargetInput2():

    tlInfo = {}

    for tlFile in os.listdir(base):
        try:
            if tlFile[0:2] == '~$':
                continue
            
            info = tlFile.split('_')
            if len(info) < 6:
                continue

            micro = info[0]
            if not micro.isdigit():
                continue
            micro = int(micro)

            tlName = ' '.join([ s for s in info[1:-3] if not isKeyDate(s)])

            fileDate = convertDate(info[-2], 'F')
            effDate = convertDate(info[-3], 'E')
            annDate = convertDate(info[-4], 'A')

            source = info[-1].split('.')[0]

            if micro not in tlInfo:
                tlInfo[micro] = {}
            else:
                errors.append('duplicate file for micro {}'.format(micro))
                if fileDate <= tlInfo[micro]['FileDate']:
                    continue

            tlInfo[micro]['TlName'] = tlName
            tlInfo[micro]['Source'] = source
            tlInfo[micro]['FileDate'] = fileDate
            tlInfo[micro]['AnnDate'] = annDate
            tlInfo[micro]['EffDate'] = effDate
            tlInfo[micro]['Upcoming'] = upComing(tlName, annDate, effDate)
        except Exception as e:
            errors.append(str(e) + ' in ' + tlFile)
