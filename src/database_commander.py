from src.supporter import DatabaseHandler


class DatabaseCommander:
    """Commander Class to execute queries and return the results as lists """

    def __init__(self):
        self.handler = DatabaseHandler()

    def get_recipe_ingredients(self, recipe_id):
        query = "SELECT Zutaten.Name, Zusammen.Menge, Zusammen.Hand FROM Zusammen INNER JOIN Zutaten ON Zusammen.Zutaten_ID = Zutaten.ID WHERE Zusammen.Rezept_ID = ?"
        return self.handler.query_database(query, (recipe_id,))

    def get_all_recipes_properties(self):
        query = "SELECT ID, Name, Alkoholgehalt, Menge, Kommentar, Enabled, V_Alk, c_Alk, V_Com, c_Com FROM Rezepte"
        return self.handler.query_database(query)

    def build_recipe_object(self):
        recipe_object = {}
        recipe_data = self.get_all_recipes_properties()
        for recipe in recipe_data:
            ingredient_data = self.get_recipe_ingredients(recipe[0])
            recipe_object[recipe[1]] = {
                "ID": recipe[0],
                "alcohollevel": recipe[2],
                "volume": recipe[3],
                "comment": recipe[4],
                "enabled": recipe[5],
                "volume_alcohol": recipe[6],
                "concentration_alcohol": recipe[7],
                "volume_comment": recipe[8],
                "concentration_comment": recipe[9],
                "ingredients": {a[0]: [a[1], a[2]] for a in ingredient_data},
            }
        return recipe_object

    def get_ingredients_at_bottles(self):
        query = "SELECT Zutat_F FROM Belegung"
        result = self.handler.query_database(query)
        return [x[0] for x in result]

    def get_ingredient_names(self, condition_filter=""):
        query = "SELECT Name FROM Zutaten"
        if condition_filter != "":
            query = f"{query} {condition_filter}"
        names = self.handler.query_database(query)
        return [x[0] for x in names]

    def get_ingredient_names_hand(self):
        return self.get_ingredient_names("WHERE Hand = 1")

    def get_ingredient_names_machine(self):
        return self.get_ingredient_names("WHERE Hand = 0")

    def get_bottle_fill_levels(self):
        query = "SELECT Zutaten.Mengenlevel, Zutaten.Flaschenvolumen FROM Belegung LEFT JOIN Zutaten ON Zutaten.ID = Belegung.ID"
        values = self.handler.query_database(query)
        levels = []
        for current_value, max_value in values:
            # restrict the value between 0 and 100
            proportion = 0
            if current_value != None:
                proportion = round(min(max(current_value / max_value * 100, 0), 100))
            levels.append(proportion)
        return levels

    def get_ingredient_data(self, ingredient_name):
        query = "SELECT ID, Name, Alkoholgehalt, Flaschenvolumen, Hand, Mengenlevel FROM Zutaten WHERE Name = ?"
        values = self.handler.query_database(query, (ingredient_name,))
        if values:
            values = values[0]
            return {
                "ID": values[0],
                "name": values[1],
                "alcohollevel": values[2],
                "volume": values[3],
                "hand_add": values[4],
                "volume_level": values[5],
            }
        return {}

    def get_bottle_usage(self, ingredient_id):
        query = "SELECT COUNT(*) FROM Belegung WHERE ID = ?"
        if self.handler.query_database(query, (ingredient_id,))[0][0]:
            return True
        return False

    # set (update) commands
    def set_bottleorder(self, ingredient_names):
        for i, ingredient in enumerate(ingredient_names):
            bottle = i + 1
            query = "UPDATE OR IGNORE Belegung SET ID = (SELECT ID FROM Zutaten WHERE Name = ?), Zutat_F = ? WHERE Flasche = ?"
            searchtuple = (ingredient, ingredient, bottle)
            self.handler.query_database(query, searchtuple)

    def set_bottle_volumelevel_to_max(self, boolean_list):
        query = "UPDATE OR IGNORE Zutaten Set Mengenlevel = Flaschenvolumen WHERE ID = (SELECT ID FROM Belegung WHERE Flasche = ?)"
        for i, set_to_max in enumerate(boolean_list):
            bottle = i + 1
            if set_to_max:
                self.handler.query_database(query, (bottle,))

    def set_ingredient_data(self, ingredient_name, alcohollevel, volume, new_level, onlyhand, ingredient_id):
        query = "UPDATE OR IGNORE Zutaten SET Name = ?, Alkoholgehalt = ?, Flaschenvolumen = ?, Mengenlevel = ?, Hand = ? WHERE ID = ?"
        searchtuple = (ingredient_name, alcohollevel, volume, new_level, onlyhand, ingredient_id)
        self.handler.query_database(query, searchtuple)

    # insert commands
    def insert_new_ingredient(self, ingredient_name, alcohollevel, volume, onlyhand):
        query = "INSERT OR IGNORE INTO Zutaten(Name,Alkoholgehalt,Flaschenvolumen,Verbrauchsmenge,Verbrauch,Mengenlevel,Hand) VALUES (?,?,?,0,0,0,?)"
        searchtuple = (ingredient_name, alcohollevel, volume, onlyhand)
        self.handler.query_database(query, searchtuple)
