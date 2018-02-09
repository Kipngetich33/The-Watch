from django.test import TestCase
from . models import Neighborhood

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
        self.neighborhood.save_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods)==1)

    def test_delete_neighborhood(self):
        '''
        Test the delete_neighborhood methods
        '''
        self.neighborhood.save_neighborhood()
        self.neighborhood2 = Neighborhood(neighborhood_name = 'Rochester', neighborhood_location ='Nebraska', occupants_count = 1)
        self.neighborhood2.save()
        self.neighborhood.delete_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods)==1)


