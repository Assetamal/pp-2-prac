import json

def merge_patch(source, patch):
    for key in patch:
        if patch[key] is None:
            # remove key if exists
            source.pop(key, None)
        elif key in source and isinstance(source[key], dict) and isinstance(patch[key], dict):
            # recursive merge
            merge_patch(source[key], patch[key])
        else:
            # add or replace
            source[key] = patch[key]
    return source


# Read input
source = json.loads(input())
patch = json.loads(input())

result = merge_patch(source,patch)

print(json.dumps(result, separators=(',', ':'), sort_keys=True))