import numbers
import re
import datetime

errorMessages = []

class DataValidator:
    def __init__(self, data, rules, customAttributes={}, customErrorMessage=[]):
        self.data = data
        self.rules = rules
        self.customAttributes = customAttributes
        self.customErrorMessages = customErrorMessage
        self.errorMessages = []

    def getErrorMessagees(self):
        self.isValidData()
        return self.errorMessages



        return errorMessages

    def isValidData(self):
        rulesForTheValue = []
        tmpStr = ""
        tmpStr2 = ""
        isValid = True
        print(self.data)
        for key, value in self.data.items():
            ########################################################
            if isinstance(value,dict):
                print("catched dict ")
                for subkey, subVal in value.items():
                    tmpStr=""
                    rulesForTheValue=self.rules[key+"."+subkey].split("|")
                    for rule in rulesForTheValue:
                        tmpStr = ""
                        tmpStr2 = ""

                        if (rule == 'string'):
                            if self.isValidString(subVal):
                                continue;
                            else:
                                tmpStr = tmpStr + key + "." +subkey+"."+ rule
                                self.errorMessages.append(self.customErrorMessages[tmpStr])
                                isValid = False

                        if (rule == 'number'):
                            if self.isValidNumber(subVal):
                                continue;
                            else:
                                tmpStr = tmpStr + key + "." +subkey+"."+ rule
                                self.errorMessages.append(self.customErrorMessages[tmpStr])
                                isValid = False

                        if (rule == 'required'):
                            if self.isValidReuired(subVal):
                                continue;
                            else:
                                tmpStr = tmpStr + key + "." +subkey+"."+ rule
                                self.errorMessages.append(self.customErrorMessages[tmpStr])
                                isValid = False

                        if (rule == 'email'):
                            if self.isValidEmail(subVal):
                                continue;
                            else:
                                tmpStr = tmpStr + key + "." +subkey+"."+ rule
                                self.errorMessages.append(self.customErrorMessages[tmpStr])
                                isValid = False
                        if (rule == 'date'):
                            print("Hi")
                            if self.isValidDate(subVal):
                                continue;
                            else:
                                tmpStr = tmpStr + key + "." +subkey+"."+ rule
                                self.errorMessages.append(self.customErrorMessages[tmpStr])
                                isValid = False

                        if (rule == 'phone number'):
                            if self.isValidPhoneNumber(subVal):
                                continue;
                            else:
                                tmpStr = tmpStr + key + "." +subkey+"."+ rule
                                self.errorMessages.append(self.customErrorMessages[tmpStr])
                                isValid = False

                        if (rule == 'array'):
                            if self.isValidList(subVal):
                                continue;
                            else:
                                tmpStr = tmpStr + key + "." +subkey+"."+ rule
                                self.errorMessages.append(self.customErrorMessages[tmpStr])
                                isValid = False

                        if (rule[:3] == 'min'):
                            print("validating min")
                            print(rule[3:])
                            if self.isValidMin(subVal, int(rule[3:])):
                                continue;
                            else:
                                tmpStr = "The " + key+"."+subkey + " field must be at least " + rule[3:]

                                self.errorMessages.append(tmpStr)
                                isValid = False

                        if (rule[:3] == 'max'):
                            if self.isValidMax(subVal, int(rule[3:])):
                                continue;
                            else:
                                tmpStr = "The " + key+"."+subkey  + " field must be at most " + rule[3:]

                                self.errorMessages.append(tmpStr)
                                isValid = False

                        if (rule[:2] == 'in'):
                            allowedValues = rule[3:].split(",")
                            if self.isValidIn(value, allowedValues):
                                continue;
                            else:
                                tmpStr = "The" + key+"."+subkey + "field must be one of these " + rule[3:0]

                                self.errorMessages.append(self.customErrorMessages[tmpStr])
                                isValid = False

                continue;




            ########################################################
            rulesForTheValue = self.rules[key].split("|")
            for rule in rulesForTheValue:
                tmpStr = ""
                tmpStr2=""


                if (rule == 'string'):
                    if self.isValidString(value):
                        continue;
                    else:
                        tmpStr =tmpStr + key + "." + rule
                        self.errorMessages.append(self.customErrorMessages[tmpStr])
                        isValid = False

                if (rule == 'number'):
                    if self.isValidNumber(value):
                        continue;
                    else:
                        tmpStr =tmpStr + key + "." + rule
                        self.errorMessages.append(self.customErrorMessages[tmpStr])
                        isValid = False

                if (rule == 'required'):
                    if self.isValidReuired(value):
                        continue;
                    else:
                        tmpStr = tmpStr + key + "." + rule
                        self.errorMessages.append(self.customErrorMessages[tmpStr])
                        isValid = False

                if (rule == 'email'):
                    if self.isValidEmail(value):
                        continue;
                    else:
                        tmpStr = tmpStr + key + "." + rule
                        self.errorMessages.append(self.customErrorMessages[tmpStr])
                        isValid = False
                if (rule == 'date'):
                    if self.isValidDate(value):
                        continue;
                    else:
                        tmpStr = tmpStr + key + "." + rule
                        self.errorMessages.append(self.customErrorMessages[tmpStr])
                        isValid = False

                if (rule == 'phone number'):
                    if self.isValidPhoneNumber(value):
                        continue;
                    else:
                        tmpStr = tmpStr + key + "." + rule
                        self.errorMessages.append(self.customErrorMessages[tmpStr])
                        isValid = False

                if (rule == 'array'):
                    if self.isValidList(value):
                        continue;
                    else:
                        tmpStr = tmpStr + key + "." + rule
                        self.errorMessages.append(self.customErrorMessages[tmpStr])
                        isValid = False

                if (rule[:3] == 'min'):
                    print("validating min")
                    print(rule[3:])
                    if self.isValidMin(value,int(rule[3:])):
                        continue;
                    else:
                        tmpStr = "The " + key + " field must be at least "+ rule[3:]

                        self.errorMessages.append(tmpStr)
                        isValid = False

                if (rule[:3] == 'max'):
                    if self.isValidMax(value,int(rule[3:])):
                        continue;
                    else:
                        tmpStr = "The " + key + " field must be at most "+ rule[3:]

                        self.errorMessages.append(tmpStr)
                        isValid = False

                if (rule[:2] == 'in'):
                    allowedValues = rule[3:].split(",")
                    if self.isValidIn(value,allowedValues):
                        continue;
                    else:
                        tmpStr = "The" + key + "field must be one of these " + rule[3:0]

                        self.errorMessages.append(self.customErrorMessages[tmpStr])
                        isValid = False






    def isValidIn(self, val, listOfValues):
        if val in listOfValues:
            return True
        else:
            return False

    def isValidList(self, val):
        if type(val) == list:
            return True
        else:
            return False

    def isValidMax(self, val, maxVal):
        if (val > maxVal):
            return False
        else:
            return True

    def isValidMin(self, val, minVal):
        print("val"+str(val))
        print("minVal" + str(minVal))

        if (val < minVal):
            return False
        else:
            return True

    def isValidDate(self, val):
        if (len(val)) != 10:
            return False
        try:
            dd = val[:2]
            dd = int(dd)
            mm = int(val[3:5])
            yyyy = int(val[6:])
            now = datetime.datetime.now()

            if (yyyy > now.year):
                return False

            if (mm == 2 and dd > 28):
                return False
            if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
                if mm > 31:
                    return False
            elif (mm > 12 or mm < 1):
                return False
            else:
                if (dd > 30):
                    return False

            if (dd > 31 or dd < 1):
                return False
            return True

        except ValueError:
            return False

    # change here:
    def isValidPhoneNumber(slef, phone_number):
        if len(phone_number) != 12:
            return False
        for i in range(12):
            if i in [3, 7]:
                if phone_number[i] != '-':
                    return False
            elif not phone_number[i].isalnum():
                return False
        return True

    def getFailedAttributes(self):
        failedAttr = []

        return failedAttr

    def isValidEmail(self, val):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", val):
            return False
        else:
            return True

    def isValidReuired(self, val):
        if val is not None:
            return True
        else:
            return False

    def isValidString(self, val):
        if isinstance(val, str):
            return True
        else:
            return False

    def isValidNumber(self, val):
        if isinstance(val, numbers.Number):
            return True
        else:
            return False
