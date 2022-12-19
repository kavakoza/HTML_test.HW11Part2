import json


def load_candidates_from_json():
    with open('candidates.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)
    return data


def get_all_candidates():
    return load_candidates_from_json()


def get_candidate(id):
    for candidate in load_candidates_from_json():
        if candidate['id'] == id:
            return candidate
    return 'Not found'


def get_candidates_by_name(name):
    names = []
    for candidate in load_candidates_from_json():
        if name.lower() in candidate['name'].lower():
            names.append(candidate)
    return names


def get_candidates_by_skill(skills):
    candidates = []
    for candidate in load_candidates_from_json():
        if skills.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates

