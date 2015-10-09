# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)

class expense(models.Model):
	_name = 'fmsexpensess.expense'
	
	#add all necessary fields
	client_id = fields.Many2one('res.partner', ondelete='set null', string="Client", index=True, domain="[('is_company', '=', True), ('supplier', '=', False)]", required=True)
	#client_vessel_id = fields.Many2one("fmsexpensess.vessel", ondelete="cascade", string="Client Vessel", required=True)

	projectNumber = fields.Char(string="Project Number", required=True)	
	vesselName = fields.Char(string="Vessel Name", required=True)
	invoiceNumber = fields.Char(string="Invoice No")
	# ?
	guardTL = fields.Boolean(string="Guald Team Leader")
	creditNoteNo = fields.Char(string="Credit Note No")

	# replace gurads with relation to users!
	#arel_id = fields.Many2one('res.users')
	guard_id_one = fields.Many2one("fmsexpensess.guard", ondelete="cascade", string="Guard Name", required=True)
	guard_id_two = fields.Many2one("fmsexpensess.guard", ondelete="cascade", string="Guard Name")#, attrs="{'invisible':[('guard_id_cost_two', '=', '0.00')]}")
	guard_id_three = fields.Many2one("fmsexpensess.guard", ondelete="cascade", string="Guard Name")
	guard_id_forth = fields.Many2one("fmsexpensess.guard", ondelete="cascade", string="Guard Name")

	guard_id_cost_one = fields.Float(digits=(10,2), string="Guard Salary", required=True)
	guard_id_cost_two = fields.Float(digits=(10,2), string="Guard Salary")
	guard_id_cost_three = fields.Float(digits=(10,2), string="Guard Salary")
	guard_id_cost_forth = fields.Float(digits=(10,2), string="Guard Salary")


	# Replace later with new Model
	placeEmbark = fields.Selection([('18n', '18 NORTH'), ('suez', 'SUEZ'), ('19N', '19 NORTH'), ('galle', 'GALLE')
		, ('fujairah', 'FUJAIRAH'), ('durban', 'DURBAN'), ('Richardsbay', 'RICHARDS BAY'), ('moroni', 'MORONI')
		, ('maldives', 'MALDIVES'), ('other', 'OTHER')])

	placeDisembark = fields.Selection([('18n', '18 NORTH'), ('suez', 'SUEZ'), ('19N', '19 NORTH'), ('galle', 'GALLE')
		, ('fujairah', 'FUJAIRAH'), ('durban', 'DURBAN'), ('Richardsbay', 'RICHARDS BAY'), ('moroni', 'MORONI')
		, ('maldives', 'MALDIVES'), ('other', 'OTHER')])

	#Duration Of Trip 
	tripStartDate = fields.Date(string="Trip Start Date", required=True)
	tripEndDate = fields.Date(string="Trip End Date", required=True)

	#MOBILIZATION / DEMOBILIZATION	 	
	mobilizationDate = fields.Date(string="Mobilization Date", required=True)
	demobilizationDate = fields.Date(string="Demobilization Date", required=True)

	#REVENUES per GuardCon $		
	revenuesPerGaurdAmount = fields.Float(digits=(10,2), string="Revenues Per Guard") 
	#revenuesPerGaurdCompanyAgents = fields.Char(string="RevPerGuard Company Agents")
	#revenuesPerGaurdTransferDate = fields.Date(string="RevPerGuard Transfer Date")

	#Invoice Amount
	invoiceAmount = fields.Float(digits=(10,2), string="Invoice Amount")
	#invoiceCompanyAgents = fields.Char(string="Invoice Company Agents")
	#invoiceTrasferDate = fields.Date(string="Invoice Transfer Date")

	#Credit Note Amount
	creditNoteAmount = fields.Float(digits=(10,2), string="Credit Note Amount")
	#creditNoteCompanyAgents = fields.Char(string="Credit Note Company Agents")
	#creditNoteTransferDate = fields.Date(string="Credit Note Transfer Date")

	# compute
	totalRevenuesAmount = fields.Float(digits=(10,2), string="Total Revenues Amount", readonly=True, compute="_compute_total_revenues")

	#Expenses 
	expDepartTicketsAmount  = fields.Float(digits=(10,2), string="Depart Tickets Amount")
	expDepartTicketsTransferDate = fields.Date(string="Depart Tickets Transfer Date")
	expDepartTicketsBank = fields.Many2one("res.partner.bank", ondelete="cascade", string="Bank Account")
	expDepartTicketsCompanyAgents = fields.Many2one('res.partner', ondelete='set null', string="Company/Agents", index=True, domain="[('supplier', '=', True)]")	

	expHotelEmbarkAmount = fields.Float(digits=(10,2), string="Hotel Embark Amount")
	expHotelEmbarkTransferDate = fields.Date(string="Hotel Embark Transfer Date")
	expHotelEmbarkBank = fields.Many2one("res.partner.bank", ondelete="cascade", string="Bank Account")
	expHotelEmbarkCompanyAgents = fields.Many2one('res.partner', ondelete='set null', string="Company/Agents", index=True, domain="[('supplier', '=', True)]")	

	expEmbarkationAmount = fields.Float(digits=(10,2), string="Embarkation Amount")
	expEmbarkationTransferDate = fields.Date(string="Embarkation Transfer Date")
	expEmbarkationBank = fields.Many2one("res.partner.bank", ondelete="cascade", string="Bank Account")
	expEmbarkationCompanyAgents = fields.Many2one('res.partner', ondelete='set null', string="Company/Agents", index=True, domain="[('supplier', '=', True)]")	

	expMobilizationAmount = fields.Float(digits=(10,2), string="Mobilization Amount")
	expMobilizationTransferDate = fields.Date(string="Mobilization Transfer Date")
	expMobilizationBank = fields.Many2one("res.partner.bank", ondelete="cascade", string="Bank Account")
	expMobilizationCompanyAgents = fields.Many2one('res.partner', ondelete='set null', string="Company/Agents", index=True, domain="[('supplier', '=', True)]")	

	expDemobilizationAmount = fields.Float(digits=(10,2), string="Demobilization Amount")
	expDemobilizationTransferDate = fields.Date(string="Demobilization Transfer Date")
	expDemobilizationBank = fields.Many2one("res.partner.bank", ondelete="cascade", string="Bank Account")
	expDemobilizationCompanyAgents = fields.Many2one('res.partner', ondelete='set null', string="Company/Agents", index=True, domain="[('supplier', '=', True)]")	

	expAgentDisembarkAmount = fields.Float(digits=(10,2), string="Agent Disembark Amount")
	expAgentDisembarkTransferDate = fields.Date(string="Agent Disembark Transfer Date")
	expAgentDisembarkBank = fields.Many2one("res.partner.bank", ondelete="cascade", string="Bank Account")
	expAgentDisembarkCompanyAgents = fields.Many2one('res.partner', ondelete='set null', string="Company/Agents", index=True, domain="[('supplier', '=', True)]")	

	expHotelDisembarkAmount = fields.Float(digits=(10,2), string="Hotel Disembark Amount")
	expHotelDisembarkTransferDate = fields.Date(string="Hotel Disembark Transfer Date")
	expHotelDisembarkBank = fields.Many2one("res.partner.bank", ondelete="cascade", string="Bank Account")
	expHotelDisembarkCompanyAgents = fields.Many2one('res.partner', ondelete='set null', string="Company/Agents", index=True, domain="[('supplier', '=', True)]")	

	expReturnTicketsAmount = fields.Float(digits=(10,2), string="Return Tickets Amount")
	expReturnTicketsTransferDate = fields.Date(string="Return Tickets Transfer Date")
	expReturnTicketsBank = fields.Many2one("res.partner.bank", ondelete="cascade", string="Bank Account")
	expReturnTicketsCompanyAgents = fields.Many2one('res.partner', ondelete='set null', string="Company/Agents", index=True, domain="[('supplier', '=', True)]")	

	expInsuranceAmount = fields.Float(digits=(10,2), string="Insurance Amount")
	expInsuranceTransferDate = fields.Date(string="Insurance Transfer Date")
	expInsuranceBank = fields.Many2one("res.partner.bank", ondelete="cascade", string="Bank Account")
	expInsuranceCompanyAgents = fields.Many2one('res.partner', ondelete='set null', string="Company/Agents", index=True, domain="[('supplier', '=', True)]")	

	expGuardsCostAmount = fields.Float(digits=(10,2), string="Guards Cost Amount", readonly=True, compute="_compute_total_guards_cost" )
	#expGuardsCostTransferDate = fields.Date(string="Guards Cost Transfer Date")
	#expGuardsCostBank = fields.Many2one("res.partner.bank", ondelete="cascade", string="Bank Account")
	#expGuardsCostCompanyAgents = fields.Many2one('res.partner', ondelete='set null', string="Company/Agents", index=True, domain="[('supplier', '=', True)]")	

	expArmsRentalCostAmount = fields.Float(digits=(10,2), string="Arms Rental Cost Amount")
	expArmsRentalTransferDate = fields.Date(string="Arms Rental Transfer Date")
	expArmsRentalBank = fields.Many2one("res.partner.bank", ondelete="cascade", string="Bank Account")
	expArmsRentalCompanyAgents = fields.Many2one('res.partner', ondelete='set null', string="Company/Agents", index=True, domain="[('supplier', '=', True)]")	

	expCommisionCostAmount = fields.Float(digits=(10,2), string="Commision Cost Amount")
	expCommisionTransferDate = fields.Date(string="Commision Transfer Date")
	expCommisionBank = fields.Many2one("res.partner.bank", ondelete="cascade", string="Bank Account")
	expCommisionCompanyAgents = fields.Many2one('res.partner', ondelete='set null', string="Company/Agents", index=True, domain="[('supplier', '=', True)]")	

	# compute
	expTotalExpenses = fields.Float(digits=(15,2), string="Total Expenses", readonly=True, compute="_compute_total_expenses")

	# copmute
	totalProfit = fields.Float(digits=(15,2), string="Total Profit", readonly=True, compute="_compute_total_profit")

