from .base_analyzer import BaseAnalyzer
import pandas as pd
import numpy as np
from scipy import stats as st
from typing import Dict

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
