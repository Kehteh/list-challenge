def is_prime(some_number: int): # A bit trickier!
    """This function tests to see if the input is a prime number.
    Whenever a prime number is divided by an integer larger than 1 and smaller
    than itself, the result includes a remainder.

    NOTE: The lowest prime number is 2. 1 and 0 are not prime.
    
    Arguments:
        - some_number: an integer to be tested for prime-ness

    Returns:
        - a boolean representing whether or not some_number is prime
    """

    if some_number <2:
        return False
    
    for num in range(2, some_number):
    # check some_number is divisible by num
    # Hint int(1.5) == 1.0
        if some_number / num ==int(some_number / num):
            return False
    return True
