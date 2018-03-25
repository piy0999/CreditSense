from trim_data import ext_num_from_sub_grade
from trim_data import drop_emp_title
from trim_data import fill_na_annual_inc
from trim_data import drop_zip_code
from trim_data import fill_na_delinq_2yrs
from trim_data import drop_earliest_cr_line
from trim_data import fill_na_inq_last_6mths
from trim_data import fill_na_open_acc
from trim_data import fill_na_pub_rec
from trim_data import fill_na_revol_util
from trim_data import fill_na_total_acc
from trim_data import drop_out_prncp
from trim_data import drop_out_prncp_inv
from trim_data import drop_total_rec_late_fee
from trim_data import drop_recoveries
from trim_data import drop_collection_recovery_fee
from trim_data import drop_last_pymnt_d
from trim_data import drop_collections_12_mths_ex_med
from trim_data import drop_policy_code
from trim_data import drop_application_type
from trim_data import drop_acc_now_delinq
from trim_data import drop_tot_coll_amt
from trim_data import drop_tot_cur_bal
from trim_data import fill_na_total_rev_hi_lim
from trim_data import drop_url
from trim_data import drop_pymnt_plan
from trim_data import drop_issue_d
from trim_data import drop_addr_state
from trim_data import drop_last_credit_pull_d


def trim_features(loan):
    ext_num_from_sub_grade(loan)
    drop_emp_title(loan)
    fill_na_annual_inc(loan)
    drop_zip_code(loan)
    fill_na_delinq_2yrs(loan)
    drop_earliest_cr_line(loan)
    fill_na_inq_last_6mths(loan)
    fill_na_open_acc(loan)
    fill_na_pub_rec(loan)
    fill_na_revol_util(loan)
    fill_na_total_acc(loan)
    drop_pymnt_plan(loan)
    drop_url(loan)
    drop_total_rec_late_fee(loan)
    drop_out_prncp(loan)
    drop_out_prncp_inv(loan)
    drop_recoveries(loan)
    drop_collection_recovery_fee(loan)
    drop_last_pymnt_d(loan)
    drop_collections_12_mths_ex_med(loan)
    drop_policy_code(loan)
    drop_application_type(loan)
    drop_acc_now_delinq(loan)
    drop_tot_coll_amt(loan)
    drop_tot_cur_bal(loan)
    fill_na_total_rev_hi_lim(loan)
    drop_issue_d(loan)
    drop_addr_state(loan)
    drop_last_credit_pull_d(loan)
    
