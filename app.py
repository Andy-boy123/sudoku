# app.py
from flask import Flask, render_template, jsonify
from sudoku_generator import generate_sudoku
import threading

app = Flask(__name__)

# 创建一个锁，用于确保在多线程中生成数独时不会出现竞争条件
sudoku_lock = threading.Lock()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate_sudoku')
def get_sudoku():
    # 使用锁以确保多个线程不会同时生成数独
    with sudoku_lock:
        sudoku_data = generate_sudoku()
    return jsonify(sudoku_data)


if __name__ == '__main__':
    app.run(debug=True)
