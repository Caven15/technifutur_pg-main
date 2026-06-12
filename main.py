from decimal import Decimal

from sqlalchemy import select

from models.base import init_db, get_db_session, engine, Base

from models import Category, Plant, Customer


def create_sample_data(session):
	# Création de catégories
	categorie_fleur = Category(name="Fleur")
	categorie_interieur = Category(name="Plante d'intérieur")
	categorie_exterieur = Category(name="Plante d'extérieur")

	session.add_all([categorie_fleur, categorie_exterieur, categorie_interieur])
	
	session.flush() # Envoie à la db sasn commit définitif (avoir les id's)
	print(" Catégories créées et flush... (avoir les id's)")

	# Créer des plantes avec une ralation => Many-to-Many
	rose = Plant(
		name="Rose Rouge",
		description="Belle rose rouge",
		base_price=Decimal("4.50"),
		categories=[categorie_fleur,categorie_exterieur] # asignation direct => jointure N-N automatique
	)

	jonquille = Plant(
		name="jonquille",
		description="Jolie jonquilles jaune",
		base_price=Decimal("2.20"),
		categories=[categorie_fleur,categorie_exterieur] 
	)

	ficus = Plant(
		name="ficus",
		description="Jolie ficuss jaune",
		base_price=Decimal("1.80"),
		categories=[categorie_fleur,categorie_interieur]
	)

	session.add_all([rose, jonquille, ficus])
	session.flush()

	print("Plantes créées avec leurs catégories  (table d'assos est bien remplie )")

	client = Customer(
		first_name="Jhon",
		last_name="Doe"
	)
	session.add(client)
	session.flush()

	print(f" Client créé : {client.first_name} ({client.id})")

	# Utilisation de la méthode metier => client
	order = client.place_order(session, [
		(rose,3),
		(jonquille, 10),
		(ficus, 1)
	])

	print(f"Commande qui sont créée automatiquement {order.id}")

	session.commit()

def 

if __name__ == "__main__":
	with get_db_session() as session:
		
		init_db(delete=True)

		# vérification pour voir si nos données existe déjà
		existing_customer = session.execute(select(Customer)).scalar_one_or_none()

		if not existing_customer:
			create_sample_data(session)
		else:
			print("Données déjà présentes")
