from .db import db

class Post(db.Model):
    __tablename__ = 'posts'


    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    locationId = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=True)
    captionRawData = db.Column(db.Text, nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True), server_default=db.func.now()) #func.sysdate())
    updatedAt = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), server_onupdate=db.func.now())

 
    # Model name is title case and singular
    user = db.relationship('User', foreign_keys=userId)  #owner of the post
    taggedUsers = db.relationship('User', secondary='taggedusers')
    comments = db.relationship('Comment', foreign_keys='Comment.parentPostId')
    images = db.relationship('Image', foreign_keys='Image.postId')
    likingUsers = db.relationship('User', secondary='likedposts')
    userSaves = db.relationship('User', secondary='savedposts')



    # to_dict method to convert a dataframe into a dictionary of series or list like data type depending on orient parameter
    def to_dict(self):       
        return {
            "id": self.id,
            "userId": self.userId,
            "locationId": self.locationId,
            "captionRawData": self.captionRawData,
            "createdAt": self.createdAt,
            "user": self.user.to_dict_no_posts(),   #no posts so if a post has this user, there is no infinite circular references
            "taggedUsers": [user.to_dict_no_posts() for user in self.taggedUsers],
            "comments": [comment.to_dict() for comment in self.comments],
            "images": [image.to_dict() for image in self.images],
            "likingUsers": {user.id:[user.username, user.profilePicUrl] for user in self.likingUsers},
            "userSaves": {user.id:user.id for user in self.userSaves}
        }

    def to_dict_for_self(self):       
        return {
            "id": self.id,
            "userId": self.userId,
            "locationId": self.locationId,
            "captionRawData": self.captionRawData,
            "taggedUsers": [user.to_dict_no_posts() for user in self.taggedUsers],
            "comments": [comment.to_dict() for comment in self.comments],
            "images": [image.to_dict() for image in self.images],
            "likingUsers": {user.id:[user.username, user.profilePicUrl] for user in self.likingUsers},
            "userSaves": {user.id:user.id for user in self.userSaves}
        }