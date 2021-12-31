from flask import Blueprint, render_template, flash, url_for, redirect
from app.auth.views import current_user, login_required, logout_user
from app.models import User
from app import db
from werkzeug.utils import escape, unescape
from app.account.forms import UpdateAccountForm

account = Blueprint("account", __name__, template_folder="templates")

@account.route("/profile/<username>")
@login_required
def show(username):
	user = User.query.filter_by(username=username).first()
	return render_template("show_account.html", user=user)

@account.route("/edit", methods=["GET", "POST"])
@login_required
def edit():
	form = UpdateAccountForm()

	if form.validate_on_submit():
		current_user.email 	 = escape(form.email.data)
		current_user.username = escape(form.username.data)
		db.session.add(current_user._get_current_object())
		db.session.commit()
		flash("Your account has been updated.", "success")
		return redirect(url_for("account.show", username=current_user.username))

	form.email.data 	  = unescape(current_user.email)
	form.username.data = unescape(current_user.username)
	return render_template("edit_account.html", form=form)

@account.route("/delete", methods=["POST"])
@login_required
def delete():
	db.session.delete(current_user._get_current_object())
	db.session.commit()
	logout_user()
	flash("Your account has been deleted.", "success")
	return redirect(url_for("auth.login"))
