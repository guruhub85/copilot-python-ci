#Use pytest to the test the app.py file
import pytest

from app import add                 
def test_add():     
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -5) == -10               
    assert add(1.5, 2.5) == 4.0 
    assert add(-1.5, -2.5) == -4.0
    # add main function to test the add function
if __name__ == "__main__":
    result = pytest.main()
    if result == 0:
        print("All tests passed successfully!")
                  

