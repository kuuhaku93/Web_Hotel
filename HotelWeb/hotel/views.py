from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from .models import Hotel,User
from .forms import AddHotel,AddUser

class Index(View):
    def get(self,request):
        return render(request,"hotel/index.html")
    
class DanhSach(View):
    def get(seft,request):
        h = Hotel.objects.filter(Status=True)
        context={"hotel":h}
        return render(request,"hotel/danhsach.html",context)
    
class SapXep(View):
    def get(seft,request):
        h = Hotel.objects.filter(Status=True)
        context={"hotel":h}
        return render(request,"hotel/sapxep.html",context)

class SapXepTheoTen(View):
    def get(seft,request):
        h = Hotel.objects.filter(Status=True).order_by('HotelName')
        context={"hotel":h}
        return render(request,"hotel/sapxep.html",context)

class SapXepTheoRating(View):
    def get(seft,request):
        h = Hotel.objects.filter(Status=True).order_by('-Rating')
        context={"hotel":h}
        return render(request,"hotel/sapxep.html",context)
    
class ViTri(View):
    def get(seft,request):
        v=Hotel.objects.values('Location').filter(Status=True).distinct()
        h = Hotel.objects.filter(Status=True)
        context={"hotel":h,"vitri":v,"vitridachon":"Tất cả"}
        return render(request,"hotel/vitri.html",context)
    
    def post(seft,request):
        vc=request.POST.get('city')
        v=Hotel.objects.values('Location').filter(Status=True).distinct()
        if request.POST.get('city')=="Tất cả":
            return redirect('vitri')
        h = Hotel.objects.filter(Location=request.POST.get('city'),Status=True)
        context={"hotel":h,"vitri":v,"vitridachon":vc}
        return render(request,"hotel/vitri.html",context)


class PhongTrong(View):
    def get(seft,request):
        h = Hotel.objects.filter(RoomAvilable__gt=0,Status=True)
        context={"hotel":h}
        return render(request,"hotel/phongtrong.html",context)

class DatPhong(View):
    def get(seft,request):
        h = Hotel.objects.filter(Status=True)
        u = User.objects.filter(Status=True)
        context={"hotel":h,"user":u}
        return render(request,"hotel/datphong.html",context)
    
class NewHotel(View):
    def get(self,request):
        a=AddHotel
        return render(request,"hotel/newhotel.html",{"f":a})

    def post(self,request):
        newhotel=AddHotel(request.POST)
        if newhotel.is_valid():
            newhotel.save()
            return redirect('danhsach')
        else:
            return HttpResponse('THÊM KHÁCH SẠN THẤT BẠI')

class DeleteHotel(View):
    def get(seft,request,hotel_id):
        h = Hotel.objects.get(pk=hotel_id)
        #h.Status=False
        h.save()
        return redirect('danhsach')
    
class NewUser(View):
    def get(self,request):
        a=AddUser
        return render(request,"hotel/newuser.html",{"f":a})

    def post(self,request):
        newuser=AddUser(request.POST)
        if newuser.is_valid():
            h=Hotel.objects.get(HotelName=(newuser.cleaned_data["BookingRoom"]).HotelName)
            h.RoomAvilable-=1
            h.save()
            newuser.save()
            return redirect('datphong')
        else:
            return HttpResponse('ĐẶT PHÒNG THẤT BẠI')

class DeleteUser(View):
    def get(seft,request,user_id):
        u = User.objects.get(pk=user_id)
        u.Status=False
        h=Hotel.objects.get(HotelName=u.BookingRoom)
        h.RoomAvilable+=1
        h.save()
        u.save()
        return redirect('datphong')