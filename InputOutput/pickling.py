#Author: Nandini Patel
#Date: May 4, 2020
#Description: Pickling in Python

import pickle #importing pick lib

# imelda = ("More Mayhem", 
#             "Imelda May",
#             "2011",
#             ((1, "Pulling the Rug")),
#             (2, "Pscyo"),
#             (3, "Mayhem"))

# with open("imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda, pickle_file) 
    #dumps it into the file

# with open("imelda.pickle", "rb") as imelda_pickled:
#     imelda2 = pickle.load(imelda_pickled)

# print(imelda2)

#once a file is open for writing, it can dump several things
#you can dump multiple things using pickle; while load, load in the order that its dumped in

#deletes a pickle file while loading it
pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")