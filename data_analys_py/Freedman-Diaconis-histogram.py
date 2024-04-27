import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_histograms(dataframe, column, condition_column, condition_values, binning_method='friedman',
                    remove_outliers=False):
    fig, ax = plt.subplots(figsize=(8, 6))

    for condition_value in condition_values:
        df_filtered = dataframe[dataframe[condition_column] == condition_value]
        df = df_filtered[[column]].dropna()

        # Избавляемся от выбросов
        if remove_outliers:
            q_low = df[column].quantile(0.01)
            q_high = df[column].quantile(0.99)
            df = df[(df[column] > q_low) & (df[column] < q_high)]

        # Прологарифмируем значения
        df[column] = np.log(df[column])

        # Строим гистограмму
        bins = calculate_bins(df[column], method=binning_method)
        ax.hist(df[column], bins=bins, alpha=0.5, label=f'{condition_column} = {condition_value}')

        # Расчет и вывод медианы
        median_value = np.exp(df[column].median())  # Преобразуем обратно после логарифмирования
        ax.axvline(x=np.log(median_value), linestyle='--',  # Прологарифмируем медиану
                   label=f'Median ({condition_column} = {condition_value}): {median_value:}')

    # Настройки графика
    ax.set_title(f'Histogram of {column} for {condition_column} values')
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')
    ax.legend()
    plt.show()


def calculate_bins(column, method='friedman'):
    if method == 'friedman':
        iqr = np.percentile(column, 75) - np.percentile(column, 25)
        bin_width = 2 * iqr / (len(column) ** (1 / 3))
    elif method == 'sqrt':
        bin_width = int(len(data) ** 0.5)
    else:
        raise ValueError("Invalid binning method. Use 'friedman' or 'sqrt'.")

    num_bins = int((max(column) - min(column)) / bin_width)
    return num_bins

# Загрузка данных из файла
data = pd.read_csv('')

# Построение гистограммы для log(min_distance) при 0
plot_histograms(data, 'min_distance', 'place', [0, 1], binning_method='friedman', remove_outliers=True)
