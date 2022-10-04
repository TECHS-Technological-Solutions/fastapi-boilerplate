import re
from datetime import datetime
from uuid import UUID
from enum import Enum
from typing import Optional

import phonenumbers
from pydantic import BaseModel, EmailStr, validator, constr
from argon2 import PasswordHasher


JWT_ALGORITHM = 'HS512'

argon_ph = PasswordHasher()


def validator_non_empty_string(val: str):
    if val is not None and len(val) < 1:
        raise ValueError('Value must not be empty.')
    return val


class BasicMessage(BaseModel):
    detail: str


class TokenTypeEnum(str, Enum):
    bearer = 'Bearer'


class TokenResponse(BaseModel):
    auth_token: str
    token_type: TokenTypeEnum


class SignupRequest(BaseModel):
    """
    Regular user signup validator
    """
    email: EmailStr
    first_name: constr(min_length=1)
    last_name: constr(min_length=1)
    phone_number: constr(min_length=8)

    organization_id: constr(min_length=1)

    password: constr(min_length=8, max_length=128)
    password_confirmation: constr(min_length=8)

    invite_token: Optional[str] = ''  # pylint: disable=unsubscriptable-object

    @validator('email')
    def lower_case_email(cls, email: str):
        return email.lower()

    @validator('invite_token')
    def prevent_invite_token_empty_string(cls, val: str):
        return validator_non_empty_string(val)

    @validator('password')
    def validate_password(cls, password: str):
        error_message = ''
        if not re.search(r'.*\d.*', password):
            error_message += "Password must contain digit.\n"
        if not re.search(r'.*[A-Z].*', password):
            error_message += "Password must contain capital letter.\n"
        if not re.search(r'.*[a-z].*', password):
            error_message += "Password must contain lower letter.\n"
        if not re.search(r'.*\W.*', password):
            error_message += "Password must contain special character.\n"
        if error_message:
            raise ValueError(error_message)
        return password

    @validator('phone_number')
    def is_phone_number_valid(cls, phone_number):
        check_phone_num = phonenumbers.parse(phone_number)
        if not phonenumbers.is_possible_number(check_phone_num):
            raise ValueError("Provided phone number is not valid.")
        return phone_number

    @validator('password_confirmation')
    def validate_password_confirmation(cls, password_confirmation: str, values: dict):
        if password_confirmation and values['password'] and values['password'] != password_confirmation:
            raise ValueError('Passwords must match.')
        return password_confirmation


class ResetPasswordRequest(BaseModel):
    email: str
    organization_id: UUID


class ResetPasswordToken(BaseModel):
    token: str
    user_id: UUID
    expiration: datetime
    is_used: bool = False


class ResetPasswordConfirm(BaseModel):
    email: str
    token: str
    new_password: str
    new_password_confirm: str
    organization_id: UUID


class AuthRequestResponse(BaseModel):
    id: UUID
    is_verified: bool

    class Config:
        orm_mode = True


# pylint:disable=unsubscriptable-object
class User(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: Optional[datetime]
    email: str
    phone_number: str
    is_superuser: bool

    class Config:
        orm_mode = True