#	_sql_constraints = [
#		('name_unique',
#		'UNIQUE(name)',
#		"The course title must be unique"),
#	]




	def _check_date(self, cr, uid, vals, context=None):
	    for obj in self.browse(cr, uid):
			start_date = obj.tripStartDate
			end_date = obj.tripEndDate


			_logger.error("Error message FMS: %r, %r", start_date, end_date )
			if start_date and end_date:
				from_dt = datetime.strptime(start_date, '%d-%m-%Y')
				to_dt = datetime.strptime(end_date, '%d-%m-%Y')

			if to_dt < from_dt:
				return False
			return True

	#_constraints = [(_check_date, 'End Date must be greater than Start Date!', ['tripStartDate','tripEndDate']),]



	# METHODS FOR Expense
	@api.one
	@api.depends('invoiceAmount', 'creditNoteAmount')
	def _compute_total_revenues(self):
		if self.invoiceAmount or self.creditNoteAmount:
			self.totalRevenuesAmount = self.invoiceAmount - self.creditNoteAmount

	@api.one
	@api.depends('expDepartTicketsAmount','expHotelEmbarkAmount','expEmbarkationAmount','expMobilizationAmount','expDemobilizationAmount','expAgentDisembarkAmount','expHotelDisembarkAmount','expReturnTicketsAmount','expInsuranceAmount', 'expArmsRentalCostAmount','expCommisionCostAmount', 'guard_id_cost_one', 'guard_id_cost_two', 'guard_id_cost_three', 'guard_id_cost_forth')
	def _compute_total_expenses(self):
		if self.expDepartTicketsAmount or self.expHotelEmbarkAmount or self.expEmbarkationAmount or self.expMobilizationAmount or self.expDemobilizationAmount or self.expAgentDisembarkAmount or self.expHotelDisembarkAmount or self.expReturnTicketsAmount or self.expInsuranceAmount or self.expArmsRentalCostAmount or self.expCommisionCostAmount or self.guard_id_cost_one or self.guard_id_cost_two or self.guard_id_cost_three or self.guard_id_cost_forth:
			self.expTotalExpenses = self.expDepartTicketsAmount + self.expHotelEmbarkAmount + self.expEmbarkationAmount + self.expMobilizationAmount + self.expDemobilizationAmount + self.expAgentDisembarkAmount + self.expHotelDisembarkAmount + self.expReturnTicketsAmount + self.expInsuranceAmount + self.expArmsRentalCostAmount + self.expCommisionCostAmount + self.guard_id_cost_three + self.guard_id_cost_forth + self.guard_id_cost_one + self.guard_id_cost_two 

	@api.one
	@api.depends('totalRevenuesAmount', 'expTotalExpenses')
	def _compute_total_profit(self):
		if self.totalRevenuesAmount or self.expTotalExpenses:
			self.totalProfit = self.totalRevenuesAmount - self.expTotalExpenses

	@api.one
	@api.depends('guard_id_cost_one', 'guard_id_cost_two', 'guard_id_cost_three', 'guard_id_cost_forth')
	def _compute_total_guards_cost(self):
		if self.guard_id_cost_one or self.guard_id_cost_two or self.guard_id_cost_three or self.guard_id_cost_forth:
			self.expGuardsCostAmount = self.guard_id_cost_one + self.guard_id_cost_two + self.guard_id_cost_three + self.guard_id_cost_forth


	#def read_group(self, cr, uid, domain, fields, groupby, offset=0, limit=None, context=None, orderby=False, lazy=True):
	#	res = super('fmsexpensess.expense', self).read_group(cr, uid, domain, fields, groupby, offset, limit=limit, context=context, orderby=orderby, lazy=lazy)
	#	if 'totalProfit' in fields:
	#		pending_value = 0.0
	#		for line in res:
	#			pending_value += line.totalProfit
	#		line['totalProfit'] = pending_value
	#	# add more "if" for more columns
	#	return res


