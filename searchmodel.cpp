#include<bits/stdc++.h>

using namespace std;


class RabinCarb{
    private:
        string text;
        string pattern;
        
    public:
        static unordered_map<char,int> hashCodes;
        
        RabinCarb(){
            //intialization of hash codes
            for(int i=97;i<=122;i++){
                char key = i;
                int value = i-96;
                RabinCarb::hashCodes[key] = value;
            }
        }
        void getStrings(string text,string pattern){
            this->text = text;
            this->pattern = pattern;
        }

        bool rabinCarbAlgorithm(){
            //algorithm will compare the two strings
            //will return true if the two strings are same else false.

            int m = pattern.size();
            int n = text.size();
            
            int patternHashValue = calculateHashValue(pattern);
            int l = 0,r = m-1;
            while(r<n){
                string subString ="";
                for(int i = l;i<=r;i++){
                    subString = subString + text[i];
                }
                int substringHashValue = calculateHashValue(subString);
                if(patternHashValue == substringHashValue  && checkCharacters(subString,pattern)){
                    return true;
                }
                l++;r++;
            }
            return false;
        }

        int calculateHashValue(string text){
            int m = text.size();

            int hashValue = 0;
            for(int i = 1;i<=m;i++){
                char ch = text[i-1];  
                hashValue = hashValue + (pow(26,m-i)*hashCodes[ch]);
            }   
            return hashValue;
        }

        //check charcaters for spurious hits
        bool checkCharacters(string subString,string pattern){
            int len = pattern.size();
            for(int i=0;i<len;i++){
                if(subString[i]!=pattern[i]) return false;
            }
            return true;
        }
};

unordered_map<char,int> RabinCarb::hashCodes;

int main(){

    //input string is the pragraph which will be uploaded by the user
    string inputString = "";
    //fetching from the preprocessed.txt
    ifstream inputFile;
    inputFile.open("pre-processed.txt",ios::in);
    if(!inputFile.is_open()){
        cout<<"File not opened! Try again"<<endl;
        return 0;
    }

    //we have fetched the pre-processed data in input string

    //database string is the paragraph which will be uploaded by the admin
    string databaseString = "eleph largest land mammal earth distinctli massiv bodi larg ear long trunk.use trunk pick object trumpet warn greet eleph suck water drink bath among use.male femal african eleph grow tusk individu either left right tusk one use usual smaller wear tear.eleph tusk serv mani purpos.extend teeth use protec eleph trunk lift move object gather food strip bark tree. also use defens.time drought eleph even use tusk dig hole find water underground.two genet differ african speci exist savanna eleph forest eleph number characterist differenti.african savanna eleph largest eleph speci asian forest eleph african forest eleph compar smaller size.asian eleph differ sever way african rel distinct physic differ.exampl asian eleph ear smaller compar larg fan shape ear african speci.male sian eleph tusk male femal african eleph grow tusk.led matriarch eleph organ complex social structur femal calv male eleph tend live isol small bachelor group.singl calf born femal everi four five year gestati period month longest mammal.calv care entir herd relat femal.femal calv may stay matern herd rest live male leav herd reach puberti.forest eleph social group differ slightli may compris adult femal offspr.howev may congreg larger group forest clear resourc abund.eleph need extens land area surviv meet ecolog need includ food water space.averag eleph feed hour consum hundr pound plant matter singl day.result lose habitat often come conflict peopl competit resource.";

    //tokenization of the two strings

    //1.Tokenization of the input string

    vector<string> inputTokens;
    char ch;
    string pattern;

    while(getline(inputFile,pattern)){
        //pattern will hold one single line
        cout<<pattern<<endl;
        inputTokens.push_back(pattern);
    }
    inputFile.close();//do make sure to close the file uou opened
    //2.Tokenization of the database string

    vector<string> databaseTokens;
    pattern = "";
    for(int i=0;i<databaseString.length();i++){
        if(databaseString[i] != '.'){
            pattern  = pattern+databaseString[i];
        }
        else{
            databaseTokens.push_back(pattern);
            pattern = "";
        }
    }

    //store the token of every input string as key with value as all other tokens in databse token
    //in a hash map

    set<pair<string,string>> detector;
    for(auto iptToken:inputTokens){//aditya --> //aditya is the.--> aditya is
        for(auto dbsToken:databaseTokens){
            string key = iptToken,value = dbsToken;
            detector.insert({key,value});
        }
    }
    
    //now give the set of two strings as the input to the rabin carb algorithm
    RabinCarb rb;
    cout<<"Matched content"<<endl;
    for(auto it:detector){
        //pair of input and the database sentence string and now compare the two sentnecs
        //using rabin carb algorirhm
        rb.getStrings(it.first,it.second);
        if(rb.rabinCarbAlgorithm()){
            cout<<it.first<<endl;
        }
    }
    return 0;
}
