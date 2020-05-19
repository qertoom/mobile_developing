import csv
import pdfkit

def start():
    while True:
        a = int(input("1-start"))
        if a ==1:
            create_pdf()
        else:
            break;

timestamp = []
msisdn_origin = []
msisdn_dest = []
call_duration = []
sms_number = []

filepath = r"data (2).csv"

with open(filepath, "r", newline="") as file:

    reader = csv.reader(file) 

   
    for row in reader:
        list0 = row[0].split(',')
        list1 = row[1].split(',')
        list2 = row[2].split(',')
        list3 = row[3].split(',')
        list4 = row[4].split(',')
    
        
        timestamp.extend(list0)
        msisdn_origin.extend(list1)
        msisdn_dest.extend(list2)
        call_duration.extend(list3)
        sms_number.extend(list4)

bill_for_income_calls = 0
bill_for_out_calls = 0
bill_for_sms = 0
total = 0


price_income_calls=2
minutes_for_free=20
price_out_calls =0
price_sms=2
   

def tarification():
    sum_income_call = 0
    sum_out_call = 0
    sms = 0
        
    for i in range(len(msisdn_origin)):
        if msisdn_origin[i] == '933156729':
            sum_income_call = sum_income_call + float(call_duration[i])
            sms = float(sms_number[i])


    for j in range(len(msisdn_dest)):
        if msisdn_dest[j] == '933156729':
            sum_out_call = sum_out_call + float(call_duration[j])

    if sum_income_call > 20:
        bill_for_income_calls = (sum_income_call - minutes_for_free) * price_income_calls
    else:
        bill_for_income_calls = 0
    #print("Bill for incoming calls: ", bill_for_income_calls)
    bill_for_out_calls = sum_out_call * price_out_calls
    #print("Bill for outcoming calls: ", bill_for_out_calls)
    calls = bill_for_out_calls +  bill_for_income_calls
    
    bill_for_sms = sms * price_sms
    #print("Bill for SMS: ", bill_for_sms)

    total = bill_for_income_calls + bill_for_out_calls + bill_for_sms
    #print('TOTAL: ', total)
    return calls, bill_for_sms




def inet():
    x=[]
    y=[]
    data = open('input.txt', 'r')
    i=0
    sum_bytes=0
    for row in data.readlines():
        str=row.split(' ')
        counter=0
        while counter< len(str):
            if str[counter] =="":
                del str[counter]
            else:
                counter +=1
            ip_src=str[4].split(':')
        if ip_src[0]=="192.168.250.3":
            #print(str[1])
            sum_bytes += float(str[8])
    #print(sum_bytes)
    bill = round(((sum_bytes/1024-1000)*0.5),2)
    #print("Bill for internet: ", bill)
    return bill

def total():
    inet1 = inet()
    print(inet1)
    calls1, sms = tarification()
    print(calls1)
    print(sms)
    total = calls1 + sms + inet1
    print(total)



def create_pdf():
    net = inet()
    tel,sms = tarification()
    sum = net + tel + sms
    text = open('index.html', 'r', encoding="UTF-8")
    output = open('index1.html', 'w', encoding="UTF-8")
    while 1:
        html = text.readline()
        if not html:
            break;
        html = html.replace("{{ BIK }}", "1111111")
        #output.write(html)
        html = html.replace("{{ SRC_NUM }}", "2233665544")
        #output.write(html)
        html = html.replace("{{ INN }}", "8800553535")
        #output.write(html)
        html = html.replace("{{ KPP }}", "255133445")
        html = html.replace("{{ DST_NUM }}", "3535555800")
        #output.write(html)
        html = html.replace("{{ NUMBER }}", "25")
        #output.write(html)
        html = html.replace("{{ DATE }}", "31.04.2020")
        #output.write(html)
        html = html.replace("{{ CUSTOMER }}", "Звягинцев Никита Юрьевич")
        #output.write(html)
        html = html.replace("{{ TEL }}", str(tel))
        #output.write(html)
        html = html.replace("{{ SMS }}", str(sms))
        #output.write(html)
        html = html.replace("{{ NET }}", str(net))
        #output.write(html)
        html = html.replace("{{ SUM }}", str(sum))
        output.write(html)
    output.close()
    file = open('index1.html', 'r')

    pdfkit.from_file('index1.html', 'invoice.pdf')


start()
