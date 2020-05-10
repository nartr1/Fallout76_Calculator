#! /usr/bin/python3
import csv
import PySimpleGUI as sg
import sys


sg.theme('Dark Black')


resource = "resources/Fallout_Pricing_complicated_sheet.csv"

fields = ["GunName","GunType","GunValue","GunLegacy","MeleeName","MeleeType","MeleeValue","MeleeLegacy","Prefix","PrefixValue","Major","MajorValue","WeaponType","Minor","MinorValue","WeaponTypeMinor"]

guns = []
#gun = {"GunName":"","GunType":"","GunValue":"","GunLegacy":""}
melees = []
#melee = {"MeleeName":"","MeleeType":"","MeleeValue":"","MeleeLegacy":""}
prefixes = []
#prefix = {"Prefix":"", "PrefixValue":""}
majors = []
#major = {"Major":"","MajorValue":"","WeaponType":""}
minors = []
#minor = {"Minor":"","MinorValue":"","WeaponTypeMinor":""}
basegun = {"GunName":"","GunType":"","GunValue":"","GunLegacy":""}
basemelee = {"MeleeName":"","MeleeType":"","MeleeValue":"","MeleeLegacy":""}
baseprefix = {"Prefix":"", "PrefixValue":""}
basemajor = {"Prefix":"", "PrefixValue":""}
baseminor = {"Minor":"","MinorValue":"","WeaponTypeMinor":""}

