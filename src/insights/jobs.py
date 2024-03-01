import csv
from typing import List, Dict


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, 'r', encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                self.jobs_list.append(dict(row))

        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        unique_job_types = []
        for job in self.jobs_list:
            if (job.get('job_type') and
                    job.get('job_type') not in unique_job_types):
                unique_job_types.append(job['job_type'])
        return unique_job_types

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
