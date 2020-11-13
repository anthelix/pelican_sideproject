#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import os
import re


def dict_name_path():
    '''
    get files in data/data_raw
    return a dic_name of the files name
    '''
    try: 
        # Get the absolute path of parent directory 
        parent = os.path.dirname(os.getcwd()) 
        # Get the absolute path of parent input files and output  files
        data_raw_path = os.path.join(parent,'data', 'data_raw')
        data_path = os.path.join(parent,'data')
        # list of files 
        files = [f for f in os.listdir(data_raw_path) if os.path.isfile(os.path.join(data_raw_path, f))]
        dic_name = {}
        if len(files) < 1:
            raise ValueError(" No files in data/data_raw")
    except Exception as e:
        print(e)
    else:
        try:
            for f in files:
                name = re.split('\W+',f)[0]
                path_in = os.path.join(data_raw_path,f)
                path_out = os.path.join(data_path,f)
                dic_name[name] = [path_in, path_out]
            return(dic_name)
        except Exception as e:
            print(e)

def surgeon(motif, dic_name):
    '''
    get Surgeon.csv file
    return dataframe
    '''
    if motif in dic_name.keys():
        try:
            path_in = dic_name[motif][0]
            path_out = dic_name[motif][1]
            name_file = motif
        except Exception as e:
            print(e)
        else:
            try:
                # Work on dataframe
                df_raw = pd.read_csv(path_in)
                colDrop = ['Copy Confirmation', 'Email', 'User ID', 'Deleted']
                df_drop = df_raw.drop(colDrop, axis=1)            
                df_drop = df_drop.apply(lambda x: x.astype(str)\
                                 .str.lower())\
                                 .rename(columns={"ID": "ID_surgeon",\
                                                  "Firstname": "Firstname Surgeon",\
                                                  "Lastname": "Lastname Surgeon"})
                
                #work on Firstname column
                df_drop['Firstname Surgeon'] = df_drop['Firstname Surgeon'].str.title()
                
                #work on Lastname Column
                df_drop['Lastname Surgeon'] = df_drop['Lastname Surgeon'].str.upper()
                if len(df_drop) < 1:
                    raise ValueError(" Dataframe for surgeon is empty")
                return(df_drop)
            except Exception as e:
                print(e)

def specialty(motif, dic_name):
    '''
    get Specilaty.csv file
    return dataframe
    '''
    if motif in dic_name.keys():
        try:
            path_in = dic_name[motif][0]
            path_out = dic_name[motif][1]
            name_file = motif
        except Exception as e:
            print(e)
        else:
            try:
                # Work on dataframe
                df_raw = pd.read_csv(path_in)
                #display(df_raw[df_raw.isnull().any(axis=1)])
                df_drop = df_raw.apply(lambda x: x.astype(str).str.lower())\
                                .rename(columns={"ID": "ID_specialty", "Name": "Specilaty Name"})
                drop_test = df_drop.apply(lambda x: x.str.contains('pélican|test|démo')).any(axis=1)
                df_drop = df_drop[~drop_test]
                #work on Specilaty Name
                df_drop['Specilaty Name'] = df_drop['Specilaty Name'].str.title()
                if len(df_drop) < 1:
                        raise ValueError(" Dataframe for specilaty is empty")
                return(df_drop)
            except Exception as e:
                print(e)

def operatingSpecialty(motif, dic_name):
    '''
    get 'OperatingSpecialty'.csv file
    return dataframe
    '''
    if motif in dic_name.keys():
        try:
            path_in = dic_name[motif][0]
            path_out = dic_name[motif][1]
            name_file = motif
        except Exception as e:
            print(e)
        else:
            try:
                # Work on dataframe
                df_raw = pd.read_csv(path_in)
                df_drop = df_raw.apply(lambda x: x.astype(str).str.lower())\
                                .rename(columns={"ID": "ID_OperatingSpecialty", "Name": "Operating Specilaty Name"})
                #display(df_drop[df_drop.isna().any(axis=1)])
                #work on Operating Specilaty Name
                df_drop['Operating Specilaty Name'] = df_drop['Operating Specilaty Name'].str.title()
                if len(df_drop) < 1:
                    raise ValueError(" Dataframe for operatingSpecialty is empty")
                return(df_drop)
            except Exception as e:
                print(e)

