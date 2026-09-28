#1.variables:
prenom= "molka"
age= 22
print("Hello " + prenom + " you are " + str(age) + " years old")

#2.conditions: 
nombre = 10
if nombre %2 == 0:
    print("le nombre est pair")
else:
    print("le nombre est impair")
    
#3.boucles:
#a:
m= input("mot: ")
print([l for l in m])

#b:



#4.listes:
#a:
liste = [12, 15, 9, 18, 14]
print("la liste est :" , liste)
#b:
print("la moyenne est :" , sum(liste) / len(liste))
print("la valeur max est :" , max(liste))
print("la valeur min est :" , min(liste))

#5.dictionnaires:
#a:
dictionnaire_student = {"name": "molka", "age": 22, "study field": "computer science"}
print("name: " + dictionnaire_student["name"] + " age: " + str(dictionnaire_student["age"]) + " study field: " + dictionnaire_student["study field"])

#b:

