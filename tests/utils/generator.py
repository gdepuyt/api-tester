from random import randint
from utils.formater import Formater


class Generator:

    def __init__(self, number_of_elements: int, random: bool = False):
        """
        Class to generate a list of postal codes.

        Args:
            number_of_elements (int): The number of postal codes to generate.
            random (bool): Whether the postal codes should be generated randomly (True) or if a fixed list should be used (False).
        """

        if random:
            self.zipcode = [randint(1000, 9000) for _ in range(number_of_elements)]
        else:
            self.zipcode = [1000, 7120, 6540, 7000][:number_of_elements]

        self.number_of_elements = number_of_elements
        self.random = random

    @property
    def postal_codes_list(self):
        """
        Returns the list of generated postal codes.

        Returns:
            list: The list of postal codes.
        """
        return self.zipcode

    @property
    def postal_codes_with_ids(self):
        """
        Returns the list of postal codes with formatted case IDs.

        Returns:
            list: The list of formatted postal codes with IDs.
        """
        if self.random:
            prefix = "Random Test - Postal Code"
        else:
            prefix = "Fixed Test - Postal Code"

        return list(map(lambda i: f"Case {Formater.format_number((i[0]+1),4)} {prefix}", enumerate(self.postal_codes_list)))















# class CodePostalVille:

#         def __init__(self, nombre_elements: int, alea: bool = False):
#             """
#             Classe pour générer des listes de codes postaux et de noms de villes.

#             Args:
#                 nombre_elements (int): Le nombre d'éléments à générer dans les listes.
#                 alea (bool): Indique si les codes postaux doivent être générés aléatoirement (True) ou si une liste fixe doit être utilisée (False).
#             """
    

#             if alea:
#                 self.codes_postaux = [randint(1000, 9000) for _ in range(nombre_elements)]
#             else:
#                 self.codes_postaux = [1000, 7120, 6540, 7000][:nombre_elements]


#             self.nombre_elements = nombre_elements
#             self.alea = alea 
          
#         @property
#         def list_postalcode(self):
#             """
#             Fonction pour obtenir les deux listes générées.

#             Returns:
#                 dict: Un dictionnaire contenant deux clés:
#                     - "codes_postaux": La liste des codes postaux.
#                     - "noms_villes": La liste des noms de villes avec le code postal concaténé.
#             """
#             return self.codes_postaux

#         @property
#         def list_postalcode_IDs(self):
#             """
#             Fonction pour obtenir les deux listes générées.

#             Returns:
#                 dict: Un dictionnaire contenant deux clés:
#                     - "codes_postaux": La liste des codes postaux.
#                     - "noms_villes": La liste des noms de villes avec le code postal concaténé.
#             """
#             # if self.toto:
#             #      msg = "Test avec code postal aléatoire - case : "
#             # else:
#             #      msg = "Test avec code postal définit dans la liste - case : "
#             if self.alea:
#                 prefix = "Test Aléatoire - Code Postal"
#             else:
#                 prefix = "Test Fixe - Code Postal"
            
#             return list(map(lambda i: f"Case {Formater.format_number((i[0]+1),4)} {prefix}", enumerate(self.codes_postaux)))




#             #return list(map(lambda i: f"{self.toto} : {i[0]+1}", enumerate(self.codes_postaux)))




