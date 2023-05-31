from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self
