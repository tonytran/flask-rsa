from flask import Flask, render_template, jsonify, request
import code



app = Flask(__name__)
@app.route('/', methods= ['GET'])
def route():

    return render_template("index.html")

@app.route('/getkey', methods= ['POST'])
def result():
    if request.method == 'POST':
      result = request.form
      primeA = result["primeA"]
      primeB = result["primeB"]
      #global public, private
      public, private = code.generate_keypair(int(primeA), int(primeB))

      return render_template("index.html", public = public, private = private)
@app.route('/encrypt', methods= ['POST', 'GET'])
def encrypt():
    if (request.method == 'GET'):
        return render_template("encrypt.html")
    elif(request.method == "POST"):
        result = request.form
        public = result['pubkey']
        publicKey = strKeyToTuple(public)

        message = result['toEncrypt']
        encryptedMessage = ','.join(map(str,code.encrypt(publicKey, message)))
        #encryptedMessage = ""

        return render_template("encrypt.html", message = "Your encrypted message is: ", encrypted = encryptedMessage)

@app.route('/decrypt', methods= ['POST', 'GET'])
def decrypt():
    if (request.method == 'GET'):
        return render_template("decrypt.html")
    elif(request.method == "POST"):
        result = request.form
        private = result['privateKey']
        privateKey = strKeyToTuple(private)
        message = result['toDecrypt']

        decryptedMessage = code.decrypt(privateKey, map(int,message.split(',')))
        return render_template("decrypt.html", message = "Your decrypted message is: ", decryptedMessage = decryptedMessage)
def strKeyToTuple(string):
    vals = string.split(',')
    tup = (int(vals[0]), int(vals[1]))
    return tup

app.run(port = 80)
