import json

def json_to_python(obj):
    return json.loads(obj.encode()) if obj is not None else None

def list_obj_to_python(obj, type):
    if obj is None:
        return None
    result = []
    iterator = obj.iterator()
    while iterator.hasNext():
        val = iterator.next()
        result.append(type(json.loads(val.encode())) if val is not None else None)
    return result

def list_to_json(obj):
    return jvm.io.vertx.core.json.JsonArray(json.dumps(obj)) if obj is not None else None

def dict_to_json(obj):
    return jvm.io.vertx.core.json.JsonObject(json.dumps(obj)) if obj is not None else None

def python_to_java(obj):
    if obj is None:
        return None
    if isinstance(obj, dict):
        return dict_to_json(obj)
    elif isinstance(obj, list):
        return list_to_json(obj)
    return obj

def java_to_python(obj):
    if obj is None:
        return None
    elif isinstance(obj, (jvm.io.vertx.core.json.JsonObject, jvm.io.vertx.core.json.JsonArray)):
        return json_to_python(obj)
    else:
        return obj
