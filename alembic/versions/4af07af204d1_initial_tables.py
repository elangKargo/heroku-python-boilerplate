"""initial tables

Revision ID: 4af07af204d1
Revises: 
Create Date: 2017-05-14 00:10:09.512356

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4af07af204d1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('endpoint_log',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('start_utc', postgresql.TIMESTAMP(), nullable=False),
    sa.Column('duration_ms', sa.INTEGER(), nullable=False),
    sa.Column('endpoint', sa.TEXT(), nullable=True),
    sa.Column('username', sa.TEXT(), nullable=True),
    sa.Column('method', sa.TEXT(), nullable=True),
    sa.Column('http_code', sa.TEXT(), nullable=True),
    sa.Column('error_message', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('session_token',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.TEXT(), nullable=True),
    sa.Column('token', sa.TEXT(), nullable=True),
    sa.Column('created_utc', postgresql.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('system_log',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('event_utc', postgresql.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('level', sa.TEXT(), nullable=True),
    sa.Column('message', sa.TEXT(), nullable=True),
    sa.Column('source', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_account',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.TEXT(), nullable=True),
    sa.Column('email', sa.TEXT(), nullable=True),
    sa.Column('secret', sa.TEXT(), nullable=True),
    sa.Column('creation_utc', postgresql.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('last_updated_utc', postgresql.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_account')
    op.drop_table('system_log')
    op.drop_table('session_token')
    op.drop_table('endpoint_log')
    # ### end Alembic commands ###
