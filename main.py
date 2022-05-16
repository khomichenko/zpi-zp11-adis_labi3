import numpy
import scipy.stats
import scipy.stats as stats


class Lab3Extra:
    sample = list

    def __init__(self, count):
        self.sample = numpy.random.random_sample(count)

    def інтервальна_оцінка_мат_сподівання(self, рівень_довіри):
        min = (numpy.mean(self.sample) - numpy.sqrt(numpy.var(self.sample)) * stats.t.ppf(рівень_довіри, (len(self.sample) - 1)) / numpy.sqrt(len(self.sample) - 1))
        max = (numpy.mean(self.sample) + numpy.sqrt(numpy.var(self.sample)) * stats.t.ppf(рівень_довіри, (len(self.sample) - 1)) / numpy.sqrt(len(self.sample) - 1))
        print(f"Інтервал математичного сподівання для рівня довіри {рівень_довіри} (n={len(self.sample)}): \t\t\t"
              f"( {min} , {max} ) \tΔ = {abs(max-min)}")

    def інтервальна_оцінка_середньоквадратичного_відхилення(self, рівень_довіри):
        min = numpy.sqrt((numpy.var(self.sample) * len(self.sample)) / scipy.stats.chi2.ppf((1 + рівень_довіри) / 2, len(self.sample) - 1))
        max = numpy.sqrt((numpy.var(self.sample) * len(self.sample)) / scipy.stats.chi2.ppf((1 - рівень_довіри) / 2, len(self.sample) - 1))
        print(f"Інтервал середньоквадратичного відхилення при рівні довіри {рівень_довіри} (n={len(self.sample)}): \t"
              f"( {min} , {max} ) \tΔ = {abs(max-min)}")


if __name__ == '__main__':
    app = Lab3Extra(80)
    app.інтервальна_оцінка_мат_сподівання(рівень_довіри=0.95)
    app.інтервальна_оцінка_середньоквадратичного_відхилення(рівень_довіри=0.95)

    print("\nЗалежність математичного сподівання від рівня довіри")
    for рівень_довіри in [0.9,0.8,0.7,0.6,0.5]:
        app.інтервальна_оцінка_мат_сподівання(рівень_довіри)
    print("При зменшені рівня довіри інтервал математичного сподівання звужується")

    print("\nЗалежність середньоквадратичного відхилення від рівня довіри")
    for рівень_довіри in [0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2]:
        app.інтервальна_оцінка_середньоквадратичного_відхилення(рівень_довіри)
    print("При зменшені рівня довіри інтервал середньоквадратичного відхилення звужується")

    print("\nЗалежність математичного сподівання від об'єму вибірки")
    for n in [80, 40, 20, 10]:
        appI = Lab3Extra(n)
        appI.інтервальна_оцінка_мат_сподівання(рівень_довіри=0.95)
    print("При зменшені об'єма вибірки інтервал математичного сподівання розширюється")

    print("\nЗалежність середньоквадратичного відхилення від об'єму вибірки")
    for n in [80, 40, 20, 10]:
        appI = Lab3Extra(n)
        appI.інтервальна_оцінка_середньоквадратичного_відхилення(рівень_довіри=0.95)
    print("При зменшені об'єма вибірки інтервал середньоквадратичного відхилення розширюється")

