from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = '92f09598141f38cd1ce84bc25737294f56a9c9dc8c87179485234135757f5eb2'