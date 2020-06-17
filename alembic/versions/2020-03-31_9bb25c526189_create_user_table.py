"""create user table

Revision ID: 9bb25c526189
Revises: 
Create Date: 2020-03-31 22:20:44.105232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9bb25c526189"
down_revision = None
branch_labels = None
depends_on = None
uuid_type = sa.dialects.postgresql.UUID


def upgrade():
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
    op.create_table(
        "beer",
        sa.Column(
            "id",
            uuid_type,
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("price", sa.Float, nullable=False),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.Column("image_url", sa.String),
        sa.Column("image_type", sa.String),
        sa.Column("image_width", sa.Integer, server_default="0", nullable=True),
        sa.Column("image_height", sa.Integer, server_default="0", nullable=True),
        sa.Column("created_at", sa.DateTime, server_default=sa.text("now()")),
    )

    op.create_table(
        "wine",
        sa.Column(
            "id",
            uuid_type,
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("price", sa.Float, nullable=False),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.Column("image_url", sa.String),
        sa.Column("image_type", sa.String),
        sa.Column("image_width", sa.Integer, server_default="0", nullable=True),
        sa.Column("image_height", sa.Integer, server_default="0", nullable=True),
        sa.Column("created_at", sa.DateTime, server_default=sa.text("now()")),
    )
    op.create_table(
        "liquor",
        sa.Column(
            "id",
            uuid_type,
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("price", sa.Float, nullable=False),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.Column("image_url", sa.String),
        sa.Column("image_type", sa.String),
        sa.Column("image_width", sa.Integer, server_default="0", nullable=True),
        sa.Column("image_height", sa.Integer, server_default="0", nullable=True),
        sa.Column("created_at", sa.DateTime, server_default=sa.text("now()")),
    )
    op.create_table(
        "shopping_cart",
        sa.Column(
            "id",
            uuid_type,
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("customer_phone_number", sa.String, nullable=False),
        sa.Column("created_at", sa.DateTime, server_default=sa.text("now()")),
    )
    op.create_table(
        "cart_item",
        sa.Column(
            "id",
            uuid_type,
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("product_id", uuid_type, nullable=False),
        sa.Column("shopping_cart_id", uuid_type, nullable=False),
        sa.Column("liquor_type", sa.Integer, nullable=False),
        sa.Column("created_at", sa.DateTime, server_default=sa.text("now()")),
    )


def downgrade():
    op.drop_table("beer")
    op.drop_table("wine")
    op.drop_table("liquor")
    op.drop_table("shopping_cart")
    op.drop_table("cart_item")
