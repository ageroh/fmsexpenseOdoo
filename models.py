# -*- coding: utf-8 -*-

from openerp import models, fields, api

class expense(models.Model):
	_name = 'fmsexpensess.expense'

	#add all necessary fields

	client_id = fields.Many2one('res.company', ondelete='set null', string="Client", index=True)

	projectNumber = fields.Char(string="Project Number", required=True)	

	vesselName = fields.Char(string="Vessel Name", required=True)

	invoiceNumber = fields.Integer(string="Invoice No")

	# ?
	guardTL = fields.Boolean(string="Guald Team Leader")

	creditNoteNo = fields.Char(string="Credit Note No")

	# replace gurads with relation to users!
	#arel_id = fields.Many2one('res.users')
	guard_id_one = fields.Many2one("fmsexpensess.guard", ondelete="cascade", string="Guard Name")
	guard_id_two = fields.Many2one("fmsexpensess.guard", ondelete="cascade", string="Guard Name")
	guard_id_three = fields.Many2one("fmsexpensess.guard", ondelete="cascade", string="Guard Name")
	guard_id_forth = fields.Many2one("fmsexpensess.guard", ondelete="cascade", string="Guard Name")

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
	revenuesPerGaurdCompanyAgents = fields.Char(string="RevPerGuard Company Agents")
	revenuesPerGaurdTransferDate = fields.Date(string="RevPerGuard Transfer Date")

	#Invoice Amount
	invoiceAmount = fields.Float(digits=(10,2), string="Invoice Amount")
	invoiceCompanyAgents = fields.Char(string="Invoice Company Agents")
	invoiceTrasferDate = fields.Date(string="Invoice Transfer Date")

	#Credit Note Amount
	creditNoteAmount = fields.Float(digits=(10,2), string="Credit Note Amount")
	creditNoteCompanyAgents = fields.Char(string="Credit Note Company Agents")
	creditNoteTransferDate = fields.Date(string="Credit Note Transfer Date")

	# compute
	totalRevenuesAmount = fields.Float(digits=(10,2), string="Total Revenues Amount", readonly=True, compute="_compute_total_revenues")


	#Expenses 
	expDepartTicketsAmount  = fields.Float(digits=(10,2), string="Depart Tickets Amount")
	expDepartTicketsCompanyAgents = fields.Char(string="Depart Tickets Company Agents")
	expDepartTicketsTransferDate = fields.Date(string="Depart Tickets Transfer Date")

	expHotelEmbarkAmount = fields.Float(digits=(10,2), string="Hotel Embark Amount")
	expHotelEmbarkCompanyAgents = fields.Char(string="Hotel Embark Company Agents")
	expHoterEmbarkTransferDate = fields.Date(string="Hotel Embark Transfer Date")

	expEmbarkationAmount = fields.Float(digits=(10,2), string="Embarkation Amount")
	expEmbarkationCompanyAgents = fields.Char(string="Embarkation Company Agents")
	expEmbarkationTransferDate = fields.Date(string="Embarkation Transfer Date")

	expMobilizationAmount = fields.Float(digits=(10,2), string="Mobilization Amount")
	expMobilizationCompanyAgents = fields.Char(string="Mobilization Company Agents")
	expMobilizationTransferDate = fields.Date(string="Mobilization Transfer Date")

	expDemobilizationAmount = fields.Float(digits=(10,2), string="Demobilization Amount")
	expDemobilizationCompanyAgents = fields.Char(string="Demobilization Company Agents")
	expDemobilizationTransferDate = fields.Date(string="Demobilization Transfer Date")

	expAgentDisembarkAmount = fields.Float(digits=(10,2), string="Agent Disembark Amount")
	expAgentDisembarkCompanyAgents = fields.Char(string="Agent Disembark Company Agents")
	expAgentDisembarkTransferDate = fields.Date(string="Agent Disembark Transfer Date")

	expHotelDisembarkAmount = fields.Float(digits=(10,2), string="Hotel Disembark Amount")
	expHotelDisembarkCompanyAgents = fields.Char(string="Hotel Disembark Company Agents")
	expHotelDisembarkTransferDate = fields.Date(string="Hotel Disembark Transfer Date")

	expReturnTicketsAmount = fields.Float(digits=(10,2), string="Return Tickets Amount")
	expReturnTicketsCompanyAgents = fields.Char(string="Return Tickets Company Agents")
	expReturnTicketsTransferDate = fields.Date(string="Return Tickets Transfer Date")

	expInsuranceAmount = fields.Float(digits=(10,2), string="Insurance Amount")
	expInsuranceCompanyAgents = fields.Char(string="Insurance Company Agents")
	expInsuranceTransferDate = fields.Date(string="Insurance Transfer Date")

	expGuardsCostAmount = fields.Float(digits=(10,2), string="Guards Cost Amount")
	expGuardsCostCompanyAgents = fields.Char(string="Guards Cost Company Agents")
	expGuardsCostTransferDate = fields.Date(string="Guards Cost Transfer Date")

	expArmsRentalCostAmount = fields.Float(digits=(10,2), string="Arms Rental Cost Amount")
	expArmsRentalCompanyAgents = fields.Char(string="Arms Rental Company Agents")
	expArmsRentalTransferDate = fields.Date(string="Arms Rental Transfer Date")

	expCommisionCostAmount = fields.Float(digits=(10,2), string="Commision Cost Amount")
	expCommisionCompanyAgents = fields.Char(string="Commision Company Agents")
	expCommisionTransferDate = fields.Date(string="Commision Transfer Date")

	expBankAccount = fields.Many2one("res.partner.bank", ondelete="cascade", string="Bank Account")

	# compute
	expTotalExpenses = fields.Float(digits=(15,2), string="Total Expenses", readonly=True, compute="_compute_total_expenses")

	# copmute
	totalProfit = fields.Float(digits=(15,2), string="Total Profit", readonly=True, compute="_compute_total_profit")

	# METHODS FOR Expense
	@api.one
	@api.depends('revenuesPerGaurdAmount', 'invoiceAmount', 'creditNoteAmount')
	def _compute_total_revenues(self):
		if self.revenuesPerGaurdAmount or self.invoiceAmount or self.creditNoteAmount:
			self.totalRevenuesAmount = self.revenuesPerGaurdAmount + self.invoiceAmount + self.creditNoteAmount

	@api.one
	@api.depends('expDepartTicketsAmount','expHotelEmbarkAmount','expEmbarkationAmount','expMobilizationAmount','expDemobilizationAmount','expAgentDisembarkAmount','expHotelDisembarkAmount','expReturnTicketsAmount','expInsuranceAmount','expGuardsCostAmount','expArmsRentalCostAmount','expCommisionCostAmount')
	def _compute_total_expenses(self):
		if self.expDepartTicketsAmount or self.expHotelEmbarkAmount or self.expEmbarkationAmount or self.expMobilizationAmount or self.expDemobilizationAmount or self.expAgentDisembarkAmount or self.expHotelDisembarkAmount or self.expReturnTicketsAmount or self.expInsuranceAmount or self.expGuardsCostAmount or self.expArmsRentalCostAmount or self.expCommisionCostAmount:
			self.expTotalExpenses = self.expDepartTicketsAmount + self.expHotelEmbarkAmount + self.expEmbarkationAmount + self.expMobilizationAmount + self.expDemobilizationAmount + self.expAgentDisembarkAmount + self.expHotelDisembarkAmount + self.expReturnTicketsAmount + self.expInsuranceAmount + self.expGuardsCostAmount + self.expArmsRentalCostAmount + self.expCommisionCostAmount

	@api.one
	@api.depends('totalRevenuesAmount', 'expTotalExpenses')
	def _compute_total_profit(self):
		if self.totalRevenuesAmount or self.expTotalExpenses:
			self.totalProfit = self.totalRevenuesAmount - self.expTotalExpenses

	


class Guard(models.Model):
	_name = "fmsexpensess.guard"

	name = fields.Char(string="Name", required=True)
	surname = fields.Char(string="Surname", required=True)
	age = fields.Integer(string="Age")
	skills = fields.Text(string="Skills - Qualifications")
	#guard_id = fields.Many2one("fmsexpensess.expense", ondelete="cascade", string="Expense")


# add LATER MAYBE.
#placeEmbark_id = fields.Many2one("fmsexpensess.place", ondelete="cascade", string="Embarkation Place")
#placeDisEmbark_id = fields.Many2one("fmsexpensess.place", ondelete="cascade", string="Disembarkation Place")
#class Place(models.Model)
#	_name = "fmsexpensess.place"
#	place = fields.Char(string="Port/Place", required=True)
