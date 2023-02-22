import json
import datetime


class Note:
    def __init__(self, id, title, body, created=None, updated=None, tags=None):
        self.id = id
        self.title = title
        self.body = body
        self.created = created
        self.updated = updated
        self.tags = tags or []


class NotesManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = []
        self.load()

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                notes = json.load(f)
                self.notes = [Note(**note) for note in notes]
        except FileNotFoundError:
            pass

    def save(self):
        with open(self.filename, 'w') as f:
            notes = [note.__dict__ for note in self.notes]
            json.dump(notes, f)

    def create(self, title, body, tags=None):
        id = len(self.notes) + 1
        note = Note(id, title, body, tags=tags)
        self.notes.append(note)
        self.save()
        return note

    def read_all(self):
        return self.notes

    def read_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None

    def update(self, id, title=None, body=None, tags=None):
        note = self.read_by_id(id)
        if note:
            note.title = title or note.title
            note.body = body or note.body
            note.tags = tags or note.tags
            note.updated = datetime.now()
            self.save()
            return note
        return None

    def delete(self, id):
        note = self.read_by_id(id)
        if note:
            self.notes.remove(note)
            self.save()
            return True
        return False

    def search_by_date(self, start_date, end_date):
        notes = []
        for note in self.notes:
            if start_date <= note.created <= end_date:
                notes.append(note)
        return notes

    def search_by_tags(self, tags):
        notes = []
        for note in self.notes:
            if all(tag in note.tags for tag in tags):
                notes.append(note)
        return notes

    def search_by_keyword(self, keyword):
        notes = []
        for note in self.notes:
            if keyword in note.title or keyword in note.body:
                notes.append(note)
        return notes
