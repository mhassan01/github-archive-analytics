from crontab import CronTab

cron = CronTab(user='username')
job = cron.new(command='python /Data_Extraction_handler/download_github_data.py')
job.minute.every(60)

cron.write()