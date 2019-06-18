from django.db import models

# Create your models here.

class BidInfo(models.Model):
    pactissueNo = models.CharField(max_length=32)
    bidCash = models.IntegerField()
    termMonth = models.IntegerField()
    businessRate = models.CharField(max_length=64)
    issueTime = models.DateTimeField()
    xyLevel = models.CharField(max_length=8)
    surplusMoney = models.CharField(max_length=32)
    applyAmt = models.CharField(max_length=32)
    bidPeopleNum = models.IntegerField()
    returnMethod = models.CharField(max_length=32)
    balance = models.CharField(max_length=32)
    closedDay = models.CharField(max_length=32)
    bidState = models.CharField(max_length=32)
    bidAmt = models.CharField(max_length=32)
    bidProgress = models.CharField(max_length=32)
    applyTitle = models.CharField(max_length=32)

    def __str__(self):
        return self.pactissueNo
