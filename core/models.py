from django.db import models

class Activity(models.Model):
    CATEGORY_CHOICES = [
        ('นักศึกษาทุนผู้ยืม', 'นักศึกษาทุนผู้ยืม'),
        ('นักศึกษาทั่วไป', 'นักศึกษาทั่วไป'),
    ]
    TERM_CHOICES = [
        ('1/2567', '1/2567'),
        ('2/2567', '2/2567'),
    ]
    ACTIVITY_TYPE_CHOICES = [
        ('กิจกรรมพัฒนาชุมชน', 'กิจกรรมพัฒนาชุมชน / ศาสนสถานต่างๆ'),
        ('กิจกรรมในคณะ', 'กิจกรรมในคณะ / มหาวิทยาลัย'),
    ]

    student_name = models.CharField(max_length=100, verbose_name="ชื่อนักศึกษา", blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    term = models.CharField(max_length=10, choices=TERM_CHOICES)
    activity_type = models.CharField(max_length=100, choices=ACTIVITY_TYPE_CHOICES)
    description = models.TextField()
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    hours = models.FloatField()
    document = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.description
