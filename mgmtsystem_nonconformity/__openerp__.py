# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Management System - Nonconformity",
    "version": "9.0.1.0.0",
    "author": "Savoir-faire Linux,Odoo Community Association (OCA)",
    "website": "http://www.savoirfairelinux.com",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": [
        'mgmtsystem_action',
        'document_page_procedure',
    ],
    "data": [
        'security/ir.model.access.csv',
        'security/mgmtsystem_nonconformity_security.xml',
        'views/mgmtsystem_nonconformity.xml',
        'views/mgmtsystem_nonconformity_stage.xml',
        'views/mgmtsystem_origin.xml',
        'views/mgmtsystem_cause.xml',
        'views/mgmtsystem_severity.xml',
        'views/mgmtsystem_action.xml',
        'reports/mgmtsystem_nonconformity_report.xml',
        'data/sequence.xml',
        'data/mgmtsystem_nonconformity_severity.xml',
        'data/mgmtsystem_nonconformity_origin.xml',
        'data/mgmtsystem_nonconformity_cause.xml',
        'data/mgmtsystem_nonconformity_stage.xml',
        'data/mail_message_subtype.xml',
    ],
    "demo": [
        "demo/mgmtsystem_nonconformity_origin.xml",
        "demo/mgmtsystem_nonconformity_cause.xml",
        "demo/mgmtsystem_nonconformity.xml",
    ],
    'installable': True,
}
