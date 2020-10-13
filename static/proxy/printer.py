from flask import Flask
from flask import jsonify
from flask import request
import cups
from flask_cors import CORS
import os
import logging
_logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

@app.route('/dotmatrix/print', methods=['POST'])
def dotmatrix_print():
    _logger.warning(1)
    conn = cups.Connection()
    printers = conn.getPrinters()
    for printer in printers:
        pass
    printer_data = request.form['printer_data']
    os.system('echo "%s" | lpr -l' % (printer_data, ))
    return jsonify({'status': 'OK'})

