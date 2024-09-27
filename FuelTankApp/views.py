from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from .models import HoleDB,FuelTankLeakTestDB
from datetime import datetime,timedelta,date
from pyModbusTCP.client import ModbusClient
import socket
import threading
import pandas as pd
import time
from django.db.models import F

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle ,Paragraph ,Spacer , Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from django.utils import timezone
# import datetime
from django.views.decorators.csrf import csrf_exempt

def HomePage(request):

    today = datetime.now()
    
    
    seven_days_ago = today - timedelta(days=7)
    azone_data = HoleDB.objects.filter(DateTime__date__gte=seven_days_ago, DateTime__date__lte=today).values_list('azone', flat=True)
    azone_data = azone_data.order_by('DateTime')

    bzone_data = HoleDB.objects.filter(DateTime__date__gte=seven_days_ago, DateTime__date__lte=today).values_list('bzone', flat=True)
    bzone_data = bzone_data.order_by('DateTime')

    czone_data = HoleDB.objects.filter(DateTime__date__gte=seven_days_ago, DateTime__date__lte=today).values_list('czone', flat=True)
    czone_data = czone_data.order_by('DateTime')

    dzone_data = HoleDB.objects.filter(DateTime__date__gte=seven_days_ago, DateTime__date__lte=today).values_list('dzone', flat=True)
    dzone_data = dzone_data.order_by('DateTime')

    ezone_data = HoleDB.objects.filter(DateTime__date__gte=seven_days_ago, DateTime__date__lte=today).values_list('ezone', flat=True)
    ezone_data = ezone_data.order_by('DateTime')

    fzone_data = HoleDB.objects.filter(DateTime__date__gte=seven_days_ago, DateTime__date__lte=today).values_list('fzone', flat=True)
    fzone_data = fzone_data.order_by('DateTime')

    gzone_data = HoleDB.objects.filter(DateTime__date__gte=seven_days_ago, DateTime__date__lte=today).values_list('gzone', flat=True)
    gzone_data = gzone_data.order_by('DateTime')
    
    
    
    
    piezoneA=[int(val) for val in azone_data]
    piezoneB=[int(val) for val in bzone_data]
    piezoneC=[int(val) for val in czone_data]
    piezoneD=[int(val) for val in dzone_data]
    piezoneE=[int(val) for val in ezone_data]
    piezoneF=[int(val) for val in fzone_data]
    piezoneG=[int(val) for val in gzone_data]

    pietotal_sumA = sum(piezoneA)
    pietotal_sumB = sum(piezoneB)
    pietotal_sumC = sum(piezoneC)
    pietotal_sumD = sum(piezoneD)
    pietotal_sumE = sum(piezoneE)
    pietotal_sumF = sum(piezoneF)
    pietotal_sumG = sum(piezoneG)
    
    
    print(pietotal_sumA)
    print(pietotal_sumB)
    print(pietotal_sumC)
    print(pietotal_sumD)
    print(pietotal_sumE)
    print(pietotal_sumF)
    print(pietotal_sumG)

    azone_val=HoleDB.objects.filter(DateTime__date=today).values_list('azone', flat=True)
    bzone_val=HoleDB.objects.filter(DateTime__date=today).values_list('bzone', flat=True)
    czone_val=HoleDB.objects.filter(DateTime__date=today).values_list('czone', flat=True)
    dzone_val=HoleDB.objects.filter(DateTime__date=today).values_list('dzone', flat=True)
    ezone_val=HoleDB.objects.filter(DateTime__date=today).values_list('ezone', flat=True)
    fzone_val=HoleDB.objects.filter(DateTime__date=today).values_list('fzone', flat=True)
    gzone_val=HoleDB.objects.filter(DateTime__date=today).values_list('gzone', flat=True)
    zoneA=[int(val) for val in azone_val]
    zoneB=[int(val) for val in bzone_val]
    zoneC=[int(val) for val in czone_val]
    zoneD=[int(val) for val in dzone_val]
    zoneE=[int(val) for val in ezone_val]
    zoneF=[int(val) for val in fzone_val]
    zoneG=[int(val) for val in gzone_val]

    # zoneA = [int(val) for val in azone_val]

    # Sum the integer values
    total_sumA = sum(zoneA)
    total_sumB = sum(zoneB)
    total_sumC = sum(zoneC)
    total_sumD = sum(zoneD)
    total_sumE = sum(zoneE)
    total_sumF = sum(zoneF)
    total_sumG = sum(zoneG)

    # print(total_sumA,"sdfbjsdfbjkfdsjk")
    # print(total_sumB,"fbjfbjfk")

    context={
        'total_sum':total_sumA,
        'bzone_val':total_sumB,
        'czone_val':total_sumC,
        'dzone_val':total_sumD,
        'ezone_val':total_sumE,
        'fzone_val':total_sumF,
        'gzone_val':total_sumG,
        'pietotal_sumA':pietotal_sumA,
        'pietotal_sumB':pietotal_sumB,
        'pietotal_sumC':pietotal_sumC,
        'pietotal_sumD':pietotal_sumD,
        'pietotal_sumE':pietotal_sumE,
        'pietotal_sumF':pietotal_sumF,
        'pietotal_sumG':pietotal_sumG,
    }
    print(context)
    return render(request, 'home.html',context)

