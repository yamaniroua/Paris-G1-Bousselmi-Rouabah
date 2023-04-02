

import numpy as np
"!pip install numpy_financial"



# ---------------------------------------FONCTION NPV-------------------------


def calculate_npv(rate, cashflows):
    npv = 0.0
    for i in range(len(cashflows)):
        npv += cashflows[i] / (1 + WACC) ** i
    return npv

# Entrées de l'utilisateur

initial_investment = float(input("Entrez le montant de l'investissement initial : "))
WACC = float(input("Entrez le taux d'actualisation : "))
cashflows = []
num_cashflows = int(input("Entrez le nombre de flux de trésorerie futurs : "))
for i in range(num_cashflows):
    cashflow = float(input("Entrez le flux de trésorerie futur pour l'année " + str(i+1) + " : "))
    cashflows.append(cashflow)

# Calcul du NPV
cashflows.insert(0, -initial_investment)
npv = calculate_npv(WACC, cashflows)

# Affichage du résultat
print("La valeur actuelle nette est : " + str(npv))
# IRR Calculation based on CF (given)
import numpy_financial as npf


def calculate_irr(cashflows):
    positive_cf = [cf for cf in cashflows if cf > 0]
    negative_cf = [cf for cf in cashflows if cf < 0]
    
    if len(negative_cf) == len(cashflows):
        return None  # Aucun taux de rendement interne n'existe pour un investissement sans rentrées de trésorerie.
    
    guess = 0.1  # valeur initiale supposée pour le taux de rendement interne
    npv = npf.npv(guess, cashflows)
    while npv > 0:
        guess += 0.01
        npv = npf.npv(guess, cashflows)
    return round(guess, 2)

# Entrées de l'utilisateur
initial_investment = float(input("Entrez le montant de l'investissement initial : "))
cashflows = []
num_cashflows = int(input("Entrez le nombre de flux de trésorerie futurs : "))
for i in range(num_cashflows):
    cashflow = float(input("Entrez le flux de trésorerie futur pour l'année " + str(i+1) + " : "))
    cashflows.append(cashflow)

# Calcul de l'IRR
cashflows.insert(0, -initial_investment)
irr = calculate_irr(cashflows)

# Affichage du résultat
if irr:
    print("Le taux de rendement interne est : " + str(irr*100) + "%")
else:
    print("Aucun taux de rendement interne n'existe pour cet investissement.") 
    
    
# Then we compute the WACC (weighted average cost of capital) by simple calculation of the cost of debt and the cost of equity 


# Fonction pour calculer le coût des capitaux propres
def calculate_cost_equity(rf, beta, rm):
    return rf + beta * (rm - rf)

# Fonction pour calculer le coût de la dette
def calculate_cost_debt(interest_rate, tax_rate):
    return interest_rate * (1 - tax_rate)

# Fonction pour calculer le WACC
def calculate_wacc(weights, costs):
    wacc = 0.0
    for i in range(len(weights)):
        wacc += weights[i] * costs[i]
    return wacc

# Entrées de l'utilisateur
rf = float(input("Entrez le taux d'intérêt sans risque (rf) : "))
rm = float(input("Entrez le taux de rendement exigé du marché (rm) : "))
beta = float(input("Entrez le bêta de l'entreprise : "))
interest_rate = float(input("Entrez le taux d'intérêt de la dette : "))
tax_rate = float(input("Entrez le taux d'imposition : "))
equity_weight = float(input("Entrez le pourcentage de poids des capitaux propres dans la structure du capital (en %) : ")) / 100
debt_weight = 1 - equity_weight

# Calcul du WACC
cost_equity = calculate_cost_equity(rf, beta, rm)
cost_debt = calculate_cost_debt(interest_rate, tax_rate)
weights = [equity_weight, debt_weight]
costs = [cost_equity, cost_debt]
wacc = calculate_wacc(weights, costs)

# Affichage du résultat
print("Le WACC est : " + str(round(wacc*100, 2)) + "%")

#-----------------------------FONCTION IRR and WACC------------------------------


# Here we would like to know if the IRR Internal Rate of Return is greater than the WACC, if so then the inverstment is profitable. 
"!Pip numpy_financial"

import numpy_financial as npf

# demander à l'utilisateur d'entrer les flux de trésorerie, séparés par des virgules
cash_flows = input("Entrez les flux de trésorerie, séparés par des virgules: ")

# convertir les flux de trésorerie en une liste d'entiers
cash_flows = [int(x) for x in cash_flows.split(',')]

# calcul de l'IRR à l'aide de la fonction np.irr()
irr = npf.irr(cash_flows)
2
# demander à l'utilisateur d'entrer le WACC
wacc = float(input("Entrez le WACC: "))

# vérifier si l'IRR est supérieur au WACC
if irr > wacc:
    print("L'investissement est rentable car l'IRR est supérieur au WACC.")
else:
    print("L'investissement n'est pas rentable car l'IRR est inférieur ou égal au WACC.")
