from flask_login import current_user
from . import db
from .models import Inschrijvingen, Talen, Lessen


def get_current_cursus():
    if current_user.is_authenticated:
        results = (
            db.session.query(Inschrijvingen, Talen, Lessen)
            .filter(Inschrijvingen.userID == current_user.id)
            .join(Lessen, Inschrijvingen.lessenID == Lessen.lesID)
            .join(Talen, Lessen.talenID == Talen.id)
            .all()
        )
        lessen_dict = {}
        for inschrijvingen, talen, lessen in results:
            lessen_dict[f'{talen.name}_{lessen.lesID}'] = talen.name
        return lessen_dict

