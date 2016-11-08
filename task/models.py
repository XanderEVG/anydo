from django.db import models
from django.utils import timezone

class Task(models.Model):
	#Константы
    NEW = 'NEW'
    WORK = 'WRK'
    WAIT = 'WIT'
    DONE = 'DON'
    CANCELED = 'CLD'
    STATUSES_CHOICES = (
        (NEW, 'Новая'),
        (WORK, 'В работе'),
        (WAIT, 'Ожидание'),
        (DONE, 'Завершено'),
		(CANCELED, 'Отменено'),
    )
	
    NOREPEAT = 'NOR'
    DAY = 'DAY'
    WEEK = 'WEK'
    MONTH = 'MON'
    YEAR = 'YER'
    REPEATTYPE_CHOICES = (
        (NOREPEAT, 'Не повторять'),
		(DAY, 'Ежедневно'),
        (WEEK, 'Еженедельно'),
        (MONTH, 'Ежемесячно'),
        (YEAR, 'Ежегодно'),
    )
    
    #поля
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    status = models.CharField(max_length=3, choices=STATUSES_CHOICES, default=NEW)
	
    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='author', related_name="author")
    performer = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='performer', related_name="performer")
    
    sort_position = models.IntegerField(default=999)
    priority = models.IntegerField(default=0)
    important = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    planned_date = models.DateTimeField(blank=True, null=True)
    exec_date = models.DateTimeField(blank=True, null=True)
    icon = models.ForeignKey('icon', blank=True, null=True)
    object = models.ForeignKey('object', blank=True, null=True)		
    category = models.ForeignKey('category', blank=True, null=True)
    tags = models.ManyToManyField('tag', blank=True)	
    remind = models.DateTimeField(blank=True, null=True)		
    read_permission = models.ManyToManyField('auth.User', blank=True, verbose_name='read_permission', related_name="read_permission")	
    write_permission = models.ManyToManyField('auth.User', blank=True, verbose_name='write_permission', related_name="write_permission")		
    repeat_notification = models.CharField(max_length=3, choices=REPEATTYPE_CHOICES, default=NOREPEAT)						  
    repeat_task = models.CharField(max_length=3, choices=REPEATTYPE_CHOICES, default=NOREPEAT)	
    repeat_task_date = models.DateTimeField(blank=True, null=True)
    notification_task_date = models.DateTimeField(blank=True, null=True)
    
    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        # your code here

    def execute(self):
        #self.exec_date = timezone.now()
        #self.save()
        pass

    def __str__(self):
        return self.title
        

        
        
        
        
        
        
        


	
class object(models.Model):
    pass
	
class category(models.Model):
    pass
	
class tag(models.Model):
    pass
    
class icon(models.Model):
    pass