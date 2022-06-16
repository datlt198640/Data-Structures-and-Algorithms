import ctypes


class DynamicArray(object):

    def __init__(self):
        self.n = 0  # Count actual elements (Default is 0)
        self.capacity = 1  # Default Capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            # Check it k index is in bounds of array
            return IndexError('K is out of bounds!')

        return self.A[k]  # Retrieve from array at index k

    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity)  # Double capacity if not enough room

        self.A[self.n] = ele  # Set self.n index to element
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap)  # New bigger array

        for k in range(self.n):  # Reference all existing values
            B[k] = self.A[k]

        self.A = B  # Call A the new bigger array
        self.capacity = new_cap  # Reset the capacity

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()