def Detailform(request):
    if request.method == "POST":
        Azone = request.POST.get('field1')
        Bzone = request.POST.get('field2')
        Czone = request.POST.get('field3')
        Dzone = request.POST.get('field4')
        Ezone = request.POST.get('field5')
        Fzone = request.POST.get('field6')
        Gzone = request.POST.get('field7')
        
        Azone = 0 if not Azone else Azone
        Bzone = 0 if not Bzone else Bzone
        Czone = 0 if not Czone else Czone
        Dzone = 0 if not Dzone else Dzone
        Ezone = 0 if not Ezone else Ezone
        Fzone = 0 if not Fzone else Fzone
        Gzone = 0 if not Gzone else Gzone
        print(Azone,"it is a zoneeeee")
        
        savetodb=HoleDB(azone=Azone,bzone=Bzone,czone=Czone,dzone=Dzone,ezone=Ezone,fzone=Fzone,gzone=Gzone)
        savetodb.save()
     
    
    return redirect(HomePage)


def Leaktestform(request):
    if request.method == "POST":
        Azone = request.POST.get('field1')
        Bzone = request.POST.get('field2')
        Czone = request.POST.get('field3')
        D1zone = request.POST.get('field4')
        D2zone = request.POST.get('field5')
        Ezone = request.POST.get('field6')
        Fzone = request.POST.get('field7')
        Gzone = request.POST.get('field8')
        print(Azone,"it is a zoneeeee")
        
        savetodb=FuelTankLeakTestDB(azone=Azone,bzone=Bzone,czone=Czone,d1zone=D1zone,d2zone=D2zone,ezone=Ezone,fzone=Fzone,gzone=Gzone)
        savetodb.save()
    
    return render(request,'leaktest.html')

def leaktestfunc(request):

    
    return render(request,'leaktest.html')

def ReportPage(request):
    return render(request,'report.html')

