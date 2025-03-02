from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Initialize a dictionary to store cell data
cell_data = {}

@app.route('/')
def index():
    # Generate column letters (A, B, C, ..., K)
    columns = [chr(65 + i) for i in range(11)]  # A to K
    rows = range(1, 24)  # Rows 1 to 23
    return render_template('index.html', columns=columns, rows=rows, cell_data=cell_data)

@app.route('/edit', methods=['POST'])
def edit_cell():
    cell_id = request.form.get('cell_id')
    new_value = request.form.get('value')
    data_type = request.form.get('data_type')  # Get the data type (text, number, date)

    # Validate input based on data type
    if data_type == 'number':
        if not new_value.isdigit():
            flash(f"Invalid input for cell {cell_id}: Must be a number.", 'error')
            return redirect(url_for('index'))
    elif data_type == 'date':
        try:
            # Validate date format (YYYY-MM-DD)
            datetime.strptime(new_value, '%Y-%m-%d')
        except ValueError:
            flash(f"Invalid input for cell {cell_id}: Must be a valid date (YYYY-MM-DD).", 'error')
            return redirect(url_for('index'))

    # Save the validated value
    cell_data[cell_id] = new_value
    flash(f"Cell {cell_id} updated successfully.", 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
