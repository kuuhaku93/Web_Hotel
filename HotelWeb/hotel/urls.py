from django.urls import path

from . import views

urlpatterns = [
    path("",views.Index.as_view(),name="index"),
    path("danhsach",views.DanhSach.as_view(),name="danhsach"),
    path("danhsach/them",views.NewHotel.as_view(),name="themdanhsach"),
    path("danhsach/xoa/hotel_id=<int:hotel_id>",views.DeleteHotel.as_view(),name="xoadanhsach"),
    path("sapxep",views.SapXep.as_view(),name="sapxep"),
    path("sapxep/theoten",views.SapXepTheoTen.as_view(),name="sapxeptheoten"),
    path("sapxep/theorating",views.SapXepTheoRating.as_view(),name="sapxeptheorating"),
    path("vitri",views.ViTri.as_view(),name="vitri"),
    path("phongtrong",views.PhongTrong.as_view(),name="phongtrong"),
    path("datphong",views.DatPhong.as_view(),name="datphong"),
    path("datphong/them",views.NewUser.as_view(),name="themdatphong"),
    path("datphong/xoa/user_id=<int:user_id>",views.DeleteUser.as_view(),name="xoadatphong")
]