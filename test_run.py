from space import HomePage
import time
import random
import pytest


def test_upload(browser):
    b = HomePage(browser)
    b.load()
    b.uploadFile("")
    assert 3 == 3


def test_solve(browser):
    equation = HomePage(browser)
    equation.load()
    equation.solveEquation("C:\\Users\\gaura\\Downloads\\661.png")
    assert 4 == 4


def test_solvVis(browser):
    equation = HomePage(browser)
    equation.load()
    equation.solveandVis("C:\\Users\\gaura\\Downloads\\661.png")
    assert 3 == 3


def test_vis(browser):
    graph = HomePage(browser)
    graph.load()
    graph.visualize("C:\\Users\\gaura\\Downloads\\661.png")
    assert 3 == 3
