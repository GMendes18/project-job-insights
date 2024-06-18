from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = 0
        for job in self.jobs_list:
            try:
                salary = int(job.get('max_salary'))
                max_salary = max(max_salary, salary)
            except (ValueError, TypeError):
                pass
        return max_salary

    def get_min_salary(self) -> int:
        min_salary = float('inf')
        for job in self.jobs_list:
            try:
                salary = int(job.get('min_salary'))
                min_salary = min(min_salary, salary)
            except (ValueError, TypeError):
                pass
        return min_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if 'min_salary' not in job or 'max_salary' not in job:
            raise ValueError
        try:
            min_salary = int(job['min_salary'])
            max_salary = int(job['max_salary'])
            if min_salary > max_salary:
                raise ValueError
            salary = int(salary)
            return min_salary <= salary <= max_salary
        except (ValueError, TypeError, KeyError):
            raise ValueError

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
