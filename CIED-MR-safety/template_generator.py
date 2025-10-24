from docxtpl import DocxTemplate
import jinja2
import popups

# Email and note for dual chamber PPM    
def generate_email_dual_chamber_PPM(recipient, pt_name, mrn, dob, referral, gen, ra, rv, gen_impl_date, ra_impl_date, rv_impl_date, ref, template):
    """
    Generate email from template for MR Conditional dual chamber PPM.
    """
    tpl = DocxTemplate(template)
    print("MR Conditional PPM and lead system")
    context = {
        "email_recipient": recipient,
        "patient_name": pt_name,
        "MRN": mrn,
        "DoB": dob,
        "referred_for": referral,
        "CIED_model": gen,
        "RA_Lead": ra,
        "RV_Lead": rv,
        "gen_implantation_date": gen_impl_date,
        "ra_implantation_date": ra_impl_date,
        "rv_implantation_date": rv_impl_date,
        "MRSCL_ref": ref
    }
    jinja_env = jinja2.Environment(autoescape=True)
    tpl.render(context, jinja_env)
    tpl.save('outputs/email_created.docx')
    popups.conditional_message()

def generate_soliton_dual_chamber_PPM(pt_name, mrn, gen, ra, rv, gen_impl_date, ra_impl_date, rv_impl_date, ref, template):
    """
    Generate soliton note from template for MR Conditional dual chamber PPM.
    """
    tpl = DocxTemplate(template)
    context = {
        "patient_name": pt_name,
        "MRN": mrn,
        "CIED_model": gen,
        "RA_Lead": ra,
        "RV_Lead": rv,
        "gen_implantation_date": gen_impl_date,
        "ra_implantation_date": ra_impl_date,
        "rv_implantation_date": rv_impl_date,
        "MRSCL_ref": ref
    }
    jinja_env = jinja2.Environment(autoescape=True)
    tpl.render(context, jinja_env)
    tpl.save('outputs/soliton_created.docx')


# Email and note for single chamber PPM    
def generate_email_single_chamber_PPM(recipient, pt_name, mrn, dob, referral, gen, rv, gen_impl_date, rv_impl_date, ref, template):
    """
    Generate email from template for MR Conditional single chamber PPM.
    """
    tpl = DocxTemplate(template)
    context = {
        "email_recipient": recipient,
        "patient_name": pt_name,
        "MRN": mrn,
        "DoB": dob,
        "referred_for": referral,
        "CIED_model": gen,
        "RV_Lead": rv,
        "gen_implantation_date": gen_impl_date,
        "rv_implantation_date": rv_impl_date,
        "MRSCL_ref": ref
    }
    jinja_env = jinja2.Environment(autoescape=True)
    tpl.render(context, jinja_env)
    tpl.save('outputs/email_created.docx')
    popups.conditional_message()

def generate_soliton_single_chamber_PPM(pt_name, mrn, gen, rv, gen_impl_date, rv_impl_date, ref, template):
    """
    Generate soliton note from template for MR Conditional single chamber PPM.
    """
    tpl = DocxTemplate(template)
    context = {
        "patient_name": pt_name,
        "MRN": mrn,
        "CIED_model": gen,
        "RV_Lead": rv,
        "gen_implantation_date": gen_impl_date,
        "rv_implantation_date": rv_impl_date,
        "MRSCL_ref": ref
    }
    jinja_env = jinja2.Environment(autoescape=True)
    tpl.render(context, jinja_env)
    tpl.save('outputs/soliton_created.docx')
 

