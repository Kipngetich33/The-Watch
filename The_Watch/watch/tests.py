from django.test import TestCase
from . models import Neighborhood, User_Profile 

class NeighborTestClass(TestCase):
    '''
    A class that test the Image class model
    '''

    def setUp(self):
        '''
        method that runs at the begginning of each test
        '''
        self.neighborhood = Neighborhood(neighborhood_name = 'Lincon', neighborhood_location ='Nebraska', occupants_count = 1)

    def test_isInstance(self):
        '''
        Checks is an object is an instance 
        '''
        self.assertTrue(isinstance(self.neighborhood,Neighborhood)) 

    def test_create_neighborhood(self):
        '''
        Tests is the save_neighborhood function works
        '''
        self.neighborhood.create_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods)==1)

    def test_delete_neighborhood(self):
        '''
        Test the delete_neighborhood method
        '''
        self.neighborhood.save()
        self.neighborhood2 = Neighborhood(neighborhood_name = 'Rochester', neighborhood_location ='Nebraska', occupants_count = 1)
        self.neighborhood2.save()
        self.neighborhood.delete_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods)==1)

    def test_update_neighborhood(self):
        '''
        Test the update_neighborhood method
        '''
        self.neighborhood.save()
        self.neighborhood.update_neighborhood('Lincon','New York',1)
        self.neighborhood.save()
        updated_neighborhood = Neighborhood.objects.get() 
        self.assertTrue(updated_neighborhood.neighborhood_name == 'Lincon',updated_neighborhood.occupants_count == 1)

    def test_find_neigborhood(self):
        '''
        Test the find_neighborhood method using the neighborhood id 
        '''
        pass

class User_ProfileTestClass(TestCase):
    '''
    A class that test the User_ class model
    '''

    def setUp(self):
        '''
        method that runs at the begginning of each test
        '''
        self.user_profile = User_Profile(name = 'Brandford', id=1, email= 'brandford@rocketmail.com')

    def test_isInstance(self):
        '''
        Test if the creted object is an instance of the User_profile model
        '''
        self.assertTrue(isinstance(self.user_profile,User_Profile))
        









