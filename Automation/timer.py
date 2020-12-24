from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from automate import sending_message

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(sending_message, 'interval', seconds=1)

sched.start()