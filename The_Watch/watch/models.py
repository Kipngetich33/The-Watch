from django.db import models
from django.contrib.auth.models import User

class Neighborhood(models.Model):
    '''
    A class that defines the blueprint of a Neighborhood model
    '''
    neighborhood_name = models.CharField(max_length =30,null=True) 
    neighborhood_location = models.CharField(max_length =30, null =True)
    occupants_count = models.PositiveIntegerField(default=0)
    admin_foreign_key = models.ForeignKey(User, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return self.neighborhood_name

    def create_neighborhood(self):
        '''
        Methods that saves a new neighborhood
        '''
        self.save()

    def delete_neighborhood(self):
        '''
        Methods that deletes an exiting neighborhood
        '''
        self.delete() 
    
    def update_neighborhood(self):
        '''
        Methods that updates an exiting neighborhood
        '''
        self.

 



