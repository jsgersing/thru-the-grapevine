from typing import List, Optional, Any

from pydantic import BaseModel, constr, EmailStr, Extra


class GrapeBuyer(BaseModel):
    profile_id: constr(max_length=255)
    first_name: constr(max_length=255)
    last_name: constr(max_length=255)
    winery: constr(max_length=255)
    email: EmailStr
    state: constr(max_length=255)
    grapes_seeking: List[constr(max_length=255)]
    volume_seeking: List[Any]

    class Config:
        extra = Extra.forbid
        arbitrary_types_allowed = True


class GrapeBuyerUpdate(BaseModel):
    first_name: constr(max_length=255)
    last_name: constr(max_length=255)
    winery: Optional[constr(max_length=255)]
    email: Optional[EmailStr]
    state: Optional[constr(max_length=255)]
    grapes_seeking: Optional[List[constr(max_length=255)]]
    volume_seeking: List[Any]

    class Config:
        extra = Extra.forbid
        arbitrary_types_allowed = True


class GrapeSeller(BaseModel):
    profile_id: constr(max_length=255)
    first_name: constr(max_length=255)
    last_name: constr(max_length=255)
    vineyard: constr(max_length=255)
    email: EmailStr
    state: constr(max_length=255)
    grapes_selling: List[constr(max_length=255)]
    volume_selling: List[Any]

    class Config:
        extra = Extra.forbid
        arbitrary_types_allowed = True


class GrapeSellerUpdate(BaseModel):
    first_name: constr(max_length=255)
    last_name: constr(max_length=255)
    vineyard: Optional[constr(max_length=255)]
    email: Optional[EmailStr]
    state: Optional[constr(max_length=255)]
    grapes_selling: Optional[List[constr(max_length=255)]]
    volume_selling: List[Any]

    class Config:
        extra = Extra.forbid
        arbitrary_types_allowed = True
