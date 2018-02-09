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
        Method that saves a new neighborhood
        '''
        self.save()

    def delete_neighborhood(self):
        '''
        Method that deletes an exiting neighborhood
        '''
        self.delete() 
    
    def update_neighborhood(self,neighborhood_name,neighborhood_location,occupants_count):
        '''
        Method that updates an exiting neighborhood
        '''
        self.neighborhood_name = neighborhood_name
        self.neighborhood_location = neighborhood_location
        self.occupants_count += occupants_count
        self.save()

    def find_neigborhood(self,id):
            '''
            Mehthod the find_neighborhood method using the neighborhood id 
            '''
            found_neighborhood = Neighborhood.objects.get(id = id)
            return Neighborhood

    


name.
id.
neighborhood id foreign key
email address.

class User_(models.Model):
    '''
    A class that defines the User_ model class
    '''
    name = models.CharField(max_length =30,null=True) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null= True)  
    neighborhood_id = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null= True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name


class Business(models.Model):
    '''
    Class that defines the structure of a business object
    '''
    business_name = models.CharField(max_length =30,null=True) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null= True)  
    neighborhood_id = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null= True)
    business_email = models.EmailField(null=True)

    def __str__(self):
        return self.business_name     
      


 



