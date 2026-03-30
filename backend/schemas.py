from pydantic import BaseModel, conint, constr

# Model for validating user information
class User(BaseModel):
    id: int
    username: constr(min_length=3, max_length=50)
    email: constr(regex=r'^[^@\s]+@[^@\s]+\.[^@\s]+$')

# Model for validating transaction details
class Transaction(BaseModel):
    transaction_id: int
    amount: conint(gt=0)
    from_user: User
    to_user: User

# Model for validating block information in the blockchain
class Block(BaseModel):
    index: int
    transactions: list[Transaction]
    timestamp: str  # preferably datetime
    previous_hash: str
