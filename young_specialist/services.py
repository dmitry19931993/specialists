import xlsxwriter
import datetime
from datetime import date
from .models import YoungSpecialistIndicators, YoungSpecialistsView
import io
from django.http import HttpResponse

def table(start_month_obj, end_month_obj, organization_list, article_list):
    month_list = [
        'ЯНВАРЬ', 'ФЕВАРАЛЬ', 'МАРТ',
        'АПРЕЛЬ', 'МАЙ', 'ИЮНЬ', 'ИЮЛЬ',
        'АВГУСТ', 'СЕНТЯБРЬ', 'ОКТЯБРЬ', 'НОЯБРЬ', 'ДЕКАБРЬ'
    ]
    start_month = f'{month_list[start_month_obj.month - 1]}'
    end_month = f'{month_list[end_month_obj.month - 1]}'
    if start_month_obj.year == end_month_obj.year:
        start_year = ''
        end_year = f'{end_month_obj.year}'
    else:
        start_year = f'{start_month_obj.year}'
        end_year = f'{end_month_obj.year}'


    # Создание нового Excel файла и добавление листа
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()

    # Определение форматов для ячеек
    bold_format = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'border': 1, 'text_wrap': True,})
    header_format = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'border': 1, 'text_wrap': True,})
    merge_format = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'border': 1})
    rotation_format = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'border': 1, 'rotation': 90,})

    # Настройка ширины колонок
    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('F:F', 20)
    worksheet.set_row(3, 40)
    worksheet.set_row(4, 40)
    worksheet.set_row(5, 80)

    # Объединение и добавление ячеек с заголовками
    worksheet.merge_range('A2:AJ2', 'Молодые специалисты', merge_format)
    worksheet.merge_range('A3:AJ3', f'За {start_month} {start_year}-{end_month} {end_year} года', merge_format)
    worksheet.merge_range('A4:A6', 'Наименование организации', bold_format)
    worksheet.merge_range('B4:B6', f'{article_list[0]}', bold_format)
    worksheet.merge_range('C4:E4', f'{article_list[1]}', bold_format)
    worksheet.merge_range('C5:C6', 'Всего', header_format)
    worksheet.merge_range('D5:E5', 'Категория, источник приема на работу', header_format)
    worksheet.write('D6', 'Целевое', rotation_format)
    worksheet.write('E6', 'Распределение', rotation_format)
    worksheet.merge_range('F4:F6', f'{article_list[2]}', bold_format)
    worksheet.merge_range('G4:I4', f'{article_list[3]}', bold_format)
    worksheet.merge_range('G5:G6', 'Всего', header_format)
    worksheet.merge_range('H5:I5', 'Категория, источник приема на работу', header_format)
    worksheet.write('H6', 'Целевое', rotation_format)
    worksheet.write('I6', 'Распределение', rotation_format)
    worksheet.merge_range('J4:L4', f'{article_list[4]}', bold_format)
    worksheet.merge_range('J5:J6', 'Всего', header_format)
    worksheet.merge_range('K5:L5', 'Категория, источник приема на работу', header_format)
    worksheet.write('K6', 'Целевое', rotation_format)
    worksheet.write('L6', 'Распределение', rotation_format)
    worksheet.merge_range('M4:O4', f'{article_list[5]}', bold_format)
    worksheet.merge_range('M5:M6', 'Всего', header_format)
    worksheet.merge_range('N5:O5', 'Категория, источник приема на работу', header_format)
    worksheet.write('N6', 'Целевое', rotation_format)
    worksheet.write('O6', 'Распределение', rotation_format)
    worksheet.merge_range('P4:R4', f'{article_list[6]}', bold_format)
    worksheet.merge_range('P5:P6', 'Всего', header_format)
    worksheet.merge_range('Q5:R5', 'Категория, источник приема на работу', header_format)
    worksheet.write('Q6', 'Целевое', rotation_format)
    worksheet.write('R6', 'Распределение', rotation_format)
    worksheet.merge_range('S4:U4', f'{article_list[7]}', bold_format)
    worksheet.merge_range('S5:S6', 'Всего', header_format)
    worksheet.merge_range('T5:U5', 'Категория, источник приема на работу', header_format)
    worksheet.write('T6', 'Целевое', rotation_format)
    worksheet.write('U6', 'Распределение', rotation_format)
    worksheet.merge_range('V4:X4', f'{article_list[8]}', bold_format)
    worksheet.merge_range('V5:V6', 'Всего', header_format)
    worksheet.merge_range('W5:X5', 'Категория, источник приема на работу', header_format)
    worksheet.write('W6', 'Целевое', rotation_format)
    worksheet.write('X6', 'Распределение', rotation_format)
    worksheet.merge_range('Y4:AA4', f'{article_list[9]}', bold_format)
    worksheet.merge_range('Y5:Y6', 'Всего', header_format)
    worksheet.merge_range('Z5:AA5', 'Категория, источник приема на работу', header_format)
    worksheet.write('Z6', 'Целевое', rotation_format)
    worksheet.write('AA6', 'Распределение', rotation_format)
    worksheet.merge_range('AB4:AD4', f'{article_list[10]}', bold_format)
    worksheet.merge_range('AB5:AB6', 'Всего', header_format)
    worksheet.merge_range('AC5:AD5', 'Категория, источник приема на работу', header_format)
    worksheet.write('AC6', 'Целевое', rotation_format)
    worksheet.write('AD6', 'Распределение', rotation_format)
    worksheet.merge_range('AE4:AG4', f'{article_list[11]}', bold_format)
    worksheet.merge_range('AE5:AE6', 'Всего', header_format)
    worksheet.merge_range('AF5:AG5', 'Категория, источник приема на работу', header_format)
    worksheet.write('AF6', 'Целевое', rotation_format)
    worksheet.write('AG6', 'Распределение', rotation_format)
    worksheet.merge_range('AH4:AJ4', f'{article_list[12]}', bold_format)
    worksheet.merge_range('AH5:AH6', 'Всего', header_format)
    worksheet.merge_range('AI5:AJ5', 'Категория, источник приема на работу', header_format)
    worksheet.write('AI6', 'Целевое', rotation_format)
    worksheet.write('AJ6', 'Распределение', rotation_format)

    for organization in organization_list:
        worksheet.write(f'A{7 + organization_list.index(organization)}', f'{organization}', bold_format)
        yong_specialists = YoungSpecialistsView.objects.filter(name=organization)
        worksheet.write(
            f'B{7 + organization_list.index(organization)}',
            yong_specialists[0].target_distribution_count + yong_specialists[0].distribution_count, header_format
        )
        worksheet.write(
            f'C{7 + organization_list.index(organization)}',
            yong_specialists[0].target_distribution_count + yong_specialists[0].distribution_count, header_format
        )
        worksheet.write(
            f'D{7 + organization_list.index(organization)}',
            yong_specialists[0].target_distribution_count, header_format
        )
        worksheet.write(
            f'E{7 + organization_list.index(organization)}',
            yong_specialists[0].distribution_count, header_format
        )
        worksheet.write(
            f'G{7 + organization_list.index(organization)}',
            yong_specialists[1].target_distribution_count + yong_specialists[1].distribution_count, header_format
        )
        worksheet.write(
            f'H{7 + organization_list.index(organization)}',
            yong_specialists[1].target_distribution_count, header_format
        )
        worksheet.write(
            f'I{7 + organization_list.index(organization)}',
            yong_specialists[1].distribution_count, header_format
        )
        worksheet.write(
            f'J{7 + organization_list.index(organization)}',
            yong_specialists[2].target_distribution_count + yong_specialists[2].distribution_count, header_format
        )
        worksheet.write(
            f'K{7 + organization_list.index(organization)}',
            yong_specialists[2].target_distribution_count, header_format
        )
        worksheet.write(
            f'L{7 + organization_list.index(organization)}',
            yong_specialists[2].distribution_count, header_format
        )
        worksheet.write(
            f'M{7 + organization_list.index(organization)}',
            yong_specialists[3].target_distribution_count + yong_specialists[3].distribution_count, header_format
        )
        worksheet.write(
            f'N{7 + organization_list.index(organization)}',
            yong_specialists[3].target_distribution_count, header_format
        )
        worksheet.write(
            f'O{7 + organization_list.index(organization)}',
            yong_specialists[3].distribution_count, header_format
        )
        worksheet.write(
            f'P{7 + organization_list.index(organization)}',
            yong_specialists[4].target_distribution_count + yong_specialists[4].distribution_count, header_format
        )
        worksheet.write(
            f'Q{7 + organization_list.index(organization)}',
            yong_specialists[4].target_distribution_count, header_format
        )
        worksheet.write(
            f'R{7 + organization_list.index(organization)}',
            yong_specialists[4].distribution_count, header_format
        )
        worksheet.write(
            f'S{7 + organization_list.index(organization)}',
            yong_specialists[5].target_distribution_count + yong_specialists[5].distribution_count, header_format
        )
        worksheet.write(
            f'T{7 + organization_list.index(organization)}',
            yong_specialists[5].target_distribution_count, header_format
        )
        worksheet.write(
            f'U{7 + organization_list.index(organization)}',
            yong_specialists[5].distribution_count, header_format
        )
        worksheet.write(
            f'V{7 + organization_list.index(organization)}',
            yong_specialists[6].target_distribution_count + yong_specialists[6].distribution_count, header_format
        )
        worksheet.write(
            f'W{7 + organization_list.index(organization)}',
            yong_specialists[6].target_distribution_count, header_format
        )
        worksheet.write(
            f'X{7 + organization_list.index(organization)}',
            yong_specialists[6].distribution_count, header_format
        )
        worksheet.write(
            f'Y{7 + organization_list.index(organization)}',
            yong_specialists[7].target_distribution_count + yong_specialists[7].distribution_count, header_format
        )
        worksheet.write(
            f'Z{7 + organization_list.index(organization)}',
            yong_specialists[7].target_distribution_count, header_format
        )
        worksheet.write(
            f'AA{7 + organization_list.index(organization)}',
            yong_specialists[7].distribution_count, header_format
        )
        worksheet.write(
            f'AB{7 + organization_list.index(organization)}',
            yong_specialists[8].target_distribution_count + yong_specialists[8].distribution_count, header_format
        )
        worksheet.write(
            f'AC{7 + organization_list.index(organization)}',
            yong_specialists[8].target_distribution_count, header_format
        )
        worksheet.write(
            f'AD{7 + organization_list.index(organization)}',
            yong_specialists[8].distribution_count, header_format
        )
        worksheet.write(
            f'AE{7 + organization_list.index(organization)}',
            yong_specialists[9].target_distribution_count + yong_specialists[9].distribution_count, header_format
        )
        worksheet.write(
            f'AF{7 + organization_list.index(organization)}',
            yong_specialists[9].target_distribution_count, header_format
        )
        worksheet.write(
            f'AG{7 + organization_list.index(organization)}',
            yong_specialists[9].distribution_count, header_format
        )
        worksheet.write(
            f'AH{7 + organization_list.index(organization)}',
            yong_specialists[10].target_distribution_count + yong_specialists[10].distribution_count, header_format
        )
        worksheet.write(
            f'AI{7 + organization_list.index(organization)}',
            yong_specialists[10].target_distribution_count, header_format
        )
        worksheet.write(
            f'AJ{7 + organization_list.index(organization)}',
            yong_specialists[10].distribution_count, header_format
        )
        worksheet.write(
            f'F{7 + organization_list.index(organization)}',
            f'=SUM('
            f'G{7 + organization_list.index(organization)}+'
            f'J{7 + organization_list.index(organization)}+'
            f'M{7 + organization_list.index(organization)}+'
            f'P{7 + organization_list.index(organization)}+'
            f'S{7 + organization_list.index(organization)}+'
            f'V{7 + organization_list.index(organization)}+'
            f'Y{7 + organization_list.index(organization)}+'
            f'AB{7 + organization_list.index(organization)}+'
            f'AE{7 + organization_list.index(organization)}+'
            f'AH{7 + organization_list.index(organization)}'
            f')', header_format
        )
    worksheet.write(f'A{7 + len(organization_list)}', 'Итого:', bold_format)
    worksheet.write(f'B{7 + len(organization_list)}', f'=SUM(B7:B{6 + len(organization_list)})', header_format)
    worksheet.write(f'C{7 + len(organization_list)}', f'=SUM(C7:C{6 + len(organization_list)})', header_format)
    worksheet.write(f'D{7 + len(organization_list)}', f'=SUM(D7:D{6 + len(organization_list)})', header_format)
    worksheet.write(f'E{7 + len(organization_list)}', f'=SUM(E7:E{6 + len(organization_list)})', header_format)
    worksheet.write(f'F{7 + len(organization_list)}', f'=SUM(F7:F{6 + len(organization_list)})', header_format)
    worksheet.write(f'G{7 + len(organization_list)}', f'=SUM(G7:G{6 + len(organization_list)})', header_format)
    worksheet.write(f'H{7 + len(organization_list)}', f'=SUM(H7:H{6 + len(organization_list)})', header_format)
    worksheet.write(f'I{7 + len(organization_list)}', f'=SUM(H7:H{6 + len(organization_list)})', header_format)
    worksheet.write(f'J{7 + len(organization_list)}', f'=SUM(J7:J{6 + len(organization_list)})', header_format)
    worksheet.write(f'K{7 + len(organization_list)}', f'=SUM(K7:K{6 + len(organization_list)})', header_format)
    worksheet.write(f'L{7 + len(organization_list)}', f'=SUM(L7:L{6 + len(organization_list)})', header_format)
    worksheet.write(f'M{7 + len(organization_list)}', f'=SUM(M7:M{6 + len(organization_list)})', header_format)
    worksheet.write(f'N{7 + len(organization_list)}', f'=SUM(N7:N{6 + len(organization_list)})', header_format)
    worksheet.write(f'O{7 + len(organization_list)}', f'=SUM(O7:O{6 + len(organization_list)})', header_format)
    worksheet.write(f'P{7 + len(organization_list)}', f'=SUM(P7:P{6 + len(organization_list)})', header_format)
    worksheet.write(f'Q{7 + len(organization_list)}', f'=SUM(Q7:Q{6 + len(organization_list)})', header_format)
    worksheet.write(f'R{7 + len(organization_list)}', f'=SUM(R7:R{6 + len(organization_list)})', header_format)
    worksheet.write(f'S{7 + len(organization_list)}', f'=SUM(S7:S{6 + len(organization_list)})', header_format)
    worksheet.write(f'T{7 + len(organization_list)}', f'=SUM(T7:T{6 + len(organization_list)})', header_format)
    worksheet.write(f'U{7 + len(organization_list)}', f'=SUM(U7:U{6 + len(organization_list)})', header_format)
    worksheet.write(f'V{7 + len(organization_list)}', f'=SUM(V7:V{6 + len(organization_list)})', header_format)
    worksheet.write(f'W{7 + len(organization_list)}', f'=SUM(W7:W{6 + len(organization_list)})', header_format)
    worksheet.write(f'X{7 + len(organization_list)}', f'=SUM(X7:X{6 + len(organization_list)})', header_format)
    worksheet.write(f'Y{7 + len(organization_list)}', f'=SUM(Y7:Y{6 + len(organization_list)})', header_format)
    worksheet.write(f'Z{7 + len(organization_list)}', f'=SUM(Z7:Z{6 + len(organization_list)})', header_format)
    worksheet.write(f'AA{7 + len(organization_list)}', f'=SUM(AA7:AA{6 + len(organization_list)})', header_format)
    worksheet.write(f'AB{7 + len(organization_list)}', f'=SUM(AB7:AB{6 + len(organization_list)})', header_format)
    worksheet.write(f'AC{7 + len(organization_list)}', f'=SUM(AC7:AC{6 + len(organization_list)})', header_format)
    worksheet.write(f'AD{7 + len(organization_list)}', f'=SUM(AD7:AD{6 + len(organization_list)})', header_format)
    worksheet.write(f'AE{7 + len(organization_list)}', f'=SUM(AE7:AE{6 + len(organization_list)})', header_format)
    worksheet.write(f'AF{7 + len(organization_list)}', f'=SUM(AF7:AF{6 + len(organization_list)})', header_format)
    worksheet.write(f'AG{7 + len(organization_list)}', f'=SUM(AG7:AG{6 + len(organization_list)})', header_format)
    worksheet.write(f'AH{7 + len(organization_list)}', f'=SUM(AH7:AH{6 + len(organization_list)})', header_format)
    worksheet.write(f'AI{7 + len(organization_list)}', f'=SUM(AI7:AI{6 + len(organization_list)})', header_format)
    worksheet.write(f'AJ{7 + len(organization_list)}', f'=SUM(AJ7:AJ{6 + len(organization_list)})', header_format)


    # Закрытие файла
    workbook.close()
    output.seek(0)

    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="Young specialists.xlsx"'
    return response

def data_filter(start_month, end_month):
    organization_list = []
    article_list = []
    start_month_obj = datetime.datetime.strptime(start_month, '%Y-%m')
    end_month_obj = datetime.datetime.strptime(end_month, '%Y-%m')
    start_date = date(start_month_obj.year, start_month_obj.month, 1)
    end_date = date(end_month_obj.year, end_month_obj.month + 1, 1)\
        if end_month_obj.month < 12 else date(end_month_obj.year + 1, 1, 1)
    monthly_records = YoungSpecialistsView.objects.filter(
        start_date__lt=start_date, end_date__gt=end_date
    )
    articles = YoungSpecialistIndicators.objects.all()
    for article in articles:
        article_list.append(article.article_name)
    for organization in monthly_records.values('name').distinct():
         organization_list.append(organization['name'])
    return table(start_month_obj, end_month_obj, organization_list, article_list)