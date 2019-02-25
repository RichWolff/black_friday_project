from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from config import db_engine

Base = declarative_base()
engine = create_engine(db_engine)

class User(Base):
     __tablename__ = 'users'

     id = Column('id',Integer, primary_key=True)
     gender = Column('gender',String)
     age = Column('age',String)
     occupation = Column('occupation',Integer)
     city_category = Column('city_category',String)
     years_in_current_city = Column('years_in_current_city',String)
     marital_status = Column('marital_status',Integer)
     transaction = relationship('Transaction')
     
     def __repr__(self):
        return f"<User(id='{self.id}', gender='{self.gender}', age='{self.age}'"# -*- coding: utf-8 -*-

class Product(Base):
     __tablename__ = 'products'

     id = Column(String, primary_key=True)
     product_category_1 = Column('product_category_1',Integer)
     product_category_2 = Column('product_category_2',Integer)
     product_category_3 = Column('product_category_3',Integer)
     transaction = relationship('Transaction')

     def __repr__(self):
        return f"<Product(id='{self.id}', product_category_1='{self.product_category_1}', product_category_2='{self.product_category_2}', product_category_3='{self.product_category_3}'"# -*- coding: utf-8 -*-

class Transaction(Base):
     __tablename__ = 'transactions'

     id = Column('id',Integer, primary_key=True,autoincrement=True)
     user_id = Column('user_id',Integer, ForeignKey('users.id'), nullable=False,)
     product_id = Column('product_id',Integer, ForeignKey('products.id'),nullable=False)
     income = Column('income',Integer,nullable=False)

     def __repr__(self):
        return f"<Transaction(id='{self.id}', user_id='{self.user_id}', product_id='{self.product_id}', income='{self.income}'"# -*- coding: utf-8 -*-

# Add relationship to Product and User table

Base.metadata.create_all(engine)

