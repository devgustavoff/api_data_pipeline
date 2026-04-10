
def transform(datas):
    datas['temperature'] = (datas['temperature'] - 273.15).round(1)
    datas['collected_at'] = datas['collected_at'].dt.floor(freq='h')
    datas['name'] = datas['name'].str.title()
    return datas