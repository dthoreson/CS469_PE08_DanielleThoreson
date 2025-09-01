class TreasureHunterClass:
    """Greedy algorithm solution for matching hunters and treasures on a map. 
    
    Each element in the map array is either:
    - 'H' Hunter
    - 'T' Treasure
    
    Rules per assignment:
    - Each hunter can capture at most one treasure
    - A hunter can only capture a treasure within distance k 
    - Goal: maximize the number of treasures captured
    """

    def __init__(self):
        """Here we initialize the TreasureHunterClass
        """
        pass

    
    def hunt_treasure(self, arr, n, k): 
        """Return the maximum number of treasures that can be captured. (int)

        Params:
        arr : list[str] --> The map of length n with elements 'H' Hunter or 'T' Treasure
        n : int --> The length of the map array
        k : int --> Maximum allowed distance between a Hunter and a Treasure


        """
        #TODO: function logic
        # Step 1: Create two lists to store the positions (indexes) of hunters and treasures
        hunters = []
        treasures = []

        #Gather positions of hunters and treasures
        for idx, val in enumerate(arr):
            if val == 'H':
                hunters.append(idx)
            elif val == 'T':
                treasures.append(idx)

        # Step 3: Use two pointers (i for hunters, j for treasures)
        # These let us "walk" through both lists and try to make matches
        i, j = 0, 0
        matches = 0 # This will count successful hunter-treasure pairs
        H, T = len(hunters), len(treasures)

        # Two-pointer greedy approach
        # Step 4: Greedy matching
        # Keep going as long as we have hunters and treasures left to check
        while i < H and j < T:
            if abs(hunters[i] - treasures[j]) <= k:
                #Pair this Hunter and Treasure
                # If the hunter and treasure are close enough, we match them!
                matches += 1 
                # Move to the next hunter and the next treasure
                i += 1
                j += 1
            elif hunters[i] < treasures[j]:
                # If the hunter is too far to the left, move on to the next hunter
                i += 1 
            else:
                # If the treasure is too far to the left, move on to the next treasure
                j += 1

        # Step 5: Return the total matches we found
        return matches