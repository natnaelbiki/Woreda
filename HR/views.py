from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Staff
from .forms import StaffForm
from django.contrib.auth.decorators import login_required
from account.decorators import role_required
import io
import xlsxwriter
from django.http import HttpResponse

@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def staff_list(request):
    try:
        if 'download' in request.GET:
            queryset = Staff.objects.all()

            if queryset.exists():
                # Create an in-memory Excel file
                output = io.BytesIO()

                # Create a new workbook and add a worksheet
                workbook = xlsxwriter.Workbook(output)
                worksheet = workbook.add_worksheet()

                # Define the header row
                headers = ['ስም ከነአያት በአማርኛ', 'ስም ከነአያት በእንግሊዘኛ', 'ፆታ']  # Replace with your model fields

                # Write the headers to the worksheet
                for col, header in enumerate(headers):
                    worksheet.write(0, col, header)

                # Write the model data to the worksheet
                for row, obj in enumerate(queryset, start=1):
                    worksheet.write(row, 0, obj.full_name_amh)
                    worksheet.write(row, 1, obj.full_name_eng)
                    worksheet.write(row, 2, obj.gender)
                    # Add more columns as needed

                # Close the workbook
                workbook.close()

                # Set response headers for Excel file download
                response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = 'attachment; filename="staff_list_data.xlsx"'
                return response
            else:
                return render(request, 'failed.html')
        else:
            staffs = Staff.objects.all().order_by('full_name_eng')
            paginator = Paginator(staffs, 10)  # Show 10 staffs per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'staff/staff_list.html', {'page_obj': page_obj})
    except Exception as e:
        return render(request, 'error_page.html', {'e': e})



@login_required
def add_staff(request):
    try:
        if request.method == 'POST':
            form = StaffForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('staff_list')
        else:
            form = StaffForm()
        return render(request, 'staff/add_staff.html', {'form': form})
    except Exception as e:
        return render(request, 'error_page.html', {'e': e})




#@role_required()
@login_required
def edit_staff(request, pk):
    try:
        staff = get_object_or_404(Staff, pk=pk)
        if request.method == 'POST':
            form = StaffForm(request.POST, instance=staff)
            if form.is_valid():
                form.save()
                return redirect('staff_list')
        else:
            form = StaffForm(instance=staff)
        return render(request, 'staff/edit_staff.html', {'form': form})
    except Exception as e:
        return render(request, 'error_page.html', {'e': e})






def delete_staff(request, pk):
    try:
        staff = get_object_or_404(Staff, pk=pk)
        if request.method == 'POST':
            staff.delete()
            return redirect('staff_list')
        return render(request, 'staff/delete_staff.html', {'staff': staff})
    except Exception as e:
        return render(request, 'error_page.html', {'e': e})

