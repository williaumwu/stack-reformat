#!/usr/bin/env python

import json
import pickle
import zlib
import gzip
import base64
import hashlib
import io

def b64_encode(obj):
    """
    Encodes the input object into base64 format.

    Parameters
    ----------
    obj : Any
        The input object to be encoded.

    Returns
    -------
    str
        The base64 encoded string.

    Raises
    ------
    ValueError
        If the input object is not of a supported type.
    """

    if not isinstance(obj,str):
        obj = json.dumps(obj)

    _bytes = obj.encode('ascii')
    base64_bytes = base64.b64encode(_bytes)

    # decode the b64 binary in a b64 string
    return base64_bytes.decode('ascii')

def b64_decode(token):
    """
    Decodes the base64 encoded input string.

    Parameters
    ----------
    token : str
        The base64 encoded input string.

    Returns
    -------
    Any
        The decoded object.

    Raises
    ------
    ValueError
        If the input string is not valid base64.
    """

    base64_bytes = token.encode('ascii')
    _bytes = base64.b64decode(base64_bytes)

    try:
        _results = json.loads(_bytes.decode('ascii'))
    except:
        _results = _bytes.decode('ascii')

    return _results

def gz_pickle(fname, obj):
    """
    Saves an object to a compressed pickle file.

    Parameters
    ----------
    fname : str
        The path to the file to save the object to.
    obj : Any
        The object to save to the file.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the input object is not of a supported type.
    """
    return pickle.dump(obj=obj,
                       file=gzip.open(fname,
                                      "wb",
                                      compresslevel=3),
                       protocol=2)

def gz_upickle(fname):
    return pickle.load(gzip.open(fname,
                                 "rb"))

def zpickle(obj):
    """
    Compresses an object using the zlib library and returns the compressed data.

    Parameters
    ----------
    obj : Any
        The object to be compressed.

    Returns
    -------
    bytes
        The compressed data.

    Raises
    ------
    ValueError
        If the input object is not of a supported type.
    """
    return zlib.compress(pickle.dumps(obj,
                                      pickle.HIGHEST_PROTOCOL),
                         9)

def z_unpickle(zstr):
    return pickle.loads(zlib.decompress(zstr))

def compress(indata):
    """
    Compresses an input data using the zlib library and returns the compressed data.

    Parameters
    ----------
    indata : bytes
        The input data to be compressed.

    Returns
    -------
    bytes
        The compressed data.
    """
    outdata = zlib.compress(indata,
                            lib.Z_BEST_COMPRESSION)
    return outdata

def uncompress(zdata):
    return zlib.decompress(zdata)  

# dup 452346236234
def to_envfile(obj,b64=True):
    """
    Convert a python dictionary to an environment file format.

    Parameters:
    -----------
    obj (dict): The python dictionary to convert.
    b64 (bool, optional): Whether to base64 encode the output. Defaults to True.

    Returns:
    --------
    str: The environment file format as a string.
    """

    # Create a StringIO object
    file_buffer = io.StringIO()

    for _k,_v in list(obj.items()):
        file_buffer.write("export {}={}\n".format(_k,
                                                  _v))

    if not b64:
        return file_buffer.getvalue()
    
    base64_hash = base64.b64encode(file_buffer.getvalue().encode()).decode()
    
    # Close the StringIO object
    file_buffer.close()

    return base64_hash
