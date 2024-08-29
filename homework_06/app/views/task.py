from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from sqlalchemy.orm import selectinload
from flask_pydantic import validate
from datetime import datetime

from models import Task, Tag
from database_connection import db
from schemes import (RequestTaskPost,
                     RequestTaskPatch,
                     ResponseTask)


task_router = Blueprint("tasks", __name__)


@task_router.route("/", endpoint='tasks', methods=['GET'])
def tasks_list():
    stmt = (db.select(Task)
            .options(selectinload(Task.tags))
            .order_by(Task.id))
    tasks_with_tags = db.session.execute(stmt).scalars().all()
    return render_template('tasks/tasks.html',
                           tasks=tasks_with_tags, hostname=request.host_url)


@task_router.route("/", methods=['POST'])
@validate()
def add_task(form: RequestTaskPost):

    tags = form.tags.split(",")

    existing_tags = []

    for name in tags:

        tag = db.session.scalars(
            (
                db.select(Tag).where(Tag.name == name)
            )
        ).first()
        if tag is None:
            tag = Tag(name=name)
            db.session.add(tag)
        existing_tags.append(tag)
    db.session.commit()

    task = Task(title=form.title, content=form.content,
                published_at=datetime.now().date(),
                tags=existing_tags)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('tasks.tasks'))


@task_router.route("/", methods=['DELETE'])
def delete_task():
    task_id = request.args.get('id', type=int)
    task = db.session.scalars(
        (db.select(Task)
         .where(Task.id == task_id)
         )
    ).first()
    db.session.delete(task)
    db.session.commit()
    return jsonify(success=True)


@task_router.route("/update/form/", methods=['POST'])
@validate()
def update_task(form: RequestTaskPatch):
    # stmt = db.session(Task).where(Task.id == form.id)
    # task = db.session.scalars(stmt).first()

    task = db.session.execute(db.select(Task).filter_by(id=form.id)).scalar_one()

    task.title = form.title
    task.content = form.content

    tags = form.tags.split(",")

    existing_tags = []

    for name in tags:

        tag = db.session.scalars(
            (
                db.select(Tag).where(Tag.name == name)
            )
        ).first()
        if tag is None:
            tag = Tag(name=name)
            db.session.add(tag)
        existing_tags.append(tag)
    db.session.commit()


    task.tags = existing_tags
    db.session.commit()

    return redirect(url_for('tasks.tasks'))


@task_router.route('/add/')
def tasks_add_page():
    return render_template('tasks/task_add.html')


@task_router.route('/update/')
def tasks_update_page():
    task_id = request.args.get('id', type=int)
    stmt = (db.select(Task)
            .where(Task.id == task_id)
            .options(selectinload(Task.tags))
            )
    task_with_tags = db.session.execute(stmt).scalars().first()
    return render_template('tasks/task_update.html',
                           task=task_with_tags)




