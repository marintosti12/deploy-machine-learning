"""ml inputs

Revision ID: ecd589af543e
Revises: 99e339b56253
Create Date: 2025-09-15 13:47:50.220857

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = 'ecd589af543e'
down_revision: Union[str, Sequence[str], None] = '99e339b56253'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "ml_inputs",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("NOW()"), nullable=False),

        sa.Column("id_employee", sa.Integer(), nullable=False),
        sa.Column("age", sa.Integer(), nullable=False),

        sa.Column("genre", sa.String(length=20), nullable=False),
        sa.Column("revenu_mensuel", sa.Integer(), nullable=False),
        sa.Column("statut_marital", sa.String(length=50), nullable=False),
        sa.Column("departement", sa.String(length=100), nullable=False),
        sa.Column("poste", sa.String(length=100), nullable=False),

        sa.Column("nombre_experiences_precedentes", sa.Integer(), nullable=False),
        sa.Column("nombre_heures_travailless", sa.Integer(), nullable=False),
        sa.Column("annee_experience_totale", sa.Integer(), nullable=False),
        sa.Column("annees_dans_l_entreprise", sa.Integer(), nullable=False),
        sa.Column("annees_dans_le_poste_actuel", sa.Integer(), nullable=False),

        sa.Column("nombre_participation_pee", sa.Integer(), nullable=False),
        sa.Column("nb_formations_suivies", sa.Integer(), nullable=False),
        sa.Column("nombre_employee_sous_responsabilite", sa.Integer(), nullable=False),

        sa.Column("code_sondage", sa.Integer(), nullable=False),
        sa.Column("distance_domicile_travail", sa.Integer(), nullable=False),
        sa.Column("niveau_education", sa.Integer(), nullable=False),
        sa.Column("domaine_etude", sa.String(length=100), nullable=False),

        sa.Column("ayant_enfants", sa.String(length=10), nullable=False),
        sa.Column("frequence_deplacement", sa.String(length=50), nullable=False),

        sa.Column("annees_depuis_la_derniere_promotion", sa.Integer(), nullable=False),
        sa.Column("annes_sous_responsable_actuel", sa.Integer(), nullable=False),

        sa.Column("satisfaction_employee_environnement", sa.Integer(), nullable=False),
        sa.Column("note_evaluation_precedente", sa.Integer(), nullable=False),
        sa.Column("niveau_hierarchique_poste", sa.Integer(), nullable=False),
        sa.Column("satisfaction_employee_nature_travail", sa.Integer(), nullable=False),
        sa.Column("satisfaction_employee_equipe", sa.Integer(), nullable=False),
        sa.Column("satisfaction_employee_equilibre_pro_perso", sa.Integer(), nullable=False),

        sa.Column("eval_number", sa.String(length=50), nullable=False),
        sa.Column("note_evaluation_actuelle", sa.Integer(), nullable=False),
        sa.Column("heure_supplementaires", sa.String(length=10), nullable=False),
        sa.Column("augementation_salaire_precedente", sa.Integer(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("ml_inputs")

