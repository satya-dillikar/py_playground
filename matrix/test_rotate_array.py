import rotate_array

def areSame(A,B):
   nrow = len(A)
   ncol = len(A[0])
   for i in range(nrow):
      for j in range(ncol):
         if (A[i][j] != B[i][j]):
            return False
   return True

def test_example1():
    '''Verify the output of `rotate90` function'''
    a = [[1,2,3], [4,5,6], [7,8,9]]
    expected_output = [[7,4,1], [8,5,2], [9,6,3]]
    output = rotate_array.rotate90(a)
    assert areSame(output,expected_output) == True 

def test_example2():
    '''Verify the output of `rotate90` function'''
    a = [[1,2,3], [4,5,6]]
    expected_output = [[4,1], [5,2], [6,3]]
    output = rotate_array.rotate90(a)
    assert areSame(output,expected_output) == True     