def bodyLocation(motif, dic_name):
    '''
    get BodyLocation.csv file
    return dataframe
    '''
    if motif in dic_name.keys():
        try:
            path_in = dic_name[motif][0]
            path_out = dic_name[motif][1]
            name_file = motif
        except Exception as e:
            print(e)
        else:
            try:
                # Work on dataframe
                df_raw = pd.read_csv(path_in)
                #display(df_raw[df_raw.isna().any(axis=1)])
                df_drop = df_raw.apply(lambda x: x.astype(str).str.lower())\
                                .rename(columns={"ID": "ID_bodyLocation", "Name": "Body Location Name"})
                #display(df_drop[df_drop.isna().any(axis=1)])
                #work on Body Location Name
                df_drop['Body Location Name'] = df_drop['Body Location Name'].str.title()
                if len(df_drop) < 1:
                    raise ValueError(" Dataframe for bodyLocation is empty")
                return(df_drop)
            except Exception as e:
                print(e)

def healthInstitution(motif, dic_name):
    '''
    get HealthInstitution.csv file
    return dataframe
    '''
    if motif in dic_name.keys():
        try:
            path_in = dic_name[motif][0]
            path_out = dic_name[motif][1]
            name_file = motif
        except Exception as e:
            print(e)
        else:
            try:
                # Work on dataframe
                df_raw = pd.read_csv(path_in, dtype={'zip code': 'str'})
                colDrop = ['Ad R1', 'A Dr2', 'Affiliated', 'Country', 'County', 'Type']
                df_drop = df_raw.drop(colDrop, axis=1)
                #display(df_drop[df_drop.isnull().any(axis=1)])
                
                df_drop =  df_drop.apply(lambda x: x.astype(str).str.lower())\
                                  .rename(columns={"ID": "ID_HealthInstitution", "Name": "HealthInstitution Name",\
                                                   "City": "HealthInstitution City", "Zip Code": "HealthInstitution Zip Code"})        
                drop_test = df_drop.apply(lambda x: x.str.contains(r'\bpélican\b|\btest\b|\bmaroc\b')).any(axis=1)
                df_drop = df_drop[~drop_test]
                
                #work on HealthInstitution Name            
                df_drop['HealthInstitution Name'] = df_drop['HealthInstitution Name'].str.title()
                #work on HealthInstitution City
                df_drop['HealthInstitution City'] = df_drop['HealthInstitution City'].str.split('cedex').str[0].str.upper()
                #workon HealthInstitution Zip Code
                df_drop['HealthInstitution Zip Code'] = df_drop['HealthInstitution Zip Code'].replace('\s+', '', regex=True)
                df_drop['HealthInstitution Zip Code'] =  df_drop['HealthInstitution Zip Code'].apply(lambda x : x.ljust(5, '0'))
                df_drop['HealthInstitution county'] = df_drop['HealthInstitution Zip Code'].str[:2]
                if len(df_drop) < 1:
                    raise ValueError(" Dataframe for healthInstitution is empty")
                return(df_drop)
            except Exception as e:
                print(e)