#	def create(self, cr, uid, vals, context=None):
#		context = context or {}
#		created_id = super(expense, self).create(cr, uid, vals, context)
#		values = (vals.get('line_ids', [])) + [(0, 0, {'expense_id': created_id})]
#		self.write(cr, uid, [created_id], {'line_ids': values}, context=context)
#		return created_id

class Guard(models.Model):
	_name = "fmsexpensess.guard"
	_order = "surname, name"

	name = fields.Char(string="Name", required=True)
	surname = fields.Char(string="Surname", required=True)
	age = fields.Integer(string="Age")
	skills = fields.Text(string="Skills - Qualifications")
	salary = fields.Float(digits=(10,2), string="Salary")
	#guard_id = fields.Many2one("fmsexpensess.expense", ondelete="cascade", string="Expense")

	def name_get(self,cr,uid,ids,context=None):
		result = {}
		for itemList in self.browse(cr,uid,ids,context=context):
			result[itemList.id] = itemList.surname + " " + itemList.name  

		return result.items()

	_sql_constraints = [
		('surname_uniq', 'unique("surname", "name")', 'Surnmane name must be unique')
	]




class Vessel(models.Model):
	_name = "fmsexpensess.vessel"

	name = fields.Char(string="Vessel Name", required=True)
	client_id = fields.Many2one('res.partner', ondelete='set null', string="Maritime Company", index=True, domain="[('is_company', '=', True), ('supplier', '=', False)]", required=True)

	def name_get(self,cr,uid,ids,context=None):
		result = {}
		for itemList in self.browse(cr,uid,ids,context=context):
			result[itemList.id] = itemList.client_id.name + " / " + itemList.name  

		return result.items()


#class ExpenseDetail(models.Model):
#	_name = 'fmsexpensess.detail'
 	
#	name = fields.Char(string="Name", required=True)
#	supplier_id = fields.Many2one("res.partner", ondelete="set null", string="Company/Agents", index=True, domain="[('supplier', '=', True)]")
#	expense_id = fields.Many2one("fmsexpensess.expense", string="Expense Detail", ondelete="cascade", select=True)
#	amountPaid = fields.Float(digits=(10,2), string="Insurance Amount")
	
	
	

# add LATER MAYBE.
#placeEmbark_id = fields.Many2one("fmsexpensess.place", ondelete="cascade", string="Embarkation Place")
#placeDisEmbark_id = fields.Many2one("fmsexpensess.place", ondelete="cascade", string="Disembarkation Place")
#class Place(models.Model)
#	_name = "fmsexpensess.place"
#	place = fields.Char(string="Port/Place", required=True)

