from .db import db

class HashtagPost(db.Model):
    __tablename__ = 'hashtagposts'


    id = db.Column(db.Integer, primary_key=True)
    postId = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    hashtagId = db.Column(db.Integer, db.ForeignKey('hashtags.id'), nullable=False)


    # to_dict method to convert a dataframe into a dictionary of series or list like data type depending on orient parameter
    def to_dict(self):
        return {
          "id": self.id,
          "postId": self.postId,
          "hashtagId": self.hashtagId,        
        }
        
