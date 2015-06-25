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
	expDepartTicketsAmount  = fields.Float(digits=(10,2), string="expDepartTicketsAmount")
	expDepartTicketsCompanyAgents = fields.Char(string="expDepartTicketsCompanyAgents")
	expDepartTicketsTransferDate = fields.Date(string="expDepartTicketsTransferDate")

	expHotelEmbarkAmount = fields.Float(digits=(10,2), string="expHotelEmbarkAmount")
	expHotelEmbarkCompanyAgents = fields.Char(string="expHotelEmbarkCompanyAgents")
	expHoterEmbarkTransferDate = fields.Date(string="expHoterEmbarkTransferDate")

	expEmbarkationAmount = fields.Float(digits=(10,2), string="expEmbarkationAmount")
	expEmbarkationCompanyAgents = fields.Char(string="expEmbarkationCompanyAgents")
	expEmbarkationTransferDate = fields.Date(string="expEmbarkationTransferDate")

	expMobilizationAmount = fields.Float(digits=(10,2), string="expMobilizationAmount")
	expMobilizationCompanyAgents = fields.Char(string="expMobilizationCompanyAgents")
	expMobilizationTransferDate = fields.Date(string="expMobilizationTransferDate")

	expDemobilizationAmount = fields.Float(digits=(10,2), string="expDemobilizationAmount")
	expDemobilizationCompanyAgents = fields.Char(string="expDemobilizationCompanyAgents")
	expDemobilizationTransferDate = fields.Date(string="expDemobilizationTransferDate")

	expAgentDisembarkAmount = fields.Float(digits=(10,2), string="expAgentDisembarkAmount")
	expAgentDisembarkCompanyAgents = fields.Char(string="expAgentDisembarkCompanyAgents")
	expAgentDisembarkTransferDate = fields.Date(string="expAgentDisembarkTransferDate")

	expHotelDisembarkAmount = fields.Float(digits=(10,2), string="expHotelDisembarkAmount")
	expHotelDisembarkCompanyAgents = fields.Char(string="expHotelDisembarkCompanyAgents")
	expHotelDisembarkTransferDate = fields.Date(string="expHotelDisembarkTransferDate")

	expReturnTicketsAmount = fields.Float(digits=(10,2), string="expReturnTicketsAmount")
	expReturnTicketsCompanyAgents = fields.Char(string="expReturnTicketsCompanyAgents")
	expReturnTicketsTransferDate = fields.Date(string="expReturnTicketsTransferDate")

	expInsuranceAmount = fields.Float(digits=(10,2), string="expInsuranceAmount")
	expInsuranceCompanyAgents = fields.Char(string="expInsuranceCompanyAgents")
	expInsuranceTransferDate = fields.Date(string="expInsuranceTransferDate")

	expGuardsCostAmount = fields.Float(digits=(10,2), string="expGuardsCostAmount")
	expGuardsCostCompanyAgents = fields.Char(string="expGuardsCostCompanyAgents")
	expGuardsCostTransferDate = fields.Date(string="expGuardsCostTransferDate")

	expArmsRentalCostAmount = fields.Float(digits=(10,2), string="expArmsRentalCostAmount")
	expArmsRentalCompanyAgents = fields.Char(string="expArmsRentalCompanyAgents")
	expArmsRentalTransferDate = fields.Date(string="expArmsRentalTransferDate")

	expCommisionCostAmount = fields.Float(digits=(10,2), string="expCommisionCostAmount")
	expCommisionCompanyAgents = fields.Char(string="expCommisionCompanyAgents")
	expCommisionTransferDate = fields.Date(string="expCommisionTransferDate")

	# compute
	expTotalExpenses = fields.Float(digits=(15,2), string="expTotalExpenses")

	# copmute
	totalProfit = fields.Float(digits=(15,2), string="totalProfit")


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
