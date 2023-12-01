from cassandra.cluster import Cluster
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

cluster = Cluster()
session = cluster.connect('jobs')