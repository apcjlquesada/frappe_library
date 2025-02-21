# Copyright (c) 2024, Jose Quesada and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LibraryMember(Document):
    #this method will run every time a document is saved
    def before_insert(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'
