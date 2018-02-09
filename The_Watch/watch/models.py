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

class User_Profile(models.Model):
    '''
    A class that defines the User_ model class
    '''
    name = models.CharField(max_length =30,null=True) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null= True)  
    neighborhood_id = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null= True)
    email = models.EmailField(null=True)

    def save_user_profiel(self):
        self.save()

    def delete_user_profile(self):
        self.delete()

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

    def create_business(self):
        '''
        Method that saves a new business object to the database
        '''
        self.save()

    def delete_business(self):
        '''
        Method that delete the an exiting business object to the database
        '''
        self.delete()

    def update_business(self,business_name,business_email):
        '''
        Method that updates an exiting business
        '''
        self.business_name = business_name
        self.business_email = business_email
        self.save() 

    @classmethod
    def find_business(cls,business_id):
            '''
            Method the find a business using the business name
            '''
            found_business = cls.object.get(id= business_id)
            return found_business 

    @classmethod
    def search_business(cls,business_name):
        '''
        Method that searches for a business using the business name
        '''
        searched_businesses = cls.objects.filter(business_name__icontains = business_name)
        return searched_businesses
    


      


 



