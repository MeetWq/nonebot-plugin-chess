"""init_db

Revision ID: b737d3c58568
Revises: 
Create Date: 2023-01-31 19:47:01.796812

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "b737d3c58568"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "nonebot_plugin_boardgame_gamerecord",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("game_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("session_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("start_time", sa.DateTime(), nullable=False),
        sa.Column("update_time", sa.DateTime(), nullable=False),
        sa.Column(
            "player_black_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column(
            "player_black_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column(
            "player_white_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column(
            "player_white_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column("positions", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("is_game_over", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("nonebot_plugin_boardgame_gamerecord")
    # ### end Alembic commands ###
