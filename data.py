import pandas as pd
import csv
import json
import numpy as np

contact_t = "processed_input/contacttracing.csv"
inter = "processed_input/internationaltravel.csv"
move = "processed_input/movementrestrictions.csv"
pub = "processed_input/public_transport.csv"
test = "processed_input/testing_policy.csv"
vac = "processed_input/vaccinepolicy.csv"

df_contact = pd.read_csv(contact_t, delimiter=',')
df_contact1 = df_contact[["country_name", "contact_trace"]]
df_contact1.reset_index(inplace=True, drop=True)

df_inter = pd.read_csv(inter, delimiter=",")
df_inter1 = df_inter[["inter_travel"]]
df_inter1.reset_index(inplace=True, drop=True)


df_move = pd.read_csv(move , delimiter=',')
df_move1 = df_move[["movement_res"]]
df_move1.reset_index(inplace=True, drop=True)


df_pub = pd.read_csv(pub, delimiter=",")
df_pub1 = df_pub[["public_trans"]]
df_pub1.reset_index(inplace=True, drop=True)


df_test = pd.read_csv(test, delimiter=",")
df_test1 = df_test[["test_pol"]]
df_test1.reset_index(inplace=True, drop=True)

df_vac = pd.read_csv(vac, delimiter=",")
df_vac1 = df_vac[["vaccine_pol"]]
df_vac1.reset_index(inplace=True, drop=True)

l1=df_contact1.values.tolist()
l2=df_inter1.values.tolist()
for i in range(len(l1)):
    l1[i].extend(l2[i])

df = pd.DataFrame(l1, columns=df_contact1.columns.tolist()+df_inter1.columns.tolist())

l3=df.values.tolist()
l4=df_move1.values.tolist()
for i in range(len(l3)):
    l3[i].extend(l4[i])

df = pd.DataFrame(l3, columns=df.columns.tolist()+df_move1.columns.tolist())

l5=df.values.tolist()
l6=df_pub1.values.tolist()
for i in range(len(l5)):
    l5[i].extend(l6[i])

df = pd.DataFrame(l5, columns=df.columns.tolist()+df_pub1.columns.tolist())

l6=df.values.tolist()
l7=df_test1.values.tolist()
for i in range(len(l6)):
    l6[i].extend(l7[i])

df = pd.DataFrame(l6, columns=df.columns.tolist()+df_test1.columns.tolist())

l7=df.values.tolist()
l8=df_vac1.values.tolist()
for i in range(len(l5)):
    l7[i].extend(l8[i])

df = pd.DataFrame(l7, columns=df.columns.tolist()+df_vac1.columns.tolist())
print(df)
df.to_csv("processed_input/all.csv")



# frames = [df_contact1, df_inter1, df_move1, df_pub1, df_test1, df_vac1]
# preprocessed = pd.concat(frames)
# print(preprocessed)
# preprocessed.to_csv("processed_input/all.csv")



# df['result'] = df.ffill(axis=1).iloc[:, -1:]

# print(df)

# df.to_csv("processed_input/public_transport.csv") 

