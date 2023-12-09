from typing import List

class Score:
    def __init__(self, subject : str, score : int):
        self.subject = subject
        self.score = score


class ScoreCard:
    def __init__(self, scores : List[Score]) :
        self.scores = scores
    
    def add_score(self, score : Score):
        self.scores.append(score)
        return score

    def get_score(self, id):
        return self.scores[id-1]
    
    def delete_score(self, id):
        self.scores[id-1] = None #type:ignore
    
    def update_score(self, id, score):
        self.scores[id-1].score = score
        return self.scores[id-1]