"""
Module: decision_tree.py
Implementasi Binary Decision Tree untuk logika game Akinator.
"""

from characters import get_all_characters, get_attributes


class TreeNode:
    """Representasi satu simpul dalam Binary Decision Tree."""

    def __init__(self, attribute=None, yes_branch=None, no_branch=None, character=None):
        self.attribute = attribute      # Atribut/pertanyaan di simpul ini
        self.yes_branch = yes_branch    # Cabang jika jawaban "Ya"
        self.no_branch = no_branch      # Cabang jika jawaban "Tidak"
        self.character = character      # Nama karakter (hanya di simpul daun)

    def is_leaf(self):
        return self.character is not None


class DecisionTree:
    """Binary Decision Tree yang dibangun dari data karakter."""

    def __init__(self):
        self.root = None
        self._build()

    # ------------------------------------------------------------------ #
    #  Pembangunan pohon                                                   #
    # ------------------------------------------------------------------ #

    def _build(self):
        characters = get_all_characters()
        attributes = get_attributes()
        self.root = self._build_recursive(characters, attributes)

    def _gini_impurity(self, characters):
        """Menghitung Gini Impurity dari sekumpulan karakter."""
        if not characters:
            return 0.0
        total = len(characters)
        counts = {}
        for c in characters:
            counts[c["name"]] = counts.get(c["name"], 0) + 1
        return 1.0 - sum((v / total) ** 2 for v in counts.values())

    def _best_split(self, characters, attributes):
        """Memilih atribut terbaik untuk pemisahan berdasarkan Gini gain."""
        best_attr = None
        best_gain = -1
        base_impurity = self._gini_impurity(characters)

        for attr in attributes:
            yes_group = [c for c in characters if c.get(attr)]
            no_group  = [c for c in characters if not c.get(attr)]
            if not yes_group or not no_group:
                continue
            total = len(characters)
            weighted = (len(yes_group) / total) * self._gini_impurity(yes_group) + \
                       (len(no_group)  / total) * self._gini_impurity(no_group)
            gain = base_impurity - weighted
            if gain > best_gain:
                best_gain = gain
                best_attr = attr

        return best_attr

    def _build_recursive(self, characters, attributes):
        """Membangun pohon secara rekursif."""
        # Kondisi berhenti: hanya 1 karakter atau tidak ada atribut tersisa
        if len(characters) == 1:
            return TreeNode(character=characters[0]["name"])

        if not characters:
            return TreeNode(character="Tidak diketahui")

        if not attributes:
            # Ambil karakter dengan nama pertama secara alfabetis sebagai tebakan
            best_guess = sorted(characters, key=lambda c: c["name"])[0]["name"]
            return TreeNode(character=best_guess)

        # Pilih atribut terbaik
        best_attr = self._best_split(characters, attributes)

        if best_attr is None:
            best_guess = sorted(characters, key=lambda c: c["name"])[0]["name"]
            return TreeNode(character=best_guess)

        remaining_attrs = [a for a in attributes if a != best_attr]
        yes_chars = [c for c in characters if c.get(best_attr)]
        no_chars  = [c for c in characters if not c.get(best_attr)]

        yes_branch = self._build_recursive(yes_chars, remaining_attrs) if yes_chars else TreeNode(character="Tidak diketahui")
        no_branch  = self._build_recursive(no_chars,  remaining_attrs) if no_chars  else TreeNode(character="Tidak diketahui")

        return TreeNode(attribute=best_attr, yes_branch=yes_branch, no_branch=no_branch)

    # ------------------------------------------------------------------ #
    #  Traversal (rekursif)                                               #
    # ------------------------------------------------------------------ #

    def traverse(self, node, ask_callback):
        """
        Menelusuri pohon secara rekursif.
        ask_callback(attribute) → True/False sesuai jawaban user.
        Mengembalikan nama karakter yang ditebak.
        """
        if node.is_leaf():
            return node.character

        answer = ask_callback(node.attribute)
        if answer:
            return self.traverse(node.yes_branch, ask_callback)
        else:
            return self.traverse(node.no_branch, ask_callback)

    def start_traversal(self, ask_callback):
        """Entry point traversal dari root."""
        return self.traverse(self.root, ask_callback)

    # ------------------------------------------------------------------ #
    #  Debug / visualisasi                                                #
    # ------------------------------------------------------------------ #

    def print_tree(self, node=None, depth=0, branch="ROOT"):
        """Mencetak struktur pohon ke terminal (untuk debug)."""
        if node is None:
            node = self.root
        indent = "  " * depth
        if node.is_leaf():
            print(f"{indent}[{branch}] DAUN → {node.character}")
        else:
            print(f"{indent}[{branch}] PERTANYAAN: {node.attribute}?")
            self.print_tree(node.yes_branch, depth + 1, "YA")
            self.print_tree(node.no_branch,  depth + 1, "TIDAK")