def laboratory(motif, dic_name):
    '''
    get Laboratory.csv file
    return dataframe
    '''
    if motif in dic_name.keys():
        try:
            path_in = dic_name[motif][0]
            path_out = dic_name[motif][1]
            name_file = motif
        except Exception as e:
            print(e)
        else:
            try:
                # drop extra columns
                df_raw = pd.read_csv(path_in, dtype={'zip code': 'str', 'Block Id': 'str'})
                colDrop = ['Ad R1', 'A Dr2', 'Competence', 'Connected', 'Country', 'Description', 'Events', 'Fax',\
                        'Logo Laboratory', 'Mail', 'Non Dis Po', 'Non Member', 'Site', 'Telephone']
                df_drop = df_raw.drop(colDrop, axis=1)
                #display(msno.matrix(df_drop)) ## missingno
                #work with nan values
                df_drop[['Bloc ID', 'Zip Code']] = df_drop[['Bloc ID', 'Zip Code']].fillna('000')
                df_drop['City'] = df_drop['City'].fillna('Unknow')
                #display(df_drop[df_drop.isna().any(axis=1)])
                
                #replace and clean
                df_drop = df_drop.apply(lambda x: x.astype(str).str.lower())\
                                .rename(columns={"ID": "ID_Laboratory", "Name": "Laboratory Name", "Bloc ID": "Laboratory Bloc ID",\
                                                "City": "Laboratory City", "Zip Code": "Laboratory Zip Code"})        
                drop_test = df_drop.apply(lambda x: x.str.contains(r'\bpélican\b|\btest\b|\bmaroc\b')).any(axis=1)
                df_drop = df_drop[~drop_test]
                #work on Laboratory Name
                df_drop['Laboratory Name'] = df_drop['Laboratory Name'].str.title()
                df_drop['Laboratory Name'] = df_drop['Laboratory Name'].replace('\s+', ' ', regex=True)

                #work on Laboratory City
                df_drop['Laboratory City'] = df_drop['Laboratory City'].str.split('cedex')\
                                                                    .str[0]\
                                                                    .replace('\s+', ' ', regex=True)\
                                                                    .str.upper()
                #workon Laboratory Zip Code
                df_drop['Laboratory Zip Code'] = df_drop['Laboratory Zip Code'].replace('\s+', '', regex=True)
                df_drop['Laboratory Zip Code'] =  df_drop['Laboratory Zip Code'].apply(lambda x : x.ljust(5, '0')).str[:5]

                try:
                    df_drop['Laboratory Zip Code'] = df_drop['Laboratory Zip Code'].astype('int')
                except:
                    df_drop['Laboratory Zip Code'] = df_drop['Laboratory Zip Code'].replace('\D+', 99999, regex=True).astype('int')
                df_drop['Laboratory County'] = df_drop['Laboratory Zip Code'].astype('str').str[:2].astype('int') 
                if len(df_drop) < 1:
                    raise ValueError(" Dataframe for laboratory is empty")
                return(df_drop)
            except Exception as e:
                print(e)

def operatingBlock(motif, dic_name):
    '''
    get OperatingBlock.csv file
    return dataframe
    '''
    if motif in dic_name.keys():
        try:
            path_in = dic_name[motif][0]
            path_out = dic_name[motif][1]
            name_file = motif
        except Exception as e:
            print(e)
        else:
            try:
                # drop columns
                df_raw = pd.read_csv(path_in)
    
                colDrop = ['Ad R1', 'A Dr2', 'Actor','Contact Email', 'Contact Management', 'Contact Name', 'Country',\
                           'County', 'Delivery Location', 'Disable Arch Iva Ge Auto', 'Logistic', 'Name Eds', 'Overview',\
                           'Pre Reservation', 'Return Location', 'Supplier Management', 'Telephone', 'Surgeon Directory' ]
                df_drop = df_raw.drop(colDrop, axis=1)
                
                #Deal with nan values
                df_drop[['Health Institution ID','Zip Code']] = df_drop[['Health Institution ID','Zip Code']].fillna('000')
                df_drop['City'] = df_drop['City'].fillna('Unknow')
                
                df_drop = df_drop.apply(lambda x: x.astype(str).str.lower())\
                                                   .rename(columns={"ID": "ID_OperatingBlock", "Name": "OperatingBlock Name",\
                                                                    "City": "OperatingBlock City", "Zip Code": "OperatingBlock Zip Code"})
                
                drop_test = df_drop.apply(lambda x: x.str.contains(r'\bpélican\b|\btest\b|\bmaroc\b')).any(axis=1)
                df_drop = df_drop[~drop_test]
                #work on OperatingBlock Name
                df_drop['OperatingBlock Name'] = df_drop['OperatingBlock Name'].str.title().replace('\s+', ' ', regex=True)
                
                #work on OperatingBlock City
                df_drop['OperatingBlock City'] = df_drop['OperatingBlock City'].str.split('cedex').str[0].replace('\s+', ' ', regex=True).str.upper()
                #workon OperatingBlock Zip Code
                df_drop['OperatingBlock Zip Code'] = df_drop['OperatingBlock Zip Code'].replace('\s+', '', regex=True)\
                                                                                       .replace('\.0', '', regex=True)\
                                                                                       .apply(lambda x : x.ljust(5, '0'))
                df_drop['OperatingBlock County'] = df_drop['OperatingBlock Zip Code'].str[:2]
                
                #work on Health Institution ID
                df_drop['Health Institution ID'] = df_drop['Health Institution ID'].replace('\.0', '', regex=True)

                if len(df_drop) < 1:
                    raise ValueError(" Dataframe for operatingBlock is empty")
                return(df_drop)
            except Exception as e:
                print(e)

def fosUserUser(motif, dic_name):
    '''
    get FosUserUser.csv file
    return dataframe
    '''
    if motif in dic_name.keys():
        try:
            path_in = dic_name[motif][0]
            path_out = dic_name[motif][1]
            name_file = motif
        except Exception as e:
            print(e)
        else:
            try:
                # Work on dataframe
                df_raw = pd.read_csv(path_in, dtype={'zip code': 'str'})
                colDrop = ['Admin Lab', 'Biography', 'By Default','Cg U','Confirmation Token',\
                           'Credentials Expire At', 'Credentials Expired', 'Date Of Birth', 'Email',\
                           'Email Canonical', 'Enabled', 'Expired', 'Gender','Locale', 'Locked',\
                           'Password', 'Password Requested At', 'Phone', 'Roles', 'Salt','Surgeon',\
                           'Timezone', 'Username Canonical', 'Website', 'Expires At']
                df_drop = df_raw.drop(colDrop, axis=1)
                #display(msno.matrix(df_drop)) ## missingno

                #Deal with nan values
                mystring = ['Firstname','Lastname', 'Username']
                myinteger = ['Laboratory ID','Operating Block ID', 'Surgeon Entity ID' ]
                mytimeseries = ['Last Login',  ]
                df_drop[mytimeseries] = df_drop[mytimeseries].fillna('000')
                df_drop[myinteger] = df_drop[myinteger].fillna('000')            
                df_drop[mystring] = df_drop[mystring].fillna('Unknow')
                #display(df_drop[df_drop.isnull().any(axis=1)])

                df_drop =  df_drop.apply(lambda x: x.astype(str).str.lower())\
                                  .rename(columns={"ID": "ID_FosUserUser", "Firstname": "FosUserUser Firstname",\
                                                   "Lastname": "FosUserUser Lastname", "Laboratory ID": "FosUserUser Laboratory ID",\
                                                   "Operating Block ID": "FosUserUser Operating Block ID","Surgeon Entity ID":"FosUserUser Surgeon Entity ID",\
                                                   "Username":"FosUserUser Username"})        
                drop_test = df_drop.apply(lambda x: x.str.contains(r'\bpélican\b|\btest\b|\bmaroc\b')).any(axis=1)
                df_drop = df_drop[~drop_test]
                
                #work on string            
                df_drop['FosUserUser Firstname'] = df_drop['FosUserUser Firstname'].str.title()
                df_drop['FosUserUser Lastname'] = df_drop['FosUserUser Lastname'].str.upper()
                #work on FosUserUser Operating Block ID
                df_drop['FosUserUser Operating Block ID'] = df_drop['FosUserUser Operating Block ID'].replace('\.0', '', regex=True)
                #work on FosUserUser Operating Block ID
                df_drop['FosUserUser Surgeon Entity ID'] = df_drop['FosUserUser Surgeon Entity ID'].replace('\.0', '', regex=True)
                #work on FosUserUser Operating Block ID
                df_drop['FosUserUser Laboratory ID'] = df_drop['FosUserUser Laboratory ID'].replace('\.0', '', regex=True)
                #display(msno.matrix(df_drop))            
                if len(df_drop) < 1:
                    raise ValueError(" Dataframe for fosUserUser is empty")
                return(df_drop)
            except Exception as e:
                print(e)



