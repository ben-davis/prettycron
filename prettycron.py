class CronSechdule(object):
    def __init__(self, expression):
        try:
            self.minute, self.hour, self.month_day, self.month, self.week_day = list(expression)
        except ValueError as exc:
            exc.message = "Invalid cron expression"
            raise

    def __str__(self):
        
