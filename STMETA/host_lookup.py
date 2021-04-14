import re
from Bio import Entrez
import pandas as pd

class HostLookup():
    """
    A class that tries to correct host labels found in the original metadata set from ENA

    Examples
    ----------
        >>> hostsearcher = HostLookup(email='A.N.Other@example.com', no_fix='NOFIX')
        >>> hostsearcher.search('mouse')
        ### ('Mus musculus', 'Mouse')
    """
    
    def __init__(self, email, na_val='Not available', no_fix=None):
        """Initialize the lookup system

        Parameters
        ----------
        email : str
            Email for Entrez
        na_val : str, optional
            Label for missing information, by default 'Not available'
        no_fix : str, optional
            Label for search that did not yield a result, by default None
        """
        self.na_val = na_val
        self.no_fix = no_fix
        
        if self.no_fix is None:
            self.no_fix = self.na_val
        
        self.chars = re.compile(r'[\.\,\:\;\&\'\"\?\{\}\\\*\=]')
        
        self.email = email
        Entrez.email = email
    
    def isnan(self, string):
        return pd.isna(string) or string.strip() == ''
        
    def esearch(self, host):
        
        scientific_name, common_name = self.no_fix, self.no_fix
        
        handle = Entrez.esearch(db='taxonomy', term=host)
        records = Entrez.read(handle)
        handle.close()
        
        if int(records['Count']) > 0:
            host_tax_id = records['IdList'][0]
            scientific_name, common_name = self.efetch(host_id=host_tax_id)
        
        return scientific_name, common_name
    
    def efetch(self, host_id):
        
        scientific_name, common_name = self.no_fix, self.no_fix
        
        handle = Entrez.efetch(db='taxonomy', id=host_id)
        record = Entrez.read(handle)
        handle.close()
        
        if len(record) > 0:
            scientific_name = record[0]['ScientificName']
            try:
                common_name = record[0]['OtherNames']['CommonName'][0].title()
            except:
                common_name = ''
        
        return scientific_name, common_name
        
    
    def search(self, host, tax_id=0, verbose=False):
        
        if verbose:
            print(f"Input search: host='{host}' tax_id={tax_id}" + " "*100, end='\r')
        
        if tax_id > 0:
            scientific_name, common_name = self.efetch(tax_id)
        
        if self.isnan(host) and tax_id == 0:
            return self.na_val, self.na_val
        
        scientific_name, common_name = self.esearch(host.strip())
                            
        return scientific_name, common_name
    
if __name__ == "__main__":
    hostsearcher = HostLookup(email='A.N.Other@example.com', no_fix='NOFIX')
    print(hostsearcher.search('mouse'))