from alembic import op
import sqlalchemy as sa
revision="0001_initial"; down_revision=None; branch_labels=None; depends_on=None
def upgrade():
    op.create_table("users",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("email",sa.String(255),nullable=False,unique=True),sa.Column("password_hash",sa.String(255),nullable=False))
    op.create_table("symbols",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("ticker",sa.String(32),nullable=False,unique=True),sa.Column("name",sa.String(255),nullable=False),sa.Column("market",sa.String(64),nullable=False))
    op.create_table("candles",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("symbol",sa.String(32),nullable=False),sa.Column("timeframe",sa.String(16),nullable=False),sa.Column("ts",sa.DateTime(),nullable=False),sa.Column("open",sa.Numeric(),nullable=False),sa.Column("high",sa.Numeric(),nullable=False),sa.Column("low",sa.Numeric(),nullable=False),sa.Column("close",sa.Numeric(),nullable=False),sa.Column("volume",sa.BigInteger(),nullable=False))
    op.create_index("ix_candles_symbol","candles",["symbol"]); op.create_index("ix_candles_ts","candles",["ts"])
    op.create_table("trades",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("symbol",sa.String(32),nullable=False),sa.Column("ts",sa.DateTime(),nullable=False),sa.Column("price",sa.Numeric(),nullable=False),sa.Column("volume",sa.BigInteger(),nullable=False),sa.Column("side",sa.String(8),nullable=False))
    op.create_table("orderbook",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("symbol",sa.String(32),nullable=False),sa.Column("ts",sa.DateTime(),nullable=False),sa.Column("bid_price",sa.Numeric(),nullable=False),sa.Column("bid_volume",sa.BigInteger(),nullable=False),sa.Column("ask_price",sa.Numeric(),nullable=False),sa.Column("ask_volume",sa.BigInteger(),nullable=False))
    op.create_table("open_interest",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("symbol",sa.String(32),nullable=False),sa.Column("ts",sa.DateTime(),nullable=False),sa.Column("value",sa.BigInteger(),nullable=False))
    op.create_table("alerts",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("user_id",sa.Integer(),nullable=False),sa.Column("symbol",sa.String(32),nullable=False),sa.Column("condition",sa.JSON(),nullable=False),sa.Column("active",sa.Boolean(),nullable=False))
    op.create_table("workspaces",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("user_id",sa.Integer(),nullable=False),sa.Column("name",sa.String(120),nullable=False),sa.Column("layout",sa.JSON(),nullable=False))
def downgrade():
    for t in ["workspaces","alerts","open_interest","orderbook","trades","candles","symbols","users"]: op.drop_table(t)
