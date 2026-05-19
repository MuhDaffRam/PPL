from datetime import datetime

class TextEditorMemento:
    def __init__(self, content: str):
        self._content = content
        self._saved_at = datetime.now()

    @property
    def content(self) -> str:
        return self._content

    @property
    def saved_at(self) -> datetime:
        return self._saved_at

class TextEditor:
    def __init__(self):
        self.content = ""


    def save(self) -> TextEditorMemento:
        print(f"[Editor] Menyimpan state: '{self.content}'")
        return TextEditorMemento(self.content)

    def restore(self, memento: TextEditorMemento):
        self.content = memento.content
        print(f"[Editor] Undo dilakukan. Kembali ke state waktu: {memento.saved_at.strftime('%H:%M:%S')}")

class HistoryManager:
    def __init__(self, editor: TextEditor):
        self._history = []  
        self._editor = editor

    def backup(self):
        self._history.append(self._editor.save())

    def undo(self):
        if not self._history:
            return

        memento = self._history.pop()
        
        self._editor.restore(memento)

if __name__ == "__main__":
    editor = TextEditor()
    history = HistoryManager(editor)

    editor.content = "Versi 1: Pemrograman berorientasi objek."
    history.backup()

    editor.content = "Versi 2: Pemrograman berorientasi objek sangat menyenangkan."
    history.backup()

    editor.content = "Versi 3: PBO membosankan dan bikin pusing (Typo/Salah ketik)."
    print(f"\nIsi teks sekarang: {editor.content}\n")

    history.undo()
    print(f"Isi teks setelah Undo 1: {editor.content}\n")

    history.undo()
    print(f"Isi teks setelah Undo 2: {editor.content}\n")
