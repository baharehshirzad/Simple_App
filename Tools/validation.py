import re


def validate_name(name):
      if re.match(r"^[a-zA-Z\s]{3,30}]$", name) :
          return name
      else :
             raise ValueError(" Invalid Name !!! ")


def validate_model(model):
      if re.match(r"^[a-zA-Z\s]{3,30}]$", model):
          return model
      else :
          raise ValueError(" Invalid Model !!! ")


def validate_plate(plate):
      if re.match(r"^\d{2}[A-Z]\d{3}_iran\d{2}", plate.get):
          return plate
      else :
          raise ValueError(" Invalid Plate !!! ")

