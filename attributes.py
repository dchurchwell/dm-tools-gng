
class Attribute:
    def __init__(self, value=None):
        self.value = value
    
    def set_val(self, value):
        self.value = value

    def __call__(self):
        """Allows the attribute to be called to get its value
        
        Returns:
            Value (normally int) -- The value of this attribute
        """        
        if self.value == None:
            return None
        return self.value

class AbilityScore:
    def __init__(self, value=None):
        self.value = value

    def set_val(self, value=None):
        self.value = value

        # Calculate modifier from score
        if value != None:
            self.score = value
            self.mod = self.score // 2 - 5

    def __call__(self):
        """Allows the ability to be called to get its value
        
        Returns:
            Value (normally int) -- The value of this attribute
        """        
        # Return modifier by default instead of score
        if self.value == None:
            return None
        return self.mod