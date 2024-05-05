from sqlalchemy import Column, Date, String, func


class CreatedBase(object):
    created_at = Column(Date(), name="created_at", server_default=func.now())
    created_by = Column(String(255), name="created_by", nullable=True)


class EditedBase(object):
    edited_at = Column(Date(), name="edited_at")
    edited_by = Column(String(255), name="edited_by", nullable=True)


class DeletedBase(object):
    deleted_at = Column(Date(), name="deleted_at")
    deleted_by = Column(String(255), name="deleted_by", nullable=True)
