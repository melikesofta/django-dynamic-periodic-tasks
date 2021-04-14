import json

from django.db import models
from django.utils import timezone
from django_enum_choices.fields import EnumChoiceField
from django_celery_beat.models import IntervalSchedule, PeriodicTask


from .enums import TimeInterval, SetupStatus


class Setup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setups'

    title = models.CharField(max_length=70, blank=False)
    status = EnumChoiceField(SetupStatus, default=SetupStatus.active)
    created_at = models.DateTimeField(auto_now_add=True)
    time_interval = EnumChoiceField(
        TimeInterval, default=TimeInterval.five_mins)

    task = models.OneToOneField(
        PeriodicTask,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def delete(self, *args, **kwargs):
        if self.task is not None:
            self.task.delete()

        return super(self.__class__, self).delete(*args, **kwargs)

    def setup_task(self):
        self.task = PeriodicTask.objects.create(
            name=self.title,
            task='computation_heavy_task',
            interval=self.interval_schedule,
            args=json.dumps([self.id]),
            start_time=timezone.now()
        )
        self.save()

    @property
    def interval_schedule(self):
        if self.time_interval == TimeInterval.one_min:
            return IntervalSchedule.objects.get_or_create(every=10, period=IntervalSchedule.SECONDS)[0]
        if self.time_interval == TimeInterval.five_mins:
            return IntervalSchedule.objects.get_or_create(every=5, period=IntervalSchedule.MINUTES)[0]
        if self.time_interval == TimeInterval.one_hour:
            return IntervalSchedule.objects.get_or_create(every=1, period=IntervalSchedule.HOURS)[0]

        raise NotImplementedError(
            '''Interval Schedule for {interval} is not added.'''.format(
                interval=self.time_interval.value))
