from datetime import datetime, timedelta
import popups

def is_valid_date(date_str, date_format="%d/%m/%Y"): # need to put warning about dd/mm/yyyy format to enable proper check
    """
    Check implantation date is valid format and not empty.
    """
    try:
        datetime.strptime(date_str.strip(), date_format)
        return True
    except ValueError:
        return False

def check_lt_six_weeks(date):
    """
    Check implantation date is more than 6 weeks prior, and generate warning message if not.
    """
    today = date.today()
    if (today - date).days < 42:
        earliest_date = date + timedelta(days=42)
        popups.six_week_warning(earliest_date.strftime("%d/%m/%Y"))
        

def check_impl_date(gen, ra, rv, lv):
    """
    Check implantation date of each component in the system.
    """
    date_format="%d/%m/%Y"
    dates = []
    if is_valid_date(gen):
        gen_date_obj = datetime.strptime(gen, date_format)
        dates.append(gen_date_obj)
    if is_valid_date(ra):
        ra_date_obj = datetime.strptime(ra, date_format)
        dates.append(ra_date_obj)
    if is_valid_date(rv):
        rv_date_obj = datetime.strptime(rv, date_format)
        dates.append(rv_date_obj)
    if is_valid_date(lv):
        lv_date_obj = datetime.strptime(lv, date_format)
        dates.append(lv_date_obj)
    if len(dates) > 0:
        dates = sorted(dates, reverse=True)
        check_lt_six_weeks(dates[0])