# Rejection email and note
def generate_email_reject_single_chamber_PPM(recipient, pt_name, mrn, dob, referral, gen, rv, gen_impl_date, rv_impl_date, ref, reason):
    """
    Generate rejection email from template for non-conditional single chamber PPM. 
    """
    if reason == "Generator not conditional":
        tpl = DocxTemplate("templates/single_chamber_PPM_email_reject_gen_template.docx")
    elif reason == "RV lead not conditional":
        tpl = DocxTemplate("templates/single_chamber_PPM_email_reject_RV_template.docx")
    context = {
        "email_recipient": recipient,
        "patient_name": pt_name,
        "MRN": mrn,
        "DoB": dob,
        "referred_for": referral,
        "CIED_model": gen,
        "RV_Lead": rv,
        "gen_implantation_date": gen_impl_date,
        "rv_implantation_date": rv_impl_date,
        "MRSCL_ref": ref
    }
    jinja_env = jinja2.Environment(autoescape=True)
    tpl.render(context, jinja_env)
    tpl.save('outputs/email_created.docx')

def generate_soliton_reject_single_chamber_ppm(pt_name, mrn, gen, rv, gen_impl_date, rv_impl_date, ref, reason):
    """
    Generate rejection soliton note from template for non-conditional single chamber PPM. 
    """
    if reason == "Generator not conditional":
        tpl = DocxTemplate("templates/single_chamber_PPM_soliton_reject_gen_template.docx")
    elif reason == "RV lead not conditional":
        tpl = DocxTemplate("templates/single_chamber_PPM_soliton_reject_RV_template.docx")
    context = {
        "patient_name": pt_name,
        "MRN": mrn,
        "CIED_model": gen,
        "RV_Lead": rv,
        "gen_implantation_date": gen_impl_date,
        "rv_implantation_date": rv_impl_date,
        "MRSCL_ref": ref
    }
    jinja_env = jinja2.Environment(autoescape=True)
    tpl.render(context, jinja_env)
    tpl.save('outputs/soliton_created.docx')


def generate_email_reject_dual_chamber_PPM(recipient, pt_name, mrn, dob, referral, gen, ra, rv, gen_impl_date, ra_impl_date, rv_impl_date, ref, reason):
    """
    Generate rejection email from template for non-conditional dual chamber PPM. 
    """
    if reason == "Generator not conditional":
        tpl = DocxTemplate("templates/dual_chamber_PPM_email_reject_gen_template.docx")
    elif reason == "RA lead not conditional":
        tpl = DocxTemplate("templates/dual_chamber_PPM_email_reject_RA_template.docx")
    elif reason == "RV lead not conditional":
        tpl = DocxTemplate("templates/dual_chamber_PPM_email_reject_RV_template.docx")
    context = {
        "email_recipient": recipient,
        "patient_name": pt_name,
        "MRN": mrn,
        "DoB": dob,
        "referred_for": referral,
        "CIED_model": gen,
        "RA_Lead": ra,
        "RV_Lead": rv,
        "gen_implantation_date": gen_impl_date,
        "ra_implantation_date": ra_impl_date,
        "rv_implantation_date": rv_impl_date,
        "MRSCL_ref": ref
    }
    jinja_env = jinja2.Environment(autoescape=True)
    tpl.render(context, jinja_env)
    tpl.save('outputs/email_created.docx')

def generate_soliton_reject_dual_chamber_PPM(pt_name, mrn, gen, ra, rv, gen_impl_date, ra_impl_date, rv_impl_date, ref, reason):
    """
    Generate rejection soliton note from template for non-conditional dual chamber PPM. 
    """
    if reason == "Generator not conditional":
        tpl = DocxTemplate("templates/dual_chamber_PPM_soliton_reject_gen_template.docx")
    elif reason == "RA lead not conditional":
        tpl = DocxTemplate("templates/dual_chamber_PPM_soliton_reject_RA_template.docx")
    elif reason == "RV lead not conditional":
        tpl = DocxTemplate("templates/dual_chamber_PPM_soliton_reject_RV_template.docx")
    context = {
        "patient_name": pt_name,
        "MRN": mrn,
        "CIED_model": gen,
        "RA_Lead": ra,
        "RV_Lead": rv,
        "gen_implantation_date": gen_impl_date,
        "ra_implantation_date": ra_impl_date,
        "rv_implantation_date": rv_impl_date,
        "MRSCL_ref": ref
    }
    jinja_env = jinja2.Environment(autoescape=True)
    tpl.render(context, jinja_env)
    tpl.save('outputs/soliton_created.docx')