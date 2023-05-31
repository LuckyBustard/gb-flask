from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.database import db

from models.article_tag import article_tag_association_table


class Tag(db.Model):
    class Meta:
        type_ = "tag"
        self_view = "tag_detail"
        self_view_kwargs = {"id": "<id>"}
        self_view_many = "tag_list"

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, default="", server_default="")
    articles = relationship("Article", secondary=article_tag_association_table, back_populates="tags")

    def __str__(self):
        return self.name
