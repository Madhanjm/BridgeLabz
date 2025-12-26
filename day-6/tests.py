import unittest
from emplopyee import Employee,Manager

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp=Employee(1,"madhan",50000)
        self.mng=Manager(2,"abin",80000)
    
    def test_salary(self):
        self.assertEqual(self.emp.get_sal(),50000)
        
    def test_salary(self):
        self.assertEqual(self.mng.get_sal(),80000)
        
    def test_salary_not_equal(self):
        self.assertNotEqual(self.emp.get_sal(),5000)
        
    def test_bonus(self):
        self.assertTrue(self.emp.cal_bonus()>0)
    
    def test_bonus_fail(self):
        self.assertFalse(self.emp.cal_bonus()<0)
        
    def test_update_salary_returns_none(self):
        result = self.emp.update_salary(55000)
        self.assertIsNone(result)
        
    def test_name_in_string(self):
        self.assertIn("madhan",self.emp_name)
        
    def test_employee_instance(self):
        self.assertIsInstance(self.emp, Employee)
        
    def test_employee_instance(self):
        self.assertIsInstance(self.mng, Manager)

if __name__=="__main__":
    unittest.main()