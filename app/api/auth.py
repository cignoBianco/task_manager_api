@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = crud.user.get_by_email(db, data.email)

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401)

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token}