"""empty message

Revision ID: b0906eab345e
Revises: 
Create Date: 2021-01-25 22:01:38.864863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0906eab345e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hashtags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tagInfo', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.Text(), nullable=False),
    sa.Column('state', sa.Text(), nullable=False),
    sa.Column('country', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('websiteUrl', sa.Text(), nullable=False),
    sa.Column('profilePicUrl', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('directmessages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('senderId', sa.Integer(), nullable=False),
    sa.Column('receiverId', sa.Integer(), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('viewStatus', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['receiverId'], ['users.id'], ),
    sa.ForeignKeyConstraint(['senderId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('locationId', sa.Integer(), nullable=False),
    sa.Column('captionRawData', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['locationId'], ['locations.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('userfollowers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('followerId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['followerId'], ['users.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parentPostId', sa.Integer(), nullable=False),
    sa.Column('captionRawData', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['parentPostId'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hashtagposts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('postId', sa.Integer(), nullable=False),
    sa.Column('hashtagId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['hashtagId'], ['hashtags.id'], ),
    sa.ForeignKeyConstraint(['postId'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('postId', sa.Integer(), nullable=False),
    sa.Column('imgUrl', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['postId'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('likedposts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('postId', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['postId'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('taggedusers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('postId', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('viewStatus', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['postId'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('commentlikes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('commentId', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['commentId'], ['comments.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('commenttaggedusers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('commentId', sa.Integer(), nullable=False),
    sa.Column('viewStatus', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['commentId'], ['comments.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('commenttaggedusers')
    op.drop_table('commentlikes')
    op.drop_table('taggedusers')
    op.drop_table('likedposts')
    op.drop_table('images')
    op.drop_table('hashtagposts')
    op.drop_table('comments')
    op.drop_table('userfollowers')
    op.drop_table('posts')
    op.drop_table('directmessages')
    op.drop_table('users')
    op.drop_table('locations')
    op.drop_table('hashtags')
    # ### end Alembic commands ###