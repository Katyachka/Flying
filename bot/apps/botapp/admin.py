from django.contrib import admin

from bot.apps.botapp.models import User, UserInfo, Plane, Flight, Seat, Ticket


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "user_info_id", "save_info")


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname", "sex", "phone_number", "email")


@admin.register(Plane)
class PlaneAdmin(admin.ModelAdmin):
    list_display = ("id", "model", "passengers", "plane_layout")


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "plane_id", "departure", "arrival", "departure_date_time", "arrival_date_time",
                    "duration", "cost_base", "cost_regular", "cost_plus")


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ("id", "number", "user_info_id", "flight_id")


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "flight_id", "plane_id", "seat_id")