def request(motif, dic_name):
    '''
    get Request.csv file
    return dataframe
    '''
    if motif in dic_name.keys():
        try:
            path_in = dic_name[motif][0]
            path_out = dic_name[motif][1]
            name_file = motif
        except Exception as e:
            print(e)
        else:
            try:
                # Work on dataframe
                keepCols = ['ID','Ch Iru Rg Ical Type','Chosen Laboratory ID','Date','End Date','Expected Delivery Date','Expected Material',\
                            'First Operation Date','Instrument Type','Last Operation Date','Location ID','Operating Block User ID','Recovery Date',\
                            'Specialty Ch Iru Rg Ical ID','Specialty ID','Surgeon','Surgeon Entity ID']
                df_drop = pd.read_csv(path_in, usecols=keepCols)
                #display(msno.matrix(df_drop)) ## missingno
                
                #Deal with nan values
                mystring = ['Expected Material', 'Instrument Type', 'Surgeon', 'Expected Material', 'Instrument Type']
                myinteger = ['Chosen Laboratory ID','Location ID', 'Specialty Ch Iru Rg Ical ID',\
                             'Specialty ID', 'Surgeon Entity ID', 'Ch Iru Rg Ical Type']
                mytimeseries = ['First Operation Date','Last Operation Date', 'Recovery Date', 'Expected Delivery Date']
                df_drop[mytimeseries] = df_drop[mytimeseries].fillna('000')
                df_drop[myinteger] = df_drop[myinteger].fillna('000')            
                df_drop[mystring] = df_drop[mystring].fillna('Unknow')
                
                df_drop = df_drop.apply(lambda x: x.astype(str).str.lower()).rename(columns={"ID": "ID_Request",\
                            "Ch Iru Rg Ical Type": "Chirurgical Type", "Specialty Ch Iru Rg Ical ID":"Specialty Chirurgical ID"})
                drop_test = df_drop.apply(lambda x: x.str.contains('pélican|test|démo')).any(axis=1)
                df_drop = df_drop[~drop_test]

                #work on Instrument Type and Expected Material
                df_drop['Instrument Type'] = df_drop['Instrument Type'].str.title()
                df_drop['Expected Material'] = df_drop['Expected Material'].str.title()
                df_drop['Surgeon'] = df_drop['Surgeon'].str.upper()
                myinteger = ['Chosen Laboratory ID','Location ID', 'Specialty Chirurgical ID', 'Specialty ID', 'Surgeon Entity ID',"Chirurgical Type"]
                for cols in myinteger:
                    df_drop[cols] = df_drop[cols].replace('\.0', '', regex=True)
                if len(df_drop) < 1:
                    raise ValueError(" Dataframe for request is empty")
                return(df_drop)
            except Exception as e:
                print(e)


