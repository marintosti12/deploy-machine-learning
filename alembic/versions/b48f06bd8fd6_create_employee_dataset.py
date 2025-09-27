"""create employee_dataset

Revision ID: b48f06bd8fd6
Revises: 24251a13df00
Create Date: 2025-09-26 17:49:21.505347

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b48f06bd8fd6'
down_revision: Union[str, Sequence[str], None] = '24251a13df00'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "employee_dataset",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("id_employee", sa.Integer, nullable=False, index=True),
        sa.Column("age", sa.Integer),
        sa.Column("genre", sa.String(16)),
        sa.Column("revenu_mensuel", sa.Integer),
        sa.Column("statut_marital", sa.Text),
        sa.Column("departement", sa.Text),
        sa.Column("poste", sa.Text),
        sa.Column("nombre_experiences_precedentes", sa.Integer),
        sa.Column("nombre_heures_travailless", sa.Integer),
        sa.Column("annee_experience_totale", sa.Integer),
        sa.Column("annees_dans_l_entreprise", sa.Integer),
        sa.Column("annees_dans_le_poste_actuel", sa.Integer),
        sa.Column("a_quitte_l_entreprise", sa.Integer),
        sa.Column("nombre_participation_pee", sa.Integer),
        sa.Column("nb_formations_suivies", sa.Integer),
        sa.Column("nombre_employee_sous_responsabilite", sa.Integer),
        sa.Column("code_sondage", sa.Text),
        sa.Column("distance_domicile_travail", sa.Integer),
        sa.Column("niveau_education", sa.Text),
        sa.Column("domaine_etude", sa.Text),
        sa.Column("ayant_enfants", sa.Text),
        sa.Column("frequence_deplacement", sa.Text),
        sa.Column("annees_depuis_la_derniere_promotion", sa.Integer),
        sa.Column("annes_sous_responsable_actuel", sa.Integer),
        sa.Column("satisfaction_employee_environnement", sa.Integer),
        sa.Column("note_evaluation_precedente", sa.Integer),
        sa.Column("niveau_hierarchique_poste", sa.Integer),
        sa.Column("satisfaction_employee_nature_travail", sa.Integer),
        sa.Column("satisfaction_employee_equipe", sa.Integer),
        sa.Column("satisfaction_employee_equilibre_pro_perso", sa.Integer),
        sa.Column("eval_number", sa.Text),
        sa.Column("note_evaluation_actuelle", sa.Integer),
        sa.Column("heure_supplementaires", sa.Text),
        sa.Column("augementation_salaire_precedente", sa.Text),
        sa.Column("source_file", sa.Text, nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("timezone('utc', now())"), nullable=False),
    )


def downgrade() -> None:
    op.drop_index("ix_employee_dataset_code_sondage", table_name="employee_dataset")
    op.drop_index("ix_employee_dataset_eval_number", table_name="employee_dataset")
    op.drop_index("ix_employee_dataset_id_employee", table_name="employee_dataset")
    op.drop_table("employee_dataset")
