# -*- coding: utf-8 -*-
"""
Created on Thu May 29 16:48:17 2025

@author: romai
"""

import heapq

class Job:
    def __init__(self, job_id, priority_level, execution_duration):
        self.job_id = job_id
        self.priority_level = priority_level
        self.execution_duration = execution_duration

    def __lt__(self, other):
        if self.priority_level == other.priority_level:
            return self.execution_duration < other.execution_duration
        return self.priority_level < other.priority_level

    def __repr__(self):
        return f"Job(id={self.job_id}, priority={self.priority_level}, time={self.execution_duration})"

class JobScheduler:
    def __init__(self):
        self.job_queue = []

    def add_job(self, job):
        heapq.heappush(self.job_queue, job)
        print(f"Job '{job.job_id}' added with priority {job.priority_level} and duration {job.execution_duration}.")

    def show_pending_jobs(self):
        print("\nPending jobs (unsorted):")
        if not self.job_queue:
            print("No jobs pending.")
            return
        for job in self.job_queue:
            print(f"- {job}")

    def execute_all_jobs(self):
        if not self.job_queue:
            print("No jobs to execute.")
            return
        print("\nExecuting jobs in priority order:")
        while self.job_queue:
            next_job = heapq.heappop(self.job_queue)
            print(f"Executing {next_job}")

def display_menu():
    print("\nCLOUD JOB SCHEDULER")
    print("1. Add a job")
    print("2. View pending jobs")
    print("3. Execute all jobs")
    print("4. Exit")

def main():
    scheduler = JobScheduler()

    while True:
        display_menu()
        user_choice = input("Choose an option: ")

        if user_choice == "1":
            job_id = input("Enter job ID: ")
            try:
                priority_level = int(input("Enter priority level (lower = higher priority): "))
                execution_duration = int(input("Enter execution duration (in seconds): "))
                job = Job(job_id, priority_level, execution_duration)
                scheduler.add_job(job)
            except ValueError:
                print("Error: Priority and duration must be integers.")
        elif user_choice == "2":
            scheduler.show_pending_jobs()
        elif user_choice == "3":
            scheduler.execute_all_jobs()
        elif user_choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
