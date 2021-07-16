# Problem Set 4A
# Name: MacGuffin_
# Collaborators:
# Time Spent: 1:13

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]
        # Base Case: if the string's length is 1, its' permutations are itself
        
    else:
        hold = []
        primary = sequence[0]                   # 1st letter in sequence
        perms = get_permutations(sequence[1:])  # Get all permutations of the rest of string (recursive down to len(1))
        for mut in perms:
            for pos in range(len(mut)+1):  
                hold += [mut[:pos] + primary + mut[pos:]]
                # for each position that we can insert the primary, insert it at position 'pos'
        return hold


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    INPUTS = ['abc','bag','yes']
    OUTPUTS = [['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],['bag','abg','agb','gab','gba','bga'],['yes','yse','sey','sye','esy','eys']]
    for i in range(len(INPUTS)):
        print('Input:', INPUTS[i])
        print('Expected Output:', OUTPUTS[i])
        print('Actual Output:', get_permutations(INPUTS[i]))
