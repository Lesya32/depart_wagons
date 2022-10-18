from calendar import month
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime, timedelta
from io import BytesIO
#from django.core.mail import EmailMessage, send_mail
from django.core import mail
from base.settings import  EMAIL_HOST_USER
from .models import *
import xlsxwriter, re
from django.views.generic import FormView, UpdateView, DeleteView, ListView


def home(request):

    return render(request, 'depart_wagons/layout.html')


class list_view(ListView):
    template_name = 'depart_wagons/catalog.html'
    model = mailing_list

def sending(request):
    if request.method == 'POST':
        check_client = request.POST.getlist('check_client')
        recipients= []
        for check in check_client:
            selectclient = client.objects.get(id=check).name
            filename=re.findall(r'"(.*?)"', selectclient)
            if filename:
                recipients.append([mailing_list.objects.get(id_client=check).email, filename[0]])
            else:
                recipients.append([mailing_list.objects.get(id_client=check).email, selectclient])

        #print(recipients[1][1])

    clients = mailing_list.objects.filter(admin=False)
    return render(request, 'depart_wagons/sending.html', {'clients' :clients})    

#<td><input type="checkbox" {% if uch.ng_pismo %} checked {%endif %}"/></td>     

def cron():
    try:
        yesterday = datetime.today() - timedelta(days=31)
        check_client = mailing_list.objects.filter(send=True)
        recipients= []
        for client in check_client:
            filename=re.findall(r'"(.*?)"', client.name)
            if filename:
                filename = 'mail/'+ str(filename[0]) + ' ' + yesterday.strftime("%d_%m_%Y") + '.xlsx'
            else:
                filename = 'mail/'+ str(client.name) + ' ' + yesterday.strftime("%d_%m_%Y") + '.xlsx'
            workbook = xlsxwriter.Workbook(filename)
            worksheet = workbook.add_worksheet() #'name'
            
            border_table = workbook.add_format({'bold': True,
                'border':   1,
                'align':    'center',
                'valign':   'vcenter',
                'text_wrap': True, })
            bold = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter',})
            border = workbook.add_format({'border': 1, 'valign': 'vcenter',})
            border_center = workbook.add_format({'border': 1, 'align': 'center', 'valign': 'vcenter',})
            worksheet.set_column('A:A', 7) 
            worksheet.set_column('C:C', 10)
            worksheet.set_column('D:D', 10)
            worksheet.set_column('G:G', 28)
            worksheet.set_column('H:H', 15)
            
            worksheet.merge_range('A1:H1', 'Предъявление вагонов ', bold)
            worksheet.merge_range('A2:H2', str(client.name), bold)

            worksheet.write(3, 0, 'Станция отправления ст. Сортировочная', workbook.add_format({'bold': True, }))
            worksheet.write(3, 7, 'Станция назначения ст. Китой-Комбинатская', workbook.add_format({'bold': True, 'align': 'right' }))
            worksheet.write(4, 0, 'Ангарский ф-л АО "В-Сибпромтранс"', )
            worksheet.write(4, 7, 'Восточно-Сбирская д.ж. ОАО РЖД', workbook.add_format({'align': 'right' }))
            row = 6
            worksheet.write(row, 0, '№ поезда', border_table)
            worksheet.write(row, 1, '№ п/п в поезде', border_table)
            worksheet.write(row, 2, '№ вагона', border_table)
            worksheet.write(row, 3, 'Вес груза (0,000т)', border_table)
            worksheet.write(row, 4, 'Род п/с', border_table)
            worksheet.write(row, 5, 'Наименование груза', border_table)
            worksheet.write(row, 6, 'Станция', border_table)
            worksheet.write(row, 7, 'Дата и время уведомлления о готовности передачи вагонов на выставочный путь', border_table)

            row += 1
            #print(yesterday)
            selectwagons = wagons.objects.filter(id_depart__date=yesterday, id_depart__type=1, id_client=client.id_client).order_by('id_depart', 'order')
            for wagon in selectwagons:
                worksheet.write(row, 0, wagon.id_depart.numlist, border)
                worksheet.write(row, 1, wagon.order, border_center)
                worksheet.write(row, 2, wagon.number, border)
                worksheet.write(row, 3, wagon.weight, border_center)
                worksheet.write(row, 4, wagon.id_coming.sort.sort, border_center)
                worksheet.write(row, 5, wagon.id_cargo.cargo, border_center)
                worksheet.write(row, 6, wagon.id_station.station, border)
                worksheet.write(row, 7, str(wagon.id_depart.date.strftime("%d.%m.%Y")[:10])+ ' '+str(wagon.id_depart.time) , border_center)
                row += 1
            workbook.close()
            recipients.append([ client.email, filename])
    except:
        print('Ошибка при формировании excel') #!!!!!!!!!!!!!!!!!!!!
    finally:
        try:
            mails=[]
            connection = mail.get_connection()
            for client in recipients:
                #print(client[0])
                email = mail.EmailMessage('Тестовая рассылка из тестовой базы', 'Текст письма', EMAIL_HOST_USER, [client[0]], connection=connection,)
                email.attach_file(client[1])
                mails.append(email)
            
            
            connection.send_messages(mails)
            connection.close()
        except:
            print('Ошибка при отправке почты') #!!!!!!!!!!!!!!!!!!!!

    #response = HttpResponse('Все окей')
    #return HttpResponse(response)