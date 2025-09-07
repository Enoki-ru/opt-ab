from .base_analyzer import BaseAnalyzer
import pandas as pd
import numpy as np
from scipy import stats as st
from typing import Dict, Union
from scipy.stats import norm
from typing import Union, Literal


class CalculateSampleSize:
    def __init__(self):
        self.MANN_WHITNEY_ARE = 0.955
    # Коэффициент ARE для теста Манна-Уитни относительно t-теста
    

    def get_sample_size(
        self,
        mde: float,
        baseline_conversion: float,
        alpha: float = 0.05,
        power: float = 0.8,
        method: Literal['ttest', 'mann-whitney'] = 'ttest'
    ) -> dict[str, Union[int, float, str]]:
        """Calculates the required sample size for each group in the A/B test.

        Uses manual implementation of the formula for the t-test/z-test and adjustment
        for the Mann-Whitney test.

        Args:
            mde (float): Minimum detectable effect (absolute value).
            baseline_conversion (float): Conversion in the control group.
            alpha (float, optional): The level of significance. By default, 0.05.
            power (float, optional): Test power. Default 0.8.
            method (Literal['ttest', 'mann-whitney'], optional): 
                Calculation method. 'ttest' for t-test approximation, 'mann-whitney'
                for the Mann-Whitney test. The default is 'ttest'.

        Returns:
            dict[str, Union[int, float, str]]: Словарь с результатами расчета.
        """
        # Технически, для долей это Z-тест, но он асимптотически эквивалентен t-тесту
        # при больших выборках. Поэтому название метода 'ttest' оставляем для консистентности.
        if method == 'ttest':
            sample_size_per_group = self.calculate_sample_size_manual(
                mde, baseline_conversion, alpha, power
            )
        elif method == 'mann-whitney':
            ttest_sample_size = self.calculate_sample_size_manual(
                mde, baseline_conversion, alpha, power
            )
            sample_size_per_group = int(np.ceil(ttest_sample_size / self.MANN_WHITNEY_ARE))
        else:
            raise ValueError("Метод не поддерживается. Используйте 'ttest' или 'mann-whitney'.")

        return {
            "method": method,
            "sample_size_per_group": sample_size_per_group,
            "mde": mde,
            "baseline_conversion": baseline_conversion,
            "alpha": alpha,
            "power": power
        }


    @staticmethod
    def calculate_sample_size_manual(
        mde: float,
        baseline_conversion: float,
        alpha: float,
        power: float
    ) -> int:
        """
        Calculates the sample size for comparing two fractions using a formula based on a normal approximation.
        Implementation from scratch.
        """
        # 1. Определяем параметры обеих групп
        p1 = baseline_conversion
        p2 = baseline_conversion * mde

        if not (0 < p1 < 1 and 0 < p2 < 1):
            raise ValueError("Conversions should be in the range (0, 1)")

        # 2. Находим Z оценки
        z_alpha = norm.ppf(1 - alpha / 2)  # Двухсторонний тест
        z_beta = norm.ppf(power)  # power = 1 - beta

        # 3. Расчитываем дисперсии (Биномиальное распределение)
        var1 = p1 * (1 - p1)
        var2 = p2 * (1 - p2)

        numerator = (z_alpha * np.sqrt(2 * var1) + z_beta * np.sqrt(var1 + var2))**2
        # Классическая формула: numerator = (z_alpha + z_beta)**2 * (var1 + var2)
        # Мы используем более точную, которая не предполагает var1=var2
        denominator = mde**2
        sample_size = int(np.ceil(numerator / denominator))

        return sample_size

    



class MeanAnalyzer(BaseAnalyzer):
    """Анализатор для непрерывных метрик (средние) с использованием t-теста."""

    def _check_assumptions(self, control_data: pd.Series, test_data: pd.Series):
        # Реализация специфичного шага
        print("Checking assumptions for T-test (e.g., normality)...")
        # Здесь могла бы быть проверка на нормальность (тест Шапиро-Уилка)
        pass

    def _calculate_stats(self, control_data: pd.Series, test_data: pd.Series) -> Dict[str, float]:
        # Реализация специфичного шага
        print("Calculating T-statistic and p-value...")
        t_stat, p_value = st.ttest_ind(control_data, test_data, equal_var=False) # Welch's t-test
        
        return {
            'p_value': p_value,
            't_statistic': t_stat,
            'control_mean': control_data.mean(),
            'test_mean': test_data.mean()
        }


class ProportionAnalyzer(BaseAnalyzer):
    """Анализатор для бинарных метрик (конверсии) с использованием Z-теста."""

    def _check_assumptions(self, control_data: pd.Series, test_data: pd.Series):
        # У Z-теста для пропорций свои допущения
        print("Checking assumptions for Z-test (e.g., sample size > 30)...")
        if len(control_data) < 30 or len(test_data) < 30:
            print("Warning: Sample size might be too small for Z-test.")
        pass

    def _calculate_stats(self, control_data: pd.Series, test_data: pd.Series) -> Dict[str, float]:
        # Совершенно другая математика, но интерфейс тот же!
        print("Calculating Z-statistic and p-value for proportions...")
        # ... здесь будет математика для Z-теста пропорций
        p_value = 0.123 # Заглушка
        return {'p_value': p_value}
