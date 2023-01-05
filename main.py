import colorama, os

if (os.name == "nt"):
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

def formatNumber(nombre):
	nombre_str = str(nombre)
	partie_entiere, partie_decimale = nombre_str.split(".")
	partie_entiere_inverse = partie_entiere[::-1]
	partie_entiere_formatee = ""

	for i, chiffre in enumerate(partie_entiere_inverse):
		if i > 0 and i % 3 == 0:
			partie_entiere_formatee += " "
		partie_entiere_formatee += chiffre
	
	partie_entiere_formatee = partie_entiere_formatee[::-1]
	if partie_decimale: return partie_entiere_formatee + "." + partie_decimale
	else: return partie_entiere_formatee

clear()

prixDebut = float(input("prix lors de l'achat' € : "))
somme = float(input("somme € : "))
prixFin = float(input("prix lors de la vente € : "))

solde = (somme / prixDebut) * prixFin
if (solde >= 300): soldeTaxes = (70 * solde) / 100
else: soldeTaxes = solde

benef = solde - somme
if (solde >= 300): benefTaxes = soldeTaxes - somme
else: benefTaxes = benef

print(f"""
-----------------------------------------------------------
sans taxes
-----------------------------------------------------------
Benefice : {formatNumber(benef)} €
Total    : {formatNumber(solde)} €

-----------------------------------------------------------
avec taxes
-----------------------------------------------------------
{colorama.Fore.RED}Benefice : {formatNumber(benefTaxes)} €{colorama.Fore.RESET}
Total    : {formatNumber(soldeTaxes)} €
""")
