# -*- coding: utf-8 -*-
""" Module with all nececcary functions for the ingredients Tab.
This includes all functions for the Lists, DB and Buttos/Dropdowns.
"""

import sys
import sqlite3
import time
import datetime
import csv
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

from recipes import ZutatenCB_Rezepte
from bottles import ZutatenCB_Belegung, Belegung_einlesen, Belegung_progressbar, Belegung_a
from msgboxgenerate import standartbox
from loggerconfig import logfunction, logerror

import globals


def custom_output(w, DB, c):
    w.ingredientdialog()


@logerror
def Zutat_eintragen(w, DB, c, newingredient = True):
    """ Insert the new ingredient into the DB, if all values are given 
    and its name is not already in the DB.
    Also can change the current selected ingredient (newingredient = False)
    """
    # print("Zutat ist: ", w.LEZutatRezept.text())
    # print("Alkoholanteil ist: ", w.LEGehaltRezept.text())
    # print("Flaschenvolumen ist: ", w.LEFlaschenvolumen.text())
    # print("Neues Rezept: {}".format(newingredient))
    Zutatentest = 0
    ingredientname = w.LEZutatRezept.text()
    # counts the entries in the DB with the name and checks if its already there
    if newingredient:
        c.execute("SELECT COUNT(*) FROM Zutaten WHERE Name=?",
                (ingredientname,))
        Zutatentest = c.fetchone()[0]
    if Zutatentest != 0 and newingredient:
        standartbox("Dieser Name existiert schon in der Datenbank!")
    # if the ingredient should be changed, check if its selected (should always be) and get the ID
    if not newingredient and not w.LWZutaten.selectedItems():
        Zutatentest = 1
        standartbox("Es ist keine Zutat ausgewählt!")
    elif not newingredient and w.LWZutaten.selectedItems():
        altername = w.LWZutaten.currentItem().text()
        Zspeicher = c.execute(
            "SELECT ID FROM Zutaten WHERE Name = ?", (altername,)).fetchone()[0]
        ZID = int(Zspeicher)
    # check if all Fields are filled
    if Zutatentest == 0:
        if (ingredientname == "") or (w.LEGehaltRezept.text() == "") or (w.LEFlaschenvolumen.text() == ""):
            standartbox("Eine der Eingaben ist leer!")
            Zutatentest = 1
    # check if the numbers make sense and then saves them into variables
    if Zutatentest == 0:
        try:
            conc = int(w.LEGehaltRezept.text())
            vol = int(w.LEFlaschenvolumen.text())
            if conc > 100:
                Zutatentest = 1
                standartbox(
                    "Alkoholgehalt kann nicht größer als 100 sein!")
        except ValueError:
            Zutatentest = 1
            standartbox(
                "Alkoholgehalt und Flaschenvolumen muss eine Zahl sein!")
    # if everything is okay, insert or update the db, and the List widget
    if Zutatentest == 0:
        if newingredient:
            c.execute("INSERT OR IGNORE INTO Zutaten(Name,Alkoholgehalt,Flaschenvolumen,Verbrauchsmenge,Verbrauch,Mengenlevel) VALUES (?,?,?,0,0,0)", (
                ingredientname, conc, vol))        
        else:
            vol_old = c.execute("SELECT Mengenlevel FROM Zutaten WHERE ID = ?", (ZID,)).fetchone()[0]
            if int(vol_old) > vol:
                vol_old = vol
            c.execute("UPDATE OR IGNORE Zutaten SET Name = ?, Alkoholgehalt = ?, Flaschenvolumen = ?, Mengenlevel = ? WHERE ID = ?",
                (ingredientname, conc, vol, vol_old, ZID))
            # Updates the level of the bottles and their labels
            Belegung_progressbar(w, DB, c)
            Belegung_a(w, DB, c)
        DB.commit()
        # old ingredients need to be deleted and readded
        # also when you delete an item, the selection jumps to the next item
        # to prevent strange bugs deselect all items
        if not newingredient:
            delfind = w.LWZutaten.findItems(altername, Qt.MatchExactly)
            if len(delfind) > 0:
                for item in delfind:
                    w.LWZutaten.takeItem(w.LWZutaten.row(item))
            for i in range(w.LWZutaten.count()):
                w.LWZutaten.item(i).setSelected(False)
        w.LWZutaten.addItem(ingredientname)
        # Deletes the used values
        w.LEZutatRezept.clear()
        w.LEGehaltRezept.clear()
        w.LEFlaschenvolumen.clear()
        ZutatenCB_Rezepte(w, DB, c)
        # if its a new ingredient, adds it to the boxes and sorts them
        # if its a changed one, update the values
        for box in range(1, 11):
            CBBname = getattr(w, "CBB" + str(box))
            if newingredient:
                CBBname.addItem(ingredientname)
                CBBname.model().sort(0)
            else:
                index = CBBname.findText(altername, Qt.MatchFixedString)
                if index >= 0:
                    CBBname.setItemText(index, ingredientname)
        if newingredient:
            standartbox("Zutat eingetragen")
        else:
            standartbox("Zutat mit dem Namen: <{}> under <{}> aktualisiert".format(altername, ingredientname))


