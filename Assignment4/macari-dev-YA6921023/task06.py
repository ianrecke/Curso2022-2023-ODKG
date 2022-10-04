# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12nUaD1TBMkUc8F2n4_EHLwLJnobVPvBJ

**Task 06: Modifying RDF(s)**
"""

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.1: Create a new class named "University"**

"""

# TO DO
# Visualize the results
ns = Namespace("http://somewhere#")
g.add((ns.University, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

# TO DO
# Visualize the results
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

# TO DO
# Visualize the results
g.add((ns.JaneSmith, RDF.type, ns.Researcher))

for s, p, o in g:
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**"""

# TO DO
# Visualize the results
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")
g.add((ns.JaneSmith, vcard.FN, Literal("Jane Smith", datatype=XSD.string)))
g.add((ns.JaneSmith, vcard.Given, Literal("Jane", datatype=XSD.string)))
g.add((ns.JaneSmith, vcard.Family, Literal("Smith", datatype=XSD.string)))

for s, p, o in g: 
    print(s,p,o)

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

# TO DO
# Visualize the results
g.add((ns.JohnSmith, vcard.FN, Literal("John Smith", datatype=XSD.string)))
g.add((ns.JohnSmith, vcard.Given, Literal("John", datatype=XSD.string)))
g.add((ns.JohnSmith, vcard.Family, Literal("Smith", datatype=XSD.string)))
g.add((ns.UPM, RDF.type, ns.University))
g.add((ns.JohnSmith, ns.WorksAt, ns.UPM))

for s, p, o in g:
    print(s,p,o)
