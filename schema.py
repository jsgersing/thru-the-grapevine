from typing import List, Optional

from pydantic import BaseModel, constr, EmailStr, Extra


class GrapeBuyer(BaseModel):
    profile_id: constr(max_length=255)
    name = constr(max_length=255)
    email = EmailStr
    state = constr(max_length=255)
    grapes_seeking = List[constr(max_length=255)]
    volume_seeking = List[int]

    class Config:
        extra = Extra.forbid


class GrapeBuyerUpdate(BaseModel):
    name = Optional[constr(max_length=255)]
    email = Optional[EmailStr]
    state = Optional[constr(max_length=255)]
    grapes_seeking = Optional[List[constr(max_length=255)]]
    volume_seeking = List[int]

    class Config:
        extra = Extra.forbid


class GrapeSeller(BaseModel):
    profile_id: constr(max_length=255)
    name = constr(max_length=255)
    email = EmailStr
    state = constr(max_length=255)
    grapes_selling = List[constr(max_length=255)]
    volume_selling = List[int]

    class Config:
        extra = Extra.forbid


class GrapeSellerUpdate(BaseModel):
    name = Optional[constr(max_length=255)]
    email = Optional[EmailStr]
    state = Optional[constr(max_length=255)]
    grapes_selling = Optional[List[constr(max_length=255)]]
    volume_selling = List[int]

    class Config:
        extra = Extra.forbid
