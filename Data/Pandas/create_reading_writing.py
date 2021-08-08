import pandas as pd


def reading_data_files(filepath: str) ->pd.DataFrame:
    return pd.read_csv(filepath)


if __name__ == '__main__':
    data = {'Yes': [50, 21], 'No': [131, 2]}
    pd_data = pd.DataFrame(data, index=['State A', 'State B'])
    pd_data.to_csv('create_reading_writing_example.csv')
    print(pd_data.index.astype(str))
