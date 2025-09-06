# Используем модуль abc (Abstract Base Classes)
from abc import ABC, abstractmethod
from typing import Dict, Any
import pandas as pd

class BaseAnalyzer(ABC):
    """
    Абстрактный базовый класс для всех анализаторов результатов.
    Определяет общий интерфейс и скелет алгоритма анализа (Шаблонный метод).
    """

    def run(self, control_data: pd.Series, test_data: pd.Series) -> Dict[str, Any]:
        """
        --- ЭТО ШАБЛОННЫЙ МЕТОД ---
        Он определяет общую последовательность действий для любого анализа.
        """
        print(f"--- Running analysis with {self.__class__.__name__} ---")
        
        # 1. Шаг, который должны реализовать дочерние классы
        self._check_assumptions(control_data, test_data)
        
        # 2. Еще один обязательный шаг для дочерних классов
        stats = self._calculate_stats(control_data, test_data)
        
        # 3. Общий шаг, реализованный прямо здесь
        formatted_results = self._format_results(stats)
        
        return formatted_results

    @abstractmethod
    def _check_assumptions(self, control_data: pd.Series, test_data: pd.Series):
        """
        Абстрактный метод. Каждый анализатор должен реализовать свою логику
        проверки допущений (например, нормальность, гомогенность дисперсий).
        """
        pass

    @abstractmethod
    def _calculate_stats(self, control_data: pd.Series, test_data: pd.Series) -> Dict[str, float]:
        """
        Абстрактный метод. Каждый анализатор должен реализовать свою логику
        расчета статистик (p-value, effect size, confidence intervals и т.д.).
        """
        pass

    def _format_results(self, stats: Dict[str, float]) -> Dict[str, Any]:
        """
        Конкретный метод ("хук"). Предоставляет базовое форматирование.
        Дочерние классы могут его использовать "как есть" или переопределить.
        """
        print("Formatting results...")
        # Добавляем интерпретацию p-value
        if 'p_value' in stats:
            stats['is_significant'] = stats['p_value'] < 0.05
        return stats
