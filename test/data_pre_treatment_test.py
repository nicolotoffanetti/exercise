from src.data_pre_treatment import dataNormalizer
import unittest

class TestPretreatment(unittest.TestCase):
    def setUp(self):
        print('Set up test..')
        self.dataset  = ['x','y','z','z','y','x']
        self.names = ['r', 'g', 't']
        self.nromalizer = dataNormalizer(self.dataset, self.names)

    def test_collect_labels_lenght(self):
        # test that  I am able to collect all different labels in a set
        # with the correct lenght
        aCollectedLabels = self.nromalizer.collectLabels(self.dataset)
        self.assertEqual(len(aCollectedLabels), 3)

    def test_correct_elements_are_retrieved(self):
        # test the correct elements are retrieved from the dataset,
        # given the dataset the result should be ['x','y','z']
        aCollectedLabels = self.nromalizer.collectLabels(self.dataset)
        self.assertEqual(aCollectedLabels, ['x','y','z'])
