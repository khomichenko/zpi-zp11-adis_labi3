import pandas
import matplotlib.pyplot as pyplot
import seaborn

class Lab3Extra:
    filenameA = ""
    filenameB = ""
    frameA = []
    frameB = []
    frame = []

    def __init__(self, filenameA, filenameB):
        self.filenameA = filenameA
        self.filenameB = filenameB
        self.frameA = pandas.read_csv(self.filenameA + '.csv', sep=';').dropna(axis=1, how='all')
        self.frameB = pandas.read_csv(self.filenameB + '.csv', sep=';').dropna(axis=1, how='all')
        self.frame = self.frameA.set_index('id').join(self.frameB.set_index('id'))

    def info(self):
        ## self.frame.info()
        print(f"\n{self.frame.head(5)}")

    def save(self,filename):
        self.frame.to_csv(filename + ".csv", index=False, sep=';')

    def додати_cтовпчик_з_прибутком(self):
        self.frame['Profit'] = self.frame['Total Volume'] * self.frame['AveragePrice']

    def знайти_загальний_прибуток(self):
        return self.frame.groupby('type')['Profit'].sum()

    def найбільш_успішний_рік(self):
        return self.frame.groupby('year')['Profit'].sum().idxmax()

    def графіки_залежності_сер_ціни_від_кількості_упаковок_різних_розмірів(self):
        figure, axis = pyplot.subplots(1,3,figsize=(24,5))
        figure.suptitle('Залежність середньої ціни від кількості упаковок різних розмірів')
        axis[0].set_xlabel('Середня ціна')
        axis[0].set_ylabel('Small Bags')
        axis[0].scatter(self.frame['AveragePrice'],self.frame['Small Bags'])
        axis[1].set_xlabel('Середня ціна')
        axis[1].set_ylabel('Large Bags')
        axis[1].scatter(self.frame['AveragePrice'], self.frame['Large Bags'])
        axis[2].set_xlabel('Середня ціна')
        axis[2].set_ylabel('XLarge Bags')
        axis[2].scatter(self.frame['AveragePrice'], self.frame['XLarge Bags'])
        pyplot.show()
    def графіки_для_аналіза_викидів_продаж(self):
        pyplot.boxplot(self.frame['Total Volume'])
        pyplot.show()
    def діаграма_по_кількості_проданих_авокадо_певних_видів_у_2016(self,sale_data_labels):
        figure, ax = pyplot.subplots(figsize=(6,6))
        ax.axis('equal')
        sale_data = self.frame[self.frame['year'] == 2016][sale_data_labels].sum()
        wedges, texts, autotexts = ax.pie(sale_data,labels=sale_data_labels,autopct='%1.1f%%',startangle=90,textprops=dict(color='w'))
        ax.set_title('Кількість проданих авокадо у 2016 році:')
        ax.legend(wedges,sale_data_labels,title='Вид авокадо',loc='center left',bbox_to_anchor=(1,0,0.5,1))
        pyplot.setp(autotexts,size=14,weight='bold')
        pyplot.show()

    def график_середніх_цін_на_авокадо_по_регіонам(self):
        region_list = list(self.frame.region.unique())
        average_price = []
        for i in region_list:
            x = self.frame[self.frame.region == i]
            region_average = sum(x.AveragePrice) / len(x)
            average_price.append(region_average)
        df1 = pandas.DataFrame({'region_list': region_list,'average_price': average_price})
        new_index = df1.average_price.sort_values(ascending=False).index.values
        sorted_data = df1.reindex(new_index)

        pyplot.figure(figsize=(11,5))
        ax = seaborn.barplot(x=sorted_data.region_list, y=sorted_data.average_price)
        pyplot.xticks(rotation=90)
        pyplot.xlabel('Регіон')
        pyplot.ylabel('Середня ціна за весь час')
        pyplot.title('Середні ціни на авокадо по регіонам')
        pyplot.show()

    def график_середніх_обємів_продаж_авокадо_по_регіонам(self):
        df1 = self.frame[self.frame != 'TotalUS']
        region_list = list(df1.region.unique())
        average_total_volume = []
        for i in region_list:
            x = df1[df1.region == i]
            if len(x)>0:
                average_total_volume.append(sum(x['Total Volume']) / len(x))
            else:
                average_total_volume.append(sum(x['Total Volume']) / 1)
        df3 = pandas.DataFrame({'region_list': region_list,'average_total_volume': average_total_volume})
        new_index = df3.average_total_volume.sort_values(ascending=False).index.values
        sorted_data = df3.reindex(new_index)
        pyplot.figure(figsize=(11, 5))
        ax = seaborn.barplot(x=sorted_data.region_list, y=sorted_data.average_total_volume)
        pyplot.xticks(rotation=90)
        pyplot.xlabel('Регіон')
        pyplot.ylabel('Середній об`ем продажів')
        pyplot.title('Середній об`ем продажів по регіонам за весь час')
        pyplot.show()

if __name__ == '__main__':
    app = Lab3Extra('Data3a', 'Data3b')
    app.save('Data3')

    print(f"{'*'*100}\n1. Об'єднати в один файл.\nДатафрейм {app.filenameA} і {app.filenameB} після об'єднання:\n")
    app.info()

    print(f"{'*' * 100}\n2. Створити стовпчик з прибутком.")
    app.додати_cтовпчик_з_прибутком()
    app.info()

    print(f"{'*' * 100}\n3. Загальний прибуток по органічному та неорганічному авокадо:\n{app.знайти_загальний_прибуток()}")

    print(f"{'*' * 100}\n4. Найбільш успішний рік: {app.найбільш_успішний_рік()}")

    print(f"{'*' * 100}\n5. Побудувати 3 графіки залежностей середньої ціни від кількості упаковок різних розмірів.")
    app.графіки_залежності_сер_ціни_від_кількості_упаковок_різних_розмірів()

    print(f"{'*' * 100}\n6. Чи є викиди в обсягах продаж? Для цього дивимося на діаграму розмаху")
    app.графіки_для_аналіза_викидів_продаж()

    print(f"{'*' * 100}\n7. Побудувати кругову діаграму по кількості проданих авокадо видів 4046, 4225, 4770 у 2016 році.")
    app.діаграма_по_кількості_проданих_авокадо_певних_видів_у_2016(['4046','4225','4770'])

    print(
        f"{'*' * 100}\n8. В якому штаті середня ціна за весь час була мінімальною, а в якому максимальною?\n"
        f"З мінімальною: {app.frame.groupby('region')['AveragePrice'].mean().idxmin()}\n"
        f"З максимальною: {app.frame.groupby('region')['AveragePrice'].mean().idxmax()}")

    print(f"{'*' * 100}\n9. Які регіони схожі по продажам авокадо? Поясніть свою відповідь.\n"
          f"Схожими за продажами є West, California, South Central. Дивись 2 графіки")
    app.график_середніх_цін_на_авокадо_по_регіонам()
    app.график_середніх_обємів_продаж_авокадо_по_регіонам()


