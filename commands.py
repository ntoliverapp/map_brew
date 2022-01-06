from app import db, create_app
app = create_app()
app.app_context().push()
from app.models import User, Style, Beer



def init_user_db(filename):
    db.create_all()
    print('Initialized User Database')
    with open(filename, "r") as f:
        for line in f.readlines():
            data = line.strip().split(",")
            print(data[1])
            data = User(email=data[0], username=data[1], password=data[2], age=data[3])
            
            db.session.add(data)
            db.session.commit()
    print('User Database Successfully Imported')
    
def init_style_db(filename):
    db.create_all()
    print('Initialized Style Database')
    with open(filename, "r") as f:
        for line in f.readlines():
            data = line.strip().split(",")
            print(data[0])
            
            data = Style(name=data[0], description=data[1], source=data[2], image_url=data[3])
            
            db.session.add(data)
            db.session.commit()
    print('Style Database Successfully Complete')

def init_beer_db(filename):
    db.create_all()
    print('Initialized Beer Database')
    with open(filename, "r") as f:
        for line in f.readlines():
            data = line.strip().split(",")
            # print(data)
            print(data[0])
            # print(Style.query.filter_by(name='Altbier').first().style_id)
            id = Style.query.filter_by(name=data[1]).first().id
            data = Beer(name=data[0], styles=data[1], brewery=data[2], city=data[3],state=data[4], description=data[5], abv=data[6], min_ibu=data[7],max_ibu=data[8], astringency=data[9], body=data[10],alcohol=data[11], bitter=data[12], sweet=data[13], sour=data[14],salty=data[15], fruits=data[16], hops=data[17],spices=data[18], malts=data[19], aroma=data[20], appearance=data[21],palate=data[22], taste=data[23], overall=data[24], image_url=data[25], style_id=id)
            with app.app_context():

                db.session.add(data)
                db.session.commit()
    print('Beer Database Successfully Complete')
            

# def init_mouthfeel_db(filename):
#     db.create_all()
#     print('Initialized Mouthfeel database')
#     with open(filename, "r") as f:
#         for line in f.readlines():
#             data = line.strip().split(",")
#             print(data[0])
            
#             data = Mouthfeel(astringent=data[0], body=data[1], alcoholic=data[2])
            
#             db.session.add(data)
#             db.session.commit()
#     print('Mouthfeel Database Successfully Complete')

# def init_taste_db(filename):
#     db.create_all()
#     print('Initialized Taste database')
#     with open(filename, "r") as f:
#         for line in f.readlines():
#             data = line.strip().split(",")
#             print(data[1])
            
#             data = Taste(bitter=data[0], sweet=data[1], sour=data[2], salty=data[3])
            
#             db.session.add(data)
#             db.session.commit()
#     print('Taste Database Successfully Complete')
    
# def init_flavor_aroma_db(filename):
#     db.create_all()
#     print('Initialized Flavor Aroma database')
#     with open(filename, "r") as f:
#         for line in f.readlines():
#             data = line.strip().split(",")
#             print(data[1])
            
#             data = FlavorAroma(fruity=data[0], hoppy=data[1], spices=data[2], malty=data[3])
            
#             db.session.add(data)
#             db.session.commit()
#     print('Flavor Aroma Database Successfully Complete')
    
def drop_all_db():
    if input(
        "Are you sure you want to lose all your data?"):
        db.drop_all()
        print("Dropped the database")

         
# if __name__ == '__main__':
#     # init_user_db("/Users/appleadmin2/Desktop/User.csv")
#     init_style_db("/Users/appleadmin2/Desktop/csv/Style.csv")
#     init_beer_db("/Users/appleadmin2/Desktop/csv/BeerInfo.csv")
    # init_mouthfeel_db("/Users/appleadmin2/Desktop/Mouthfeel.csv")
    # init_taste_db("/Users/appleadmin2/Desktop/Taste.csv")
    # init_flavor_aroma_db("/Users/appleadmin2/Desktop/FlavorAroma.csv")
    # drop_all_db()
   


