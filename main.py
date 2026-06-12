from models.base import init_db, get_db_session, engine, Base

if __name__ == "__main__":
	
	init_db(delete=True)
	