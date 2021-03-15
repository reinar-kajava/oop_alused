from Kasutajad import Kasutajad
from Admin import Admin

tavakasutaja = Kasutajad("Tava", "Kasutaja", "user", "qwerty")
tavakasutaja.kasutaja_tervitus()

administraator = Admin("Admin", "Istraator", "root", "qwerty")
administraator.privileegid.naita_privileegid()