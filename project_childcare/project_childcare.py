# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2015 Vertel AB (<http://vertel.se>).
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
from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp import http
from openerp.http import request
from openerp import SUPERUSER_ID
from datetime import datetime
import werkzeug
import pytz

class website_childcare(http.Controller):
        
    @http.route(['/childcare/<model("res.users"):user>', ], type='http', auth="user", website=True)
    def childcare_loggedin(self, user=False, **post):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
        return request.render('project_childcare.fee_calc',{})
        
    @http.route(['/childcare'], type='http', auth="none", website=True)
    def childcare_anon(self, **post):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
        return request.render('project_childcare.fee_calc', {})
        
        