@logerror
def Zutaten_a(w, DB, c):
    """ Load all ingredientnames into the ListWidget """
    w.LWZutaten.clear()
    Zspeicher = c.execute("SELECT Name FROM Zutaten")
    for Werte in Zspeicher:
        w.LWZutaten.addItem(Werte[0])


@logerror
def Zutaten_delete(w, DB, c):
    """ Deletes an ingredient out of the DB if its not needed in any recipe. \n
    In addition to do so, a password is needed in the interface.
    """
    ZID = 0
    if w.LEpw2.text() == globals.masterpassword:
        if not w.LWZutaten.selectedItems():
            standartbox("Keine Zutat ausgewählt!")
        else:
            Zname = w.LWZutaten.currentItem().text()
            Zspeicher = c.execute(
                "SELECT ID FROM Zutaten WHERE Name = ?", (Zname,))
            for row in Zspeicher:
                ZID = row[0]
            c.execute("SELECT COUNT(*) FROM Zusammen WHERE Zutaten_ID=?", (ZID,))
            Zutatentest = c.fetchone()[0]
            # Checks if the ingredient is used in any bottle or in any recipe and reacts accordingly
            if Zutatentest == 0:
                c.execute("SELECT COUNT(*) FROM Belegung WHERE ID=?", (ZID,))
                Zutatentest = c.fetchone()[0]
                if Zutatentest == 0:
                    c.execute("DELETE FROM Zutaten WHERE ID = ?", (ZID,))
                    DB.commit()
                    ZutatenCB_Rezepte(w, DB, c)
                    # This isn't nececary, a simple remove is better
                    # ZutatenCB_Belegung(w, DB, c)
                    for box in range(1, 11):
                        CBBname = getattr(w, "CBB" + str(box))
                        index = CBBname.findText(Zname, Qt.MatchFixedString)
                        if index >= 0:
                            globals.supressbox = True
                            CBBname.removeItem(index)
                            globals.supressbox = False
                    Zutaten_clear(w, DB, c)
                    Zutaten_a(w, DB, c)
                    standartbox("Zutat mit der ID und dem Namen:\n<{}> <{}>\ngelöscht!".format(ZID, Zname))
                else:
                    standartbox(
                        "Achtung, die Zutat ist noch in der Belegung registriert!")
            # if the ingredient is still used in recipes, inform the user about it and the first 10 recipes
            else:
                stringsaver = c.execute("SELECT Rezepte.Name FROM Zusammen INNER JOIN Rezepte ON Rezepte.ID = Zusammen.Rezept_ID WHERE Zusammen.Zutaten_ID=?", (ZID,))
                Zutatenliste = []
                for output in stringsaver:
                    Zutatenliste.append(output[0])
                    if len(Zutatenliste) >= 10:
                        break
                Zutatenstring = ', '.join(Zutatenliste)
                standartbox("Zutat kann nicht gelöscht werden, da sie in {} Rezept(en) genutzt wird! Diese sind (maximal die zehn ersten):\n{}".format(Zutatentest, Zutatenstring))
    else:
        standartbox("Falsches Passwort!")
    w.LEpw2.setText("")


@logerror
def Zutaten_Zutaten_click(w, DB, c):
    """ Search the DB entry for the ingredient and displays them """
    if w.LWZutaten.selectedItems():
        Zspeicher = c.execute(
            "SELECT Alkoholgehalt, Flaschenvolumen FROM Zutaten WHERE Name = ?", (w.LWZutaten.currentItem().text(),))
        for row in Zspeicher:
            w.LEGehaltRezept.setText(str(row[0]))
            w.LEFlaschenvolumen.setText(str(row[1]))
        w.LEZutatRezept.setText(w.LWZutaten.currentItem().text())


@logerror
def Zutaten_Flvolumen_pm(w, DB, c, operator):
    """ Increase or decrease the Bottlevolume by a given amount (25). \n
    The value cannot exceed the minimal or maximal Volume (100/1500).
    """
    minimalvolumen = 100
    maximalvolumen = 1500
    dvol = 50
    # sets the conditions that the value can not exceed the min/max value by clicking
    try:
        value_ = int(w.LEFlaschenvolumen.text())
        if operator == "+" and value_ < maximalvolumen:
            value_ += dvol
        elif operator == "-" and value_ > minimalvolumen:
            value_ -= dvol
    except ValueError:
        value_ = minimalvolumen
    w.LEFlaschenvolumen.setText(str(value_))


@logerror
def Zutaten_clear(w, DB, c):
    """ Clears all entries in the ingredient windows. """
    w.LWZutaten.clearSelection()
    w.LEZutatRezept.clear()
    w.LEGehaltRezept.clear()
    w.LEFlaschenvolumen.clear()
