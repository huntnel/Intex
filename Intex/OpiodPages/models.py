from django.db import models
from django.db.models.fields import IntegerField
from django.utils.translation import deactivate
# Create your models here.

class Credential(models.Model) :
    credential = models.CharField(max_length=20, unique=True)
    
    class Meta: 
        db_table = 'OpiodPages_credential'

    def __str__(self) :
        return (self.credential)

class State(models.Model) :
    stateabbrev = models.CharField(max_length=2)
    state = models.CharField(max_length=14, unique=True)
    population = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)

    class Meta: 
        db_table = 'OpiodPages_state'

    def __str__(self) :
        return (self.state + ', Pop: ' + str(self.population) + ' Deaths: ' + str(self.deaths))

class Drug(models.Model) :
    drugid = models.IntegerField(default=0, primary_key=True)
    drugname = models.CharField(max_length=30)
    isopioid = models.CharField(max_length=5)

    class Meta: 
        db_table = 'OpiodPages_drug'

    def __str__(self) :
        return(self.drugname)

class pd_prescriber(models.Model) :
    npi = models.IntegerField(default=0, primary_key=True)
    fname = models.CharField(max_length=11)
    lname = models.CharField(max_length=11)
    gender = models.CharField(max_length=1)
    state = models.ForeignKey("State", null=True, on_delete=models.DO_NOTHING)
    specialty = models.CharField(max_length=62)
    isopioidprescriber = models.BooleanField(default=False)
    totalprescriptions = models.IntegerField(default=0)
    drug = models.ManyToManyField('Drug', through='Triple')

    class Meta: 
        db_table = 'OpiodPages_pd_prescriber'

    def __str__(self) :
        return(self.fname + ' ' + self.lname)

class Prescriber_Credential(models.Model) :
    npi = models.ForeignKey(pd_prescriber, on_delete=models.DO_NOTHING, to_field='npi')
    credid = models.ForeignKey(Credential, on_delete=models.DO_NOTHING)
        
    def __str__(self) :
        return(str(self.npi) + " " + str(self.credid))
    class Meta: 
        db_table = 'OpiodPages_prescriber_credential'

class Triple(models.Model) :
    qty = models.IntegerField(default=0, null=False)
    drug = models.ForeignKey(Drug, on_delete=models.DO_NOTHING)
    pd_prescriber = models.ForeignKey(pd_prescriber, on_delete=models.DO_NOTHING)

    class Meta: 
        db_table = 'OpiodPages_triple'

    def __str__(self) :
        return(str(self.drug) + ", " + str(self.pd_prescriber) + ', Amount: ' + str(self.qty))

