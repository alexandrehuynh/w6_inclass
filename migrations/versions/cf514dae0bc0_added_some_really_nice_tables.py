"""added some really nice tables

Revision ID: cf514dae0bc0
Revises: 2143cf1fd541
Create Date: 2024-02-08 09:42:06.978492

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'cf514dae0bc0'
down_revision = '2143cf1fd541'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("""
    ALTER TABLE customer 
    ALTER COLUMN date_created TYPE TIMESTAMP 
    USING 
    (CASE 
        WHEN date_created IS NOT NULL THEN date_created::TIMESTAMP
        ELSE NULL 
    END)
    """)
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("""
    ALTER TABLE customer 
    ALTER COLUMN date_created TYPE VARCHAR 
    USING 
    (CASE 
        WHEN date_created IS NOT NULL THEN date_created::VARCHAR
        ELSE NULL 
    END)
    """)
    # ### end Alembic commands ###

