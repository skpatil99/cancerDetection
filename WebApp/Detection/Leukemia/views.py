from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from .forms import PatientDetailForm
from .models import PatientDetail

from .FNNTestingImageProcessing2 import imageProcessing
from .loadModelKeNet import FNN

from .CNNloader import CNN

from .KNNloadModel import KNN
from .svm_code2 import SVM
# Create your views here.

def index(request):
    return render(request,'index.html')

def verify(request):
    if request.method == 'POST':
        form = PatientDetailForm(request.POST,request.FILES)
        ID = request.POST.get('PatientID')
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            Latest_Entry = PatientDetail.objects.get(PatientID=ID)
            print("Latest_Entry ::",Latest_Entry.BloodImage)
            imageProcessing(Latest_Entry.BloodImage)

            outputLabel = {"Cancerous":1 , "Non-Cancerous":0}
            output = []
            result_KNN = KNN()
            output.append(outputLabel[result_KNN])
            result_SVM = SVM()
            output.append(outputLabel[result_SVM])
            result_CNN = CNN(Latest_Entry.BloodImage)
            output.append(outputLabel[result_CNN])
            result_FNN = FNN()
            output.append(outputLabel[result_FNN])

            print(Latest_Entry.PatientID)

            if(output.count(1) > output.count(0)):
                Latest_Entry.Result = "Cancerous"
                Latest_Entry.save()
                print("Cancerous")
            else:
                Latest_Entry.Result = "Non-Cancerous"
                Latest_Entry.save()
                print("Non-Cancerous")





            context={"Latest_Entry":Latest_Entry,"result_FNN":result_FNN,"result_KNN":result_KNN,"result_SVM":result_SVM,"result_CNN":result_CNN}
            return render(request,'verify.html',context)
    else:
        form = PatientDetailForm()

    context = {'form': form}
    return render(request,'index.html',context)

def Phase1(request):
    return render(request,'verify.html')