def ReportData(request):
    global weekdays
    global sectionname
    if request.method=="POST":
        ManualWeekdaysStart=request.POST.get('start')
        ManualWeekdaysStartVal=str(ManualWeekdaysStart)
        print(ManualWeekdaysStartVal)
        ManualWeekDaysEnd=request.POST.get('end')
        ManualWeekDaysEndVal=str(ManualWeekDaysEnd)
        print(ManualWeekDaysEndVal)
        datais=request.POST.get('start2')
        print(datais)
        sectionname = request.POST.get('deviceselection')
        print(sectionname)
        if sectionname == 'model1':
            DBis = HoleDB
        elif sectionname == 'model2':
            DBis = FuelTankLeakTestDB
        
    if datais == 'week':
            startdate=date.today()
            StartDateForWeeksList=str(startdate)
            enddate=startdate - timedelta(days=7)
            EndDateForWeeksList=str(enddate)
            # Geting value from clickdata table and filter data as per start date & end date
            weekdays=DBis.objects.values().filter(DateTime__date__range=[EndDateForWeeksList,StartDateForWeeksList])     
            print(weekdays,"vghvjgvdjvfj")
        
           
    elif datais == 'month':
            startdate=date.today()
            StartDateForWeeksList=str(startdate)
            enddate=startdate - timedelta(days=31)
            EndDateForWeeksList=str(enddate)
            weekdays=DBis.objects.values().filter(DateTime__date__range=[EndDateForWeeksList,StartDateForWeeksList])
            print(weekdays,"month data")     
    elif datais == 'half_year':
            startdate=date.today()
            StartDateForWeeksList=str(startdate)
            enddate=startdate - timedelta(days=180)
            EndDateForWeeksList=str(enddate)
            weekdays=DBis.objects.values().filter(DateTime__date__range=[EndDateForWeeksList,StartDateForWeeksList])
            print(weekdays,"half year data")     
    elif datais == 'year':
            startdate=date.today()
            StartDateForWeeksList=str(startdate)
            enddate=startdate - timedelta(days=365)
            EndDateForWeeksList=str(enddate)
            weekdays=DBis.objects.values().filter(DateTime__date__range=[EndDateForWeeksList,StartDateForWeeksList])
            print(weekdays,"year data")     
    else:       
        weekdays=DBis.objects.values().filter(DateTime__date__range=[ManualWeekdaysStartVal,ManualWeekDaysEndVal])
        print(weekdays,"of daysss")
    
    context={
        "weekdays":weekdays,
        "sectionname":sectionname,
    }
    
    return render(request,'report.html',context)


def Exporttopdf(response):
    
            if sectionname == 'model1':
            
                response = HttpResponse(content_type='application/pdf')
                current_date = date.today().strftime('%Y-%m-%d')
                file_name = f"Report_{current_date}.pdf"
            
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'
                
                doc = SimpleDocTemplate(response, pagesize=letter )
                elements = []
                
                

                # Create a list to hold table data
                table_data = [["Azone", "Bzone", "Czone","Dzone","Ezone","Fzone","Gzone","DateTime"]]  # Replace with actual column names

                # Fill the table data from weekdays
                for day in weekdays:
                    # Append data to the table_data list
                    # formatted_date = day['DateTime'].strftime('%Y-%m-%d')
                    
                    table_data.append([day['azone'], day['bzone'], day['czone'], day['dzone'],day['ezone'],day['fzone'],day['gzone'],day['DateTime'],])  # Replace with actual column values
                
                # Create the table and style
                image_path = 'C:\\Users\\choud\\Downloads\\FuleTank\\FuelTank\\FuelTankApp\static\\images\\technovizL.png' 
                image = Image(image_path, width=100, height=100 , hAlign="LEFT")
                elements.append(image)
                
                styles = getSampleStyleSheet()
                heading_text = "0B Leakage Zone Wise Report"
                heading = Paragraph(heading_text, styles['Title'])
                heading.alignment = TA_CENTER
                # Build the PDF document and return it as response
                elements.append(heading)
                spacer = Spacer(50, 40)
                elements.append(spacer)
                table = Table(table_data)
                table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.black),
                
                ]))

                elements.append(table)
                

                doc.build(elements , onFirstPage=add_border , onLaterPages= add_border)
                
                return response   
            else:
                response = HttpResponse(content_type='application/pdf')
                current_date = date.today().strftime('%Y-%m-%d')
                file_name = f"Report_{current_date}.pdf"
            
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'
                
                doc = SimpleDocTemplate(response, pagesize=letter )
                elements = []
                
                

                # Create a list to hold table data
                table_data = [["Azone", "Bzone", "Czone","D1zone","D2zone","Ezone","Fzone","Gzone","DateTime"]]  # Replace with actual column names

                # Fill the table data from weekdays
                for day in weekdays:
                    # Append data to the table_data list
                    # formatted_date = day['DateTime'].strftime('%Y-%m-%d')
                    
                    table_data.append([day['azone'], day['bzone'], day['czone'], day['d1zone'],day['d2zone'],day['ezone'],day['fzone'],day['gzone'],day['DateTime'],])  # Replace with actual column values
                
                # Create the table and style
                image_path = 'C:\\Users\\choud\\Downloads\\FuleTank\\FuelTank\\FuelTankApp\static\\images\\technovizL.png' 
                image = Image(image_path, width=100, height=100 , hAlign="LEFT")
                elements.append(image)
                
                styles = getSampleStyleSheet()
                heading_text = "Fuel Tank Leak Test"
                heading = Paragraph(heading_text, styles['Title'])
                heading.alignment = TA_CENTER
                # Build the PDF document and return it as response
                elements.append(heading)
                spacer = Spacer(50, 40)
                elements.append(spacer)
                table = Table(table_data)
                table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.black),
                
                ]))

                elements.append(table)
                

                doc.build(elements , onFirstPage=add_border , onLaterPages= add_border)
                
                return response   


