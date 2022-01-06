from flask import Blueprint, request, render_template, flash, redirect, url_for
from app.auth.views import login_required
from app.models import User, Beer, Style, SavedBeers
import wikipedia
from app import db
from app.auth.views import current_user
main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
@login_required
def home():
	return render_template('home.html')

@main.route('/info')
@login_required
def info():
	return render_template('info.html')

ITEMS_PER_PAGE=15
@main.route("/database", methods=["POST", "GET"])
@login_required
def database():
    page = request.args.get('page', 1, type=int)
    beers = Beer.sub_pages().paginate(per_page=ITEMS_PER_PAGE, page=page, error_out=True)
        
    return render_template("database.html", beers=beers, beer=Style.style_filter(),users=User.display(1) )

STYLES_PER_PAGE=12
@main.route("/style", methods=["POST", "GET"])
@login_required
def style():
    page = request.args.get('page', 1, type=int)
    style = Style.sub_page().paginate(per_page=STYLES_PER_PAGE, page=page, error_out=True)
    return render_template("style.html", style=style)  

@main.route("/database/<int:id>")
@login_required
def beer_style(id):
    beer_style = Style.query.get_or_404(id)
    return render_template('beer_style.html', beer_style=beer_style)

@main.route("/database/beer_exp/<int:id>")
@login_required
def beer_expanded(id):
    beer_expanded = Beer.query.get_or_404(id)
    return render_template('beer_expanded.html', beer_expanded=beer_expanded)  

@main.route ("/search_result", methods=["GET", "POST"])
@login_required
def search_result():

    styles = request.form.get("styles")
    name = request.form.get("name").title()
    brewery = request.form.get("brewery").title()
    city = request.form.get("city").title()
    state = request.form.get("state").upper()
   
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    list11 = []
    list12 = []
    list13 = []
    list14 = []
    list15 = []
    list16 = []
    list17 = []
    list18 = []
    list19 = []
    list20 = []
    list21 = []
    list22 = []
    list23 = []
    list24 = []
    list25 = []
    list26 = []
    list27 = []
    list28 = []

    results = Beer.search_results() 
            
    for i in results:
        if (name in i.name) and (brewery in i.brewery) and (str(styles) in i.styles) and (city in i.city) and (state in i.state):
            list1.append(i.name)
            list2.append(i.brewery)
            list3.append(i.city)
            list4.append(i.state)
            list5.append(i.description)
            list6.append(i.image_url)
            list7.append(i.styles)
            list8.append(i.abv)
            list9.append(i.min_ibu)
            list10.append(i.max_ibu)
            list11.append(i.astringency)
            list12.append(i.body)
            list13.append(i.alcohol)
            list14.append(i.bitter)
            list15.append(i.sweet)
            list16.append(i.sour)
            list17.append(i.salty)
            list18.append(i.fruits)
            list19.append(i.spices)
            list20.append(i.malts)
            list21.append(i.aroma)
            list22.append(i.palate)
            list23.append(i.taste)
            list24.append(i.overall)
            list25.append(i.hops)
            list26.append(i.appearance)
            list27.append(i.id)
            list28.append(i.style_id)

    return render_template("search_result.html", count=len(list1), result1=list1, result2 = list2, result3=list3, result4=list4, result5=list5, result6=list6, result7=list7, result8=list8, result9 = list9, result10=list10, result11=list11, result12=list12, result13=list13, result14=list14, result15=list15, result16 = list16, result17=list17, result18=list18, result19=list19, result20=list20, result21=list21, result22=list22, result23 = list23, result24=list24, result25=list25, result26=list26, result27=list27, result28=list28)



def render_saved():
    user_id = current_user.id
    saved_items = SavedBeers.query.filter(SavedBeers.user_id==user_id).all()
    beer_ids = [] #saved ids for this user
    for row in saved_items:
        beer_ids.append(row.beer_id)
    result = Beer.query.filter(Beer.id.in_(beer_ids))
    return render_template("saved.html", beers=result)

@main.route("/saved", methods=["POST", "GET"])
@login_required
def saved():
    return render_saved()
      
@main.route("/add_beer/<beer_id>/", methods=["POST", "GET"])
@login_required
def add_beer(beer_id):
    fridge=SavedBeers(user_id=current_user.id, beer_id=beer_id)
    db.session.add(fridge)
    db.session.commit()
    flash("Beer successfully added to fridge!", "success")
    return render_saved()

@main.route("/delete_beer/<beer_id>", methods=["POST", "GET"])
@login_required
def delete_beer(beer_id):
    del_fridge=SavedBeers.query.filter_by(user_id=current_user.id, beer_id=beer_id).first()
    db.session.delete(del_fridge)
    db.session.commit()
    flash("Beer successfully removed from fridge!", "success")
    return render_saved()