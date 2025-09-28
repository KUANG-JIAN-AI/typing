from flask import current_app, request

from app.models.user_mod import Users, db


def register():
    data = request.get_json()  # 从请求体里解析 JSON
    nickname = data.get("nickname")

    user = Users(nickname=nickname)

    with current_app.app_context():
        db.session.add(user)
        db.session.commit()

    return {'code': 200, 'msg': 'success'}