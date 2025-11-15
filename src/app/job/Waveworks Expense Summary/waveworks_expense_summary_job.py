from models import extract, extract_db, transform, load

def main():
    #data = extract(folder_path='data/waveworks_db/daily_expenses')
    data = extract_db(path='data/waveworks_db/wave_daily.db', table='daily_expenses')
    tdf = transform(data)
    load(tdf)

if __name__ == '__main__':
    main()
