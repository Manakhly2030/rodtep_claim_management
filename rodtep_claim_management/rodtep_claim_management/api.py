import frappe

@frappe.whitelist()
def si_on_submit(self, method):
	create_jv(self)
	
@frappe.whitelist()
def si_on_cancel(self, method):
	cancel_jv(self, method)

def create_jv(self):
		if self.total_duty_drawback:
			drawback_receivable_account = frappe.db.get_value("Company", { "company_name": self.company}, "duty_drawback_receivable_account")
			drawback_income_account = frappe.db.get_value("Company", { "company_name": self.company}, "duty_drawback_income_account")
			drawback_cost_center = frappe.db.get_value("Company", { "company_name": self.company}, "duty_drawback_cost_center")
			if not drawback_receivable_account:
				frappe.throw(_("Set Duty Drawback Receivable Account in Company"))
			elif not drawback_income_account:
				frappe.throw(_("Set Duty Drawback Income Account in Company"))
			elif not drawback_cost_center:
				frappe.throw(_("Set Duty Drawback Cost Center in Company"))
			else:
				jv = frappe.new_doc("Journal Entry")
				jv.voucher_type = "Duty Drawback Entry"
				jv.posting_date = self.posting_date
				jv.company = self.company
				jv.cheque_no = self.name
				jv.cheque_date = self.posting_date
				jv.user_remark = "Duty draw back against " + self.name + " for " + self.customer
				jv.append("accounts", {
					"account": drawback_receivable_account,
					"cost_center": drawback_cost_center,
					"debit_in_account_currency": self.total_duty_drawback
				})
				jv.append("accounts", {
					"account": drawback_income_account,
					"cost_center": drawback_cost_center,
					"credit_in_account_currency": self.total_duty_drawback
				})
				try:
					jv.save(ignore_permissions=True)
					jv.submit()
				except Exception as e:
					frappe.throw(str(e))
				else:
					self.db_set('duty_drawback_',jv.name)

		if self.get('total_meis'):
			meis_receivable_account = frappe.db.get_value("Company", { "company_name": self.company}, "meis_receivable_account")
			meis_income_account = frappe.db.get_value("Company", { "company_name": self.company}, "meis_income_account")
			meis_cost_center = frappe.db.get_value("Company", { "company_name": self.company}, "meis_cost_center")
			if not meis_receivable_account:
				frappe.throw(_("Set RODTEP Receivable Account in Company"))
			elif not meis_income_account:
				frappe.throw(_("Set RODTEP Income Account in Company"))
			elif not meis_cost_center:
				frappe.throw(_("Set RODTEP Cost Center in Company"))
			else:
				meis_jv = frappe.new_doc("Journal Entry")
				meis_jv.voucher_type = "RODTEP Entry"
				meis_jv.posting_date = self.posting_date
				meis_jv.company = self.company
				meis_jv.cheque_no = self.name
				meis_jv.cheque_date = self.posting_date
				meis_jv.user_remark = "RODTEP against " + self.name + " for " + self.customer
				meis_jv.append("accounts", {
					"account": meis_receivable_account,
					"cost_center": meis_cost_center,
					"debit_in_account_currency": self.total_meis
				})
				meis_jv.append("accounts", {
					"account": meis_income_account,
					"cost_center": meis_cost_center,
					"credit_in_account_currency": self.total_meis
				})
				
				try:
					meis_jv.save(ignore_permissions=True)
					meis_jv.submit()
					
				except Exception as e:
					frappe.throw(str(e))
				else:
					self.db_set('rodtep_jv',meis_jv.name)
def cancel_jv(self, method):
	if self.duty_drawback_jv:
		jv = frappe.get_doc("Journal Entry", self.duty_drawback_jv)
		jv.cancel()
		self.duty_drawback_jv = ''
	if self.get('meis_jv'):
		jv = frappe.get_doc("Journal Entry", self.meis_jv)
		jv.cancel()
		self.meis_jv = ''