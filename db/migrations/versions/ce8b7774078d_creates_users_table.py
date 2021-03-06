"""creates 'users' table

Revision ID: ce8b7774078d
Revises: 
Create Date: 2017-01-21 21:36:55.838241

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ce8b7774078d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=60), nullable=True),
    sa.Column('secret_key', sa.String(length=32), nullable=True),
    sa.Column('is_confirmed', sa.Boolean(), server_default='0', nullable=False),
    sa.Column('confirmation_token', sa.String(length=64), nullable=True),
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v1()'), nullable=False),
    sa.Column('created_at', sa.BigInteger(), server_default=sa.text('cast(EXTRACT(EPOCH FROM NOW()) as BIGINT)'), nullable=True),
    sa.Column('updated_at', sa.BigInteger(), server_default=sa.text('cast(EXTRACT(EPOCH FROM NOW()) as BIGINT)'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
