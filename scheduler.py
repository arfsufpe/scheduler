'''
Created on 12 de jan de 2020

@author: Rodrigo
'''
from __future__ import print_function
from ortools.sat.python import cp_model
# Each volunteer has a predefined job to do and also predefined is his total number of shifts during the whole month
# for example John is a volunteer (John is a senior) and he's going to take 7 shifts during the whole month
#             since John is a senior he might be designated to work as a one of the three jobs:
#             (supervisor, report operator, team member)
#             Albert is a senior and he's going to take 5 shifts during the whole month as a (supervisor or report operator or team member)
#             Alfred is a driver and he's going to take 4 shifts during the whole month as a driver 
#             (driver can work as driver or team member)
#             same reasoning applies to the other volunteers.

# the input is a dictionary with the total of shifts during the month and the corresponding type of volunteer and its rank:
# volunteers{'Name'} = (type of volunteer, total number of shifts in a month, rank)
# volunteers{'John'} = (senior,7, 0)
# volunteers{'Albert'} = (senior, 5,10)
# volunteers{'Alfred'} = (driver,4, 12)
# volunteers{'Layse'} = (report operator assistant,5, 13)
# volunteers{'Mia'} = (supervisor assistant, 8, 51)
# volunteers{'Jim'} = (team member, 8,56)

# SHIFT (in a single shift we have the following jobs):
# 1 - seniors can work as 
#                 supervisor (required - only 1 is enough) 
#                 OR report operator (required - 1 or 2) 
#                                     2 operators is preferable for the case we have a day with 4 teams
#                                     in the case we run out of senior volunteers it is possible to have
#                                     only one report operator
#                 OR team member (in case all all others - supervisor or report operator 'chair'- are busy already)
# 2 - supervisors' assistant can work as (supervisor assistant OR team member)
#                                        (desirable - can be 0 in the case we don't have enough volunteers)
# 3 - report operators' assistant can work as (report operator assistant OR team member)
#                                         [required*](only one is necessary no matter we have 1 or 2 report operators)
# 4 - drivers can work as (drivers OR team member)
# 5 - ordinary volunteers can work as (team member)
#         TEAM
#         1 - each team is responsible for 1 of the 12 police facilities for that shift
#         2 - each team is composed of ordinary volunteers and a driver (minimum of 2 [ 1 driver + 1 team member],
#                                                                        maximum of 4 [ 1 driver + 3 team member])

# in a week there are two shifts of 12 hours each
# from Mondays to Fridays there is only the second shift (from 7pm to 7am)(no one works at shift 1)
# on Saturdays there are two shifts (one from 7am to 7pm and another from 7pm to 7am (of Sunday)(there are workers on shift 1 and 2)
# on Sundays there is only one shift from 9am to 9pm  (workers on shift 1 only)

#what to do: create a schedule for the volunteers for the whole month for all shifts for all 12 police facilities



# Facility constraints:
# there are 12 facilities which will 'place' the operation
# for the  the whole month in each facility there must be at least two teams placed on that facility every weekend(Friday, Saturday, Sunday)
# the teams should be evenly (as even as possible) distributed among the facilities during the whole month
# at Fridays, Saturdays and Sundays the total number of teams associated to the facility must be a minimum of 3 and maximum of 4 (if we have enough volunteers)
# from Monday to Thursday there must be at least on team member associated to a facility 

# Volunteers constraints
# there is a rank among seniors and the ones with higher rank must work as a supervisor
# (seniors with higher rank should work as supervisor first, then report operator and finally team member) 
# there must be at least one day off after a shift
# the shifts of every volunteer should be evenly (as even as possible)distributed for the whole month
# for every volunteer the number of shifts must be equal to the total number of shifts passed as input


# The following information is a complement of the information above (just to make it clear)
 
# There are these types of volunteers: 
# seniors - preferably can be assigned to supervisor OR report operator
#          in the case where all the supervisor's job or report operator's job are full 
#          it is possible for seniors to compose the team
#          There is a rank in the senior subgroup and the ones with higher rank must take the supervisor's job first
#          then the report operator next and finally a team member
# senior's assistant - a list of volunteers for the specific service
# report operators' assistant - a subgroup of volunteers whose job is to assist the report operator
# team members - the remaining volunteers
# team - composed of ordinary volunteers and a driver
#        each team must be assigned to one of the 12 police facilities for the day
# drivers - each team must have one driver (subgroup of volunteers allowed to drive)


def main():
    #Data.
    num_days = 29
    num_shifts = 2
    num_facilities = 12
    num_supervisors = 20
    num_supervisor_assistants = 15
    num_report_operators = 20
    num_report_operator_assistants = 15
    num_drivers = 15
    num_team_members = 100 # will be a member of a team
    
    all_days = range(num_days)
    all_shifts = range(num_shifts)
    all_facilities = range(num_facilities)
    all_supervisors = range(num_supervisors)
    all_supervisor_assistants = range(num_supervisor_assistants)
    all_report_operators = range(num_report_operators)
    all_report_operator_assistants = range(num_report_operator_assistants)
    all_drivers = range(num_drivers)
    all_team_members = range(num_team_members)
    
    # Creates the model.
    model = cp_model.CpModel()
    
    # Creates shift variables.
    # shifts[(v, d, s, j,t,f)]: volunteer 'v' works on shift 's' on day 'd' doing the 'j' job on team 't' associated to facility 'f'.
    shifts = {}
    
    
    
    


if __name__ == '__main__':
    pass