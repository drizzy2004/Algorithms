'''
ResidencyMatch.py

This algorithm operates by reading an input file of the form

[residents | hospitals] preference 1, preference 2, preference 3, preference 4, ...

Any whitespace occurring in the input files is stripped off.

Usage:

    python ResidencyMatch.py [residents preference file] [hospitals preference file]

[Drake, Landon]

'''

import sys
import csv

class ResidencyMatch:

    # behaves like a constructor
    def __init__(self):
        '''
        Think of
        
            unmatchedHospitals
            residentsMappings
            hospitalsMappings
            matches
            
        as being instance data for your class.
        
        Whenever you want to refer to instance data, you must
        prepend it with 'self.<instance data>'
        '''
        
        # list of unmatched hospitals
        self.unmatchedHospitals = [ ]

        # list of unmatched residents
        self.unmatchedResidents = [ ]
        
        # dictionaries representing preferences mappings
        
        self.residentsMappings = { }
        self.hospitalsMappings = { }
        
        # dictionary of matches where mapping is resident:hospital
        self.matches = { }
        
        # read in the preference files
        
        '''
        This constructs a dictionary mapping a resident to a list of hospitals in order of preference
        '''
        
        prefsReader = csv.reader(open (sys.argv[1],'r'), delimiter = ',')
        for row in prefsReader:
            resident = row[0].strip()

             # all hospitals are initially unmatched
            self.unmatchedResidents.append(resident)

            # maps a resident to a list of preferences
            self.residentsMappings[resident] = [x.strip() for x in row[1:]]
            
            # initially have each resident as unmatched
            self.matches[resident] = None
        
        '''
        This constructs a dictionary mapping a hospital to a list of residents in order of preference
        '''
        
        prefsReader = csv.reader(open (sys.argv[2],'r'), delimiter = ',')
        for row in prefsReader:
            
            hospital = row[0].strip()
            
            # all hospitals are initially unmatched
            self.unmatchedHospitals.append(hospital)
            
            # maps a resident to a list of preferences
            self.hospitalsMappings[hospital] = [x.strip() for x in row[1:]] 
    
            
    # print out the stable match
    def reportMatches(self):
        print(self.matches)
            
    # follow the chart described in the lab to find the stable match
    def runMatch(self):
        '''
        It is suggested you use the debugger or similar output statements
        to determine what the contents of the data structures are
        '''        

        # The answers are: Charlie: CA, Doris: VT, Alex: WA, Barbara: NY

        # First we create a dictionary of proposed_matches (this will help us walk through the logic)
        proposed_matches = {resident: [] for resident in self.unmatchedResidents}

        # Basically saying while unmatchedResidents isn't empty / this will be the while loop for entire program
        while self.unmatchedResidents:
            # Here we need a listed for loop iterating through the unmatchedResidents list
            # and a second for loop making sure that hospital is in each resident's Mappings
            for resident in self.unmatchedResidents:
                for hospital in self.residentsMappings[resident]:
                    if hospital not in proposed_matches[resident]:
                        proposed_matches[resident].append(hospital)
                        break

                preferred_hospital = proposed_matches[resident][-1]

                if preferred_hospital not in self.matches.values():
                    self.matches[resident] = preferred_hospital
                    self.unmatchedResidents.remove(resident)

                else:
                    # Get the current match for the hospital
                    current_match = [resident for resident, hospital in self.matches.items() if hospital == preferred_hospital][0]

                    # The logic here is that we want to make sure the hospital prefers the new hospital
                    # over the current hospital in the match, and if this is true, we then switch the current hospital with the
                    # new hospital

                    if self.hospitalsMappings[preferred_hospital].index(resident) < self.hospitalsMappings[
                        preferred_hospital].index(current_match):
                        # Hospital prefers the new resident, so replace the current match
                        self.unmatchedResidents.append(current_match)
                        self.matches[resident] = preferred_hospital
                        self.unmatchedResidents.remove(resident)
                        del self.matches[current_match]



if __name__ == "__main__":
   
    # some error checking
    if len(sys.argv) != 3:
        print('ERROR: Usage\n python ResidencyMatch.py [residents preferences] [hospitals preferences]')
        quit()

    # create an instance of ResidencyMatch 
    match = ResidencyMatch()

    # now call the runMatch() function
    match.runMatch()
    
    # report the matches
    match.reportMatches()