with open(resource, "r", newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    gun = {"GunName":"","GunType":"","GunValue":"","GunLegacy":""}
    melee = {"MeleeName":"","MeleeType":"","MeleeValue":"","MeleeLegacy":""}
    prefix = {"Prefix":"", "PrefixValue":""}
    major = {"Prefix":"", "PrefixValue":""}
    minor = {"Minor":"","MinorValue":"","WeaponTypeMinor":""}

    gun = {"GunName":row['GunName'],"GunType":row['GunType'],"GunValue":row["GunValue"],"GunLegacy":row["GunLegacy"]}
    melee = {"MeleeName":row['MeleeName'],"MeleeType":row['MeleeType'],"MeleeValue":row['MeleeValue'],"MeleeLegacy":row['MeleeLegacy']}
    prefix = {"Prefix":row['Prefix'], "PrefixValue":row['PrefixValue']}
    major = {"Major":row['Major'],"MajorValue":row['MajorValue'],"WeaponType":row['WeaponType']}
    minor = {"Minor":row['Minor'],"MinorValue":row['MinorValue'],"WeaponTypeMinor":row['WeaponTypeMinor']}

    if gun != basegun:
      guns.append(gun)
    if melee != basemelee:
      melees.append(melee)
    if prefix != baseprefix:
      prefixes.append(prefix)
    if major != basemajor:
      majors.append(major)
    if minor != baseminor:
      minors.append(minor)
    gunNames = []
    meleeNames = []
    prefixNames = []
    majorNames = []
    minorNames = []
    for gun in guns:
      gunNames.append(gun["GunName"])
    for melee in melees:
      meleeNames.append(melee["MeleeName"])
    for prefix in prefixes:
      prefixNames.append(prefix["Prefix"])
    for major in majors:
      majorNames.append(major["Major"])
    for minor in minors:
      minorNames.append(minor["Minor"])


def weaponFromName(name, weapon_list, type):
  weapon = ""
  for i in weapon_list:
    if type == "gun" and name in i["GunName"]:
      weapon = i
      break
    if type == "melee" and name in i["MeleeName"]:
      weapon = i
      break
  print(weapon)
  return weapon
  pass
def gunPrefix(weapon):
  layout_prefix = [[sg.Text("Choose your prefix:")],
            [sg.Listbox(prefixNames,size=(80, 20), key="-GUNPREFIX-")],
            [sg.Button('Ok')]
           ]
  window = sg.Window('Fallout Calculator', layout_prefix)
  while True:
    event, values = window.read()
    if event in (None, 'Exit'):
      break
    if event == "Ok":
      if values["-GUNPREFIX-"]:
        print(values['-GUNPREFIX-'][0])
        #print(weapon)
        weapon["Prefix"] = values['-GUNPREFIX-'][0]
        window.close()
        gunMajor(weapon)
  pass
def meleePrefix(weapon):
  layout_prefix = [[sg.Text("Choose your prefix:")],
            [sg.Listbox(prefixNames,size=(80, 20), key="-MELEEPREFIX-")],
            [sg.Button('Ok')]
           ]
  window = sg.Window('Fallout Calculator', layout_prefix)
  while True:
    event, values = window.read()
    if event in (None, 'Exit'):
      break
    if event == "Ok":
      if values["-MELEEPREFIX-"]:
        print(values['-MELEEPREFIX-'][0])
        weapon["Prefix"] = values['-MELEEPREFIX-'][0]
        window.close()
        meleeMajor(weapon)
  pass
def gunMajor(weapon):
  gunMajors = []
  for i in majors:
    if i["WeaponType"] == "Ranged" or i["WeaponType"] == "Both":
      gunMajors.append(i["Major"])
  layout_prefix = [[sg.Text("Choose your major:")],
            [sg.Listbox(gunMajors,size=(80, 20), key="-GUNMAJOR-")],
            [sg.Button('Ok')]
           ]
  window = sg.Window('Fallout Calculator', layout_prefix)
  while True:
    event, values = window.read()
    if event in (None, 'Exit'):
      break
    if event == "Ok":
      if values["-GUNMAJOR-"]:
        print(values['-GUNMAJOR-'][0])
        #print(weapon)
        weapon["Major"] = values['-GUNMAJOR-'][0]
        print(weapon)
        window.close()
        gunMinor(weapon)
  pass
def meleeMajor(weapon):
  meleeMajors = []
  for i in majors:
    if i["WeaponType"] == "Melee" or i["WeaponType"] == "Both":
      meleeMajors.append(i["Major"])
  layout_prefix = [[sg.Text("Choose your major:")],
            [sg.Listbox(meleeMajors,size=(80, 20), key="-MELEEMAJOR-")],
            [sg.Button('Ok')]
           ]
  window = sg.Window('Fallout Calculator', layout_prefix)
  while True:
    event, values = window.read()
    if event in (None, 'Exit'):
      break
    if event == "Ok":
      if values["-MELEEMAJOR-"]:
        print(values['-MELEEMAJOR-'][0])
        #print(weapon)
        weapon["Major"] = values['-MELEEMAJOR-'][0]
        print(weapon)
        window.close()
        meleeMinor(weapon)
  pass

  meleeMinor(weapon)
  pass
def gunMinor(weapon):
  gunMinors = []
  for i in minors:
    if i["WeaponTypeMinor"] == "Ranged" or i["WeaponTypeMinor"] == "Both":
      gunMinors.append(i["Minor"])
  layout_prefix = [[sg.Text("Choose your minor:")],
            [sg.Listbox(gunMinors,size=(80, 20), key="-GUNMINOR-")],
            [sg.Button('Ok')]
           ]
  window = sg.Window('Fallout Calculator', layout_prefix)
  while True:
    event, values = window.read()
    if event in (None, 'Exit'):
      break
    if event == "Ok":
      if values["-GUNMINOR-"]:
        print(values['-GUNMINOR-'][0])
        #print(weapon)
        weapon["Minor"] = values['-GUNMINOR-'][0]
        window.close()
        presentWeapon(weapon)

  pass
def meleeMinor(weapon):
  meleeMinors = []
  for i in minors:
    if i["WeaponTypeMinor"] == "Melee" or i["WeaponTypeMinor"] == "Both":
      meleeMinors.append(i["Minor"])
  layout_prefix = [[sg.Text("Choose your minor:")],
            [sg.Listbox(meleeMinors,size=(80, 20), key="-MELEEMINOR-")],
            [sg.Button('Ok')]
           ]
  window = sg.Window('Fallout Calculator', layout_prefix)
  while True:
    event, values = window.read()
    if event in (None, 'Exit'):
      break
    if event == "Ok":
      if values["-MELEEMINOR-"]:
        print(values['-MELEEMINOR-'][0])
        #print(weapon)
        weapon["Minor"] = values['-MELEEMINOR-'][0]
        window.close()
        presentWeapon(weapon)


  pass
def presentWeapon(weapon):
  prefixValue = ""
  majorValue = ""
  minorValue = ""

  for prefix in prefixes:
    if weapon["Prefix"] == prefix["Prefix"]:
      prefixValue = prefix["PrefixValue"]
      break
  for major in majors:
    if weapon["Major"] == major["Major"]:
      majorValue = major["MajorValue"]
      break
  for minor in minors:
    if weapon["Minor"] == minor["Minor"]:
      minorValue = minor["MinorValue"]
      break

  layout = [[sg.Text("Here is your weapon:")],
            [sg.Text("Weapon: {0}\nPrefix Value: {1}\nMajor value: {2}\nMinor Value: {3}\n".format(weapon, prefixValue, majorValue, minorValue))]
           ]
  window = sg.Window('Fallout Calculator', layout)
  while True:
    event, values = window.read()
    if event in (None, 'Exit'):
      sys.exit(0)



  pass

def main():
  weapon = {}

  layout = [[sg.Text("Choose your weapon:")],
            [sg.Listbox(gunNames,size=(80, 20), key="-GUN-"), sg.Listbox(meleeNames,size=(80, 20), key="-MELEE-")],
            [sg.Button('Choose Gun'),sg.Button('Choose Melee')]
           ]
  window = sg.Window('Fallout Calculator', layout)

  while True:  # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
      break
    if event == 'Choose Gun':
        if values['-GUN-']:
            #sg.popup(f"You have chosen is {values['-GUN-'][0]}")
            list_of_weapons = guns
            #print(list_of_weapons)
            current_weapon = weaponFromName(values['-GUN-'][0], list_of_weapons, "gun")
            window.close()
            gunPrefix(current_weapon)
    if event == 'Choose Melee':
        if values['-MELEE-']:
            list_of_weapons = melees
            current_weapon = weaponFromName(values['-MELEE-'][0], list_of_weapons, "melee")
            window.close()
            meleePrefix(current_weapon)
if __name__ == "__main__":
  main()

