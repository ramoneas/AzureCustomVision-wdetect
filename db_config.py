import os
from dotenv import load_dotenv

import mysql.connector

from datetime import datetime
from azure_config import azure_object_detection

load_dotenv()
HOST = os.getenv('HOST')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
DATABASE = os.getenv('DATABASE')


#INSERT WEAPON SPC
def db_insert_weapon_spc(db, mycursor, pistols, revolvers, machine_gun, sub_machine_gun, grenades):
    weapon_sql = ("INSERT INTO weapon_loadout (pistols, revolvers, machine_gun, submachine_gun, grenades) VALUES (%s, %s, %s, %s, %s)")
    weapon_qty = (pistols, revolvers, machine_gun, sub_machine_gun, grenades)
    mycursor.execute(weapon_sql, weapon_qty)
    db.commit()

    print(mycursor.rowcount, "record inserted.")
    
    return mycursor.lastrowid
#INSERT MAIN DATA
def db_insert_main_data(db, mycursor, last_loadout_id, official, location, transportation, institution):
    data_sql = ("INSERT INTO load_data (official_in_charge, location, weapon_loadout, transportation_type, institution_in_charge, date) VALUES (%s, %s, %s, %s, %s, %s)")
    data_val = (official, location, last_loadout_id, transportation, institution, datetime.now())
    mycursor.execute(data_sql, data_val)
    db.commit()
    
    return mycursor.lastrowid

def main():
  #Extracting data from azure object detection
  objects = azure_object_detection()
  pistols = objects.count("pistol")
  revolvers = objects.count("revolver")
  machine_gun = objects.count("machinegun")
  sub_machine_gun = objects.count("subfusil")
  grenades = objects.count("grenade")

  #MySQL dB init connection
  db = mysql.connector.connect(
    host=HOST, 
    user=USERNAME,
    passwd=PASSWORD,
    database = DATABASE)

  mycursor = db.cursor()

  return db, mycursor, db_insert_weapon_spc(db, mycursor, pistols, revolvers, machine_gun, sub_machine_gun, grenades)


