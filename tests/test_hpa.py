import pytest
from core import desired

def test_up_and_bounds():assert desired(2,120,60)==4 and desired(9,600,60)==10
def test_down_and_floor():assert desired(4,10,60)==2
def test_tolerance():assert desired(3,62,60)==3
@pytest.mark.parametrize('args',[(0,100,60),(2,-1,60),(2,100,0),(2,float('nan'),60),(2.5,100,60)])
def test_bad(args):
 with pytest.raises(ValueError):desired(*args)