def sendinblue(motif, dic_name):
    '''
    get sendinblue_lod + date.csv file
    return dataframe
    '''
    if motif in dic_name.keys():
        try:
            path_in = dic_name[motif][0]
            path_out = dic_name[motif][1]
            name_file = motif
        except Exception as e:
            print(e)
        else:
            try:
                # Work on dataframe
                df_raw = pd.read_csv(path_in)
                dfDrop = df_raw.copy().drop_duplicates()
                pat = '([A-Z][0-9]{5}[a-z]?)'
                dfDrop['Request ID'] = dfDrop['sub'].str.extract(pat)
                #dfDrop['_test'] = dfDrop['sub'].str.replace(pat,'')
                dfDrop['Request ID'].fillna('Unknow', inplace=True)            
                #Create a 'Status' column with default value set to 'ok'
                dfDrop['Status'] = '99'

                mask = (dfDrop['sub'].str.contains(pat = '(?:Demande de prêt)'))
                dfDrop.loc[mask,'Status'] = 'Demande de prêt'

                mask = (dfDrop['sub'].str.contains(pat = '(?:Nouvelle demande)'))
                dfDrop.loc[mask,'Status'] = 'Nouvelle demande'

                mask = (dfDrop['sub'].str.contains(pat = '(?:a bien été prise en compte)'))
                dfDrop.loc[mask,'Status'] = 'Demande prise en compte'

                mask = (dfDrop['sub'].str.contains(pat = '(?:prêt pour l\'enlevement)'))
                dfDrop.loc[mask,'Status'] = 'Pret pour enlevement'

                mask = (dfDrop['sub'].str.contains(pat = '(?:Confirmation de réservation)'))
                dfDrop.loc[mask,'Status'] = 'Confirmation de réservation'

                mask = (dfDrop['sub'].str.contains(pat = '(?:relance)'))
                dfDrop.loc[mask,'Status'] = 'Relance'

                mask = (dfDrop['sub'].str.contains(pat = '(?: réponse positive)', regex=True))
                dfDrop.loc[mask,'Status'] = 'Demande Reponse positive'

                mask = (dfDrop['sub'].str.contains(pat = '(?: réponse négative)', regex=True))
                dfDrop.loc[mask,'Status'] = 'Demande Reponse negative'

                mask = (dfDrop['sub'].str.contains(pat = '(?:Inscription sur notre)'))
                dfDrop.loc[mask,'Status'] = 'Inscription'

                mask = (dfDrop['sub'].str.contains(pat = '(?:non retenu)'))
                dfDrop.loc[mask,'Status'] = 'Demande non retenu'

                mask = (dfDrop['sub'].str.contains(pat = '(?:An Error Occurred)'))
                dfDrop.loc[mask,'Status'] = 'Error'

                mask = (dfDrop['sub'].str.contains(pat = '(?:est terminée)'))
                dfDrop.loc[mask,'Status'] = 'Demande terminee'

                mask = (dfDrop['sub'].str.contains(pat = '(?: \:\spré-réservation)', regex=True))
                dfDrop.loc[mask,'Status'] = 'Demande pre-reservation'

                mask = (dfDrop['sub'].str.contains(pat = '(?:a été annulée)'))
                dfDrop.loc[mask,'Status'] = 'Demande annulee'

                mask = (dfDrop['sub'].str.contains(pat = '(?:est terminée)'))
                dfDrop.loc[mask,'Status'] = 'Demande terminee'

                mask = (dfDrop['sub'].str.contains(pat = '(?: \:\sréservation annulée)', regex=True))
                dfDrop.loc[mask,'Status'] = 'Reservation annulee'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^réponse positive$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'Reponse positive Autre'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^prêt[A-Z][0-9]{5}[a-z]?$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'Pret Autre'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^réservation$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'Reservation Autre'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^retenu$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'Retenu autre'

                mask = (dfDrop['sub'].str.contains(pat = '(?:confirmation de réservation)'))
                dfDrop.loc[mask,'Status'] = 'Confirmation de reservation x'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^Aucun$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'Aucun autre'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^réservation annulée$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'reservation annulee autre'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^été annulée$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'ete annulee autre'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^été$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'ete autre'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^Découvrez Arsenal Chirurgical \!$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'Decouvrez Arsenal autre'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^étécompte$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'ete compte autre'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^demande$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'demande autre'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^Vous avez reçu un nouveau message de Roxanne$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'Message Roxanne autre'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^prêtl\'enlevement$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'enlevement pret autre'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^pré-réservation$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'pre-reservation autre'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^You received a new message from Roxanne$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'Roxanne autre'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^prêt$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'pret autre'

                mask = (dfDrop['sub'].str.contains(pat = '(?:^terminée$)', regex=True))
                dfDrop.loc[mask,'Status'] = 'terminee autre'


                dfDrop.drop(['tag', 'mid','email', 'sub' ], 1, inplace=True)
                dfDrop = dfDrop.rename(columns= {'st_text': 'Status message', 'ts':'Timestamp', 'frm':'From', 'Status': "Request Status" })
                #dfDrop.sort_values(by='Status').head(20)                
                if len(dfDrop) < 1:
                    raise ValueError(" Dataframe for sendinblue is empty")
                return(dfDrop)
            except Exception as e:
                print(e)
    
def myMain():
    try:
        myDictFunction = {"Surgeon":surgeon, "OperatingSpecialty":operatingSpecialty, "BodyLocation": bodyLocation,\
                  "FosUserUser":fosUserUser,"HealthInstitution":healthInstitution, "Laboratory":laboratory,\
                  "OperatingBlock" : operatingBlock, "Request": request, "Specialty" : specialty, "Sendinblue_logs": sendinblue}
        dic_name = dict_name_path()
        path = './../data/data_clean/'
    except Exception as e:
                print(e)
    else:
        for name, myfunc in myDictFunction.items():
            df_name = 'df_'+name
            name_csv = name+'_clean.csv'
            print(path+name_csv)
            myDictFunction[name](name, dic_name).to_csv (path+name_csv, encoding = 'utf-8', index=False)
        return()

myMain()