"""
Voting System

Task:
- Implement a simple voting system.
- Store candidates in a dictionary { "candidate_name": vote_count }
- Allow voters (by ID) to vote only once.
- Use *args to register multiple candidates at once.
- Use **kwargs to update candidate details like party, region.


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Candidate as a class.
- Voter as a class with has_voted flag.
- Election as a manager class.
"""

candidates = {}
voters = set()

def register_candidates(*args, **kwargs):
    """
    Register candidates with optional metadata.
    Example:
        register_candidates("Alice", "Bob", Alice_party="Green", Bob_party="Blue")
    """
    for candidate in args:
        if candidate not in candidates:
            candidates[candidate] = {"votes": 0}
    
    # Add optional metadata (e.g., party, age, etc.)
    for key, value in kwargs.items():
        # Expect keys like "Alice_party" → maps to Alice
        name, _, meta_key = key.partition("_")
        if name in candidates:
            candidates[name][meta_key] = value


def cast_vote(voter_id, candidate):
    """
    Cast vote if voter has not voted before.
    Returns:
        "Vote casted for {candidate}" if successful,
        "Already voted!" if voter_id exists,
        "Candidate not found!" if candidate is invalid.
    """
    if voter_id in voters:
        return "Already voted!"
    
    if candidate not in candidates:
        return "Candidate not found!"
    
    candidates[candidate]["votes"] += 1
    voters.add(voter_id)
    return f"Vote casted for {candidate}."


def election_result():
    """
    Return the winner(s) and all candidates with their votes.
    """
    if not candidates:
        return {"winners": [], "candidates": {}}
    
    # Find max votes
    max_votes = max(c["votes"] for c in candidates.values())
    winners = [name for name, c in candidates.items() if c["votes"] == max_votes]
    
    return {"winners": winners, "candidates": candidates}

print("=================Example usage===================")
register_candidates("Alice", "Bob", Alice_party="Green", Bob_party="Blue")
print(candidates)

print(cast_vote("V1", "Alice"))
print(cast_vote("V2", "Bob"))
print(cast_vote("V1", "Bob"))  
print(cast_vote("V3", "Alice"))

print("\nElection Result:")
print(election_result())



