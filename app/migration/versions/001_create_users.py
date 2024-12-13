import sqlalchemy as sa
from alembic import op
from passlib.context import CryptContext

# Revisão da migração
revision = '001'
down_revision = None
branch_labels = None
depends_on = None

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str):
    return pwd_context.hash(password)

def upgrade():
    # Criação da tabela de usuários
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, unique=True, index=True),
        sa.Column('role', sa.String),
        sa.Column('hashed_password', sa.String),
    )

    # Inserindo os dois usuários default
    op.execute(
        f"INSERT INTO users (username, role, hashed_password) VALUES "
        f"('user', 'user', '{get_password_hash('L0XuwPOdS5U')}'),"
        f"('admin', 'admin', '{get_password_hash('JKSipm0YH')}')"
    )

def downgrade():
    # Drop da tabela
    op.drop_table('users')
