# -*- coding: utf-8 -*-

from openerp import models, fields, api

class expense(models.Model):
	_name = 'fmsexpensess.expense'

	#add all necessary fields

	client_id = fields.Many2one('res.company', ondelete='set null', string="Client", index=True)

	projectNumber = fields.Char(string="PROJECT NUMBER", required=True)	

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
	revenuesPerGaurdCompanyAgents = fields.Char(string="Rev per Guard, Company / Agents", help="Revenue per guard, for Company / Agents")
	revenuesPerGaurdTransferDate = fields.Date(string="Revenue per Guard, Transfer Date")

	#Invoice Amount
	invoiceAmount = fields.Float(digits=(10,2), string="Invoice Amount")
	invoiceCompanyAgents = fields.Char(string="Invoice Company Agents")
	invoiceTrasferDate = fields.Date(string="Invoice Transfer Date")

	#Credit Note Amount
	creditNoteAmount = fields.Float(digits=(10,2), string="Credit Note Amount")
	creditNoteCompanyAgents = fields.Char(string="Credit Note Company Agents")
	creditNoteTransferDate = fields.Date(string="Credit Note Transfer Date")

	# compute
	totalRevenuesAmount = fields.Float(digits=(10,2), string="Total Revenues Amount")


	#Expenses 
	expDepartTicketsAmount  = fields.Float(digits=(10,2), string="")
	expDepartTicketsCompanyAgents = fields.Char(string="")
	expDepartTicketsTransferDate = fields.Date(string="")

	expHotelEmbarkAmount = fields.Float(digits=(10,2), string="")
	expHotelEmbarkCompanyAgents = fields.Char(string="")
	expHoterEmbarkTransferDate = fields.Date(string="")

	expEmbarkationAmount = fields.Float(digits=(10,2), string="")
	expEmbarkationCompanyAgents = fields.Char(string="")
	expEmbarkationTransferDate = fields.Date(string="")

	expMobilizationAmount = fields.Float(digits=(10,2), string="")
	expMobilizationCompanyAgents = fields.Char(string="")
	expMobilizationTransferDate = fields.Date(string="")

	expDemobilizationAmount = fields.Float(digits=(10,2), string="")
	expDemobilizationCompanyAgents = fields.Char(string="")
	expDemobilizationTransferDate = fields.Date(string="")

	expAgentDisembarkAmount = fields.Float(digits=(10,2), string="")
	expAgentDisembarkCompanyAgents = fields.Char(string="")
	expAgentDisembarkTransferDate = fields.Date(string="")

	expHotelDisembarkAmount = fields.Float(digits=(10,2), string="")
	expHotelDisembarkCompanyAgents = fields.Char(string="")
	expHotelDisembarkTransferDate = fields.Date(string="")

	expReturnTicketsAmount = fields.Float(digits=(10,2), string="")
	expReturnTicketsCompanyAgents = fields.Char(string="")
	expReturnTicketsTransferDate = fields.Date(string="")

	expInsuranceAmount = fields.Float(digits=(10,2), string="")
	expInsuranceCompanyAgents = fields.Char(string="")
	expInsuranceTransferDate = fields.Date(string="")

	expGuardsCostAmount = fields.Float(digits=(10,2), string="")
	expGuardsCostCompanyAgents = fields.Char(string="")
	expGuardsCostTransferDate = fields.Date(string="")

	expArmsRentalCostAmount = fields.Float(digits=(10,2), string="")
	expArmsRentalCompanyAgents = fields.Char(string="")
	expArmsRentalTransferDate = fields.Date(string="")

	expCommisionCostAmount = fields.Float(digits=(10,2), string="")
	expCommisionCompanyAgents = fields.Char(string="")
	expCommisionTransferDate = fields.Date(string="")

	# compute
	expTotalExpenses = fields.Float(digits=(15,2), string="")

	# copmute
	totalProfit = fields.Float(digits=(15,2), string="")


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
