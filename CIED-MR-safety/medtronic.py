import template_generator as tplgen
import popups

"""
Create Medtronic pacemaker
Create a Medtronic lead list
GUI to select pacemaker and lead combination
Ouput whether MR conditional or not
List MR scanning conditions
"""

# web scraping to update lead lists, or at least notify us when there is a change.

single_chamber_PPM_list = ["A3SR01","X1SR01","X2SR01","X3SR01","ATSR01","W1SR01","W2SR01","W3SR01","EN1SR01","SPSR01"]
dual_chamber_ppm_list = ["A2DR01","A3DR01","X1DR01","X2DR01","X3DR01","ATDR01","ATDRL1","ATDRS1","W1DR01","W2DR01","W3DR01","EMDR01","ENDRO1","RVDR01","SPDR01","SPDRL1"]

all_PPM_lead_list = ["3830","4076","5076","4074","4574","5086MRI","5054","5554"]


# functions to check CIED model and leads
def CIED_single_chamber_ppm(recipient, pt_name, mrn, dob, referral, gen, rv, gen_impl_date, rv_impl_date, ref):
    if gen in single_chamber_PPM_list:
            single_chamber_PPM_check(recipient, pt_name, mrn, dob, referral, gen, rv, gen_impl_date, rv_impl_date, ref)
    else:
        single_chamber_PPM_not_cond(recipient, pt_name, mrn, dob, referral, gen, rv, gen_impl_date, rv_impl_date, ref, reason="Generator not conditional")
        popups.not_cond_warning()


def CIED_dual_chamber_ppm(recipient, pt_name, mrn, dob, referral, gen, ra, rv, gen_impl_date, ra_impl_date, rv_impl_date, ref):
    if gen in dual_chamber_ppm_list:
            dual_chamber_PPM_check(recipient, pt_name, mrn, dob, referral, gen, ra, rv, gen_impl_date, ra_impl_date, rv_impl_date, ref)
    else:
        dual_chamber_PPM_not_cond(recipient, pt_name, mrn, dob, referral, gen, ra, rv, gen_impl_date, ra_impl_date, rv_impl_date, ref, reason="Generator not conditional")
        popups.not_cond_warning()

def single_chamber_PPM_not_cond(recipient, pt_name, mrn, dob, referral, gen, rv, gen_impl_date, rv_impl_date, ref, reason):
    tplgen.generate_email_reject_single_chamber_PPM(recipient, pt_name, mrn, dob, referral, gen, rv, gen_impl_date, rv_impl_date, ref, reason)
    tplgen.generate_soliton_reject_single_chamber_ppm(pt_name, mrn, gen, rv, gen_impl_date, rv_impl_date, ref, reason) 

def dual_chamber_PPM_not_cond(recipient, pt_name, mrn, dob, referral, gen, ra, rv, gen_impl_date, ra_impl_date, rv_impl_date, ref, reason):
    tplgen.generate_email_reject_dual_chamber_PPM(recipient, pt_name, mrn, dob, referral, gen, ra, rv, gen_impl_date, ra_impl_date, rv_impl_date, ref, reason)
    tplgen.generate_soliton_reject_dual_chamber_PPM(pt_name, mrn, gen, ra, rv, gen_impl_date, ra_impl_date, rv_impl_date, ref, reason)   

# functions for individual generator types
def dual_chamber_PPM_check(recipient, pt_name, mrn, dob, referral, gen, ra, rv, gen_impl_date, ra_impl_date, rv_impl_date, ref):
    if ra in all_PPM_lead_list and rv in all_PPM_lead_list and ra != "3830" and rv != "3830":
        tplgen.generate_email_dual_chamber_PPM(recipient, pt_name, mrn, dob, referral, gen, ra, rv, gen_impl_date, ra_impl_date, rv_impl_date, ref, template='templates/dual_chamber_PPM_email_template.docx')
        tplgen.generate_soliton_dual_chamber_PPM(pt_name, mrn, gen, ra, rv, gen_impl_date, ra_impl_date, rv_impl_date, ref, template='templates/dual_chamber_PPM_soliton_template.docx')
    elif ra in all_PPM_lead_list and rv in all_PPM_lead_list:
        if ra == "3830" or rv == "3830":
            popups.lead_3830_warning()
    elif ra not in all_PPM_lead_list:
        dual_chamber_PPM_not_cond(recipient, pt_name, mrn, dob, referral, gen, ra, rv, gen_impl_date, ra_impl_date, rv_impl_date, ref, reason="RA lead not conditional")
        popups.not_cond_warning()
    elif rv not in all_PPM_lead_list:
        dual_chamber_PPM_not_cond(recipient, pt_name, mrn, dob, referral, gen, ra, rv, gen_impl_date, ra_impl_date, rv_impl_date, ref, reason="RV lead not conditional")
        popups.not_cond_warning()
    else:
        popups.error_in_check()

def single_chamber_PPM_check(recipient, pt_name, mrn, dob, referral, gen, rv, gen_impl_date, rv_impl_date, ref):
    if rv in all_PPM_lead_list and rv!= "3830":
        tplgen.generate_email_single_chamber_PPM(recipient, pt_name, mrn, dob, referral, gen, rv, gen_impl_date, rv_impl_date, ref, template='templates/single_chamber_PPM_email_template.docx') 
        tplgen.generate_soliton_single_chamber_PPM(pt_name, mrn, gen, rv, gen_impl_date, rv_impl_date, ref, template='templates/single_chamber_PPM_soliton_template.docx')
    elif rv in all_PPM_lead_list:
        if rv == "3830":
            popups.lead_3830_warning()
    else:
        popups.not_cond_warning()
        single_chamber_PPM_not_cond(recipient, pt_name, mrn, dob, referral, gen, rv, gen_impl_date, rv_impl_date, ref, reason="RV lead not conditional")