def add_border(canvas, doc):
    # Add a border to the entire page
    canvas.saveState()
    canvas.setStrokeColor(colors.black)
    canvas.rect(20, 20,  570, 750)
    canvas.restoreState()




# def DeatailPageload(request):
#     global total_break_duration
#     breakdatafromdb=PopupDataModel.objects.all()
#     print(breakdatafromdb)
#     total_break_duration = timedelta()

    
#     for break_data in breakdatafromdb:

#         break_start_time = datetime.strptime(break_data.BreakStartTime, '%H:%M:%S')
#         break_stop_time = datetime.strptime(break_data.BreakStopTime, '%H:%M:%S')

#         break_duration = break_stop_time - break_start_time
#         total_break_duration += break_duration

#     print(total_break_duration)    
#     context={
#         'breakdatafromdb':breakdatafromdb, 
        
#     }
#     return render(request,'details.html',context)
    
    


# def Detailform(request):
#     global idel_cycle_time
#     global ShiftTimeStart
#     global ShiftTimeStart_obj
#     global ShiftTimeStop_obj
#     global current_time_obj
#     global target

#     if request.method == "POST":
#         ShiftTimeStart = request.POST.get('field1')
#         ShiftTimeStop = request.POST.get('field2')
#         idel_cycle_time = request.POST.get('field3')
#         checking=request.POST.get('timeDifference')
#         target=request.POST.get('field4')
        
#         checking_time = datetime.strptime(checking, '%H:%M').strftime('%H:%M:%S')
        
#         hours, minutes, seconds = map(int, checking_time.split(':'))
#         total_minutes = (hours * 60) + minutes
#         total_break_duration_td = timedelta(hours=total_break_duration.seconds // 3600, minutes=(total_break_duration.seconds // 60) % 60, seconds=total_break_duration.seconds % 60)
#         shift_timing_td = datetime.strptime(checking_time, '%H:%M:%S').time()


#         # Subtract total_break_duration from shift_timing
#         result_td = timedelta(hours=shift_timing_td.hour, minutes=shift_timing_td.minute, seconds=shift_timing_td.second) - total_break_duration_td
#         result_str=str(result_td)
        
#         current_time_obj = datetime.now().time() 
#         ShiftTimeStart_obj = datetime.strptime(ShiftTimeStart, '%H:%M').time()
#         ShiftTimeStop_obj = datetime.strptime(ShiftTimeStop, '%H:%M').time()
#         # ShiftTimeStop_obj = datetime.strptime(ShiftTimeStop, '%H:%M').time().strftime('%H:%M')
#         print(target,"dvgdfhfhfyrtooklmk,knghfdf")
#         breakdatafromdb=PopupDataModel.objects.all()
        
#         context={
#             'result_str':result_str,
#             'breakdatafromdb':breakdatafromdb,
#         }
        
#     return render(request,'details.html',context)


        
       

