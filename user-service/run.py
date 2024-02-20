from app import app, db, jwt


@jwt.user_lookup_loader
def user_lookup_callback(jwt_header, jwt_payload):
    return jwt_payload.get("sub")

if __name__ == '__main__':
    with app.app_context():
      db.create_all()
    app.run(host='0.0.0.0', port=5000,debug=True)