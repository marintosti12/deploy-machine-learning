import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from .base import Base 

class MLInput(Base):
    __tablename__ = "ml_inputs"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                 default=lambda: datetime.now(timezone.utc), nullable=False)

    id_employee: Mapped[int] = mapped_column(Integer, index=True)
    age: Mapped[int] = mapped_column(Integer)

    genre: Mapped[str] = mapped_column(String(20))
    revenu_mensuel: Mapped[int] = mapped_column(Integer)
    statut_marital: Mapped[str] = mapped_column(String(50))
    departement: Mapped[str] = mapped_column(String(100), index=True)
    poste: Mapped[str] = mapped_column(String(100))

    nombre_experiences_precedentes: Mapped[int] = mapped_column(Integer)
    nombre_heures_travailless: Mapped[int] = mapped_column(Integer)
    annee_experience_totale: Mapped[int] = mapped_column(Integer)
    annees_dans_l_entreprise: Mapped[int] = mapped_column(Integer)
    annees_dans_le_poste_actuel: Mapped[int] = mapped_column(Integer)

    nombre_participation_pee: Mapped[int] = mapped_column(Integer)
    nb_formations_suivies: Mapped[int] = mapped_column(Integer)
    nombre_employee_sous_responsabilite: Mapped[int] = mapped_column(Integer)

    code_sondage: Mapped[int] = mapped_column(Integer)
    distance_domicile_travail: Mapped[int] = mapped_column(Integer)
    niveau_education: Mapped[int] = mapped_column(Integer)
    domaine_etude: Mapped[str] = mapped_column(String(100))

    ayant_enfants: Mapped[str] = mapped_column(String(10))
    frequence_deplacement: Mapped[str] = mapped_column(String(50))

    annees_depuis_la_derniere_promotion: Mapped[int] = mapped_column(Integer)
    annes_sous_responsable_actuel: Mapped[int] = mapped_column(Integer)  
    satisfaction_employee_environnement: Mapped[int] = mapped_column(Integer)
    note_evaluation_precedente: Mapped[int] = mapped_column(Integer)
    niveau_hierarchique_poste: Mapped[int] = mapped_column(Integer)
    satisfaction_employee_nature_travail: Mapped[int] = mapped_column(Integer)
    satisfaction_employee_equipe: Mapped[int] = mapped_column(Integer)
    satisfaction_employee_equilibre_pro_perso: Mapped[int] = mapped_column(Integer)

    eval_number: Mapped[str] = mapped_column(String(50))
    note_evaluation_actuelle: Mapped[int] = mapped_column(Integer)
    heure_supplementaires: Mapped[str] = mapped_column(String(10))  
    augementation_salaire_precedente: Mapped[int] = mapped_column(Integer)  
