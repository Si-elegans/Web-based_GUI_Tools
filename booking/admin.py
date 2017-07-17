from django.contrib import admin

from booking.models import \
    Reservation, \
    PE_results, \
    RB_results, \
    share_pe_results, \
    share_rb_results, \
    PE_results_files
    
admin.site.register(Reservation)
admin.site.register(PE_results)
admin.site.register(RB_results)
admin.site.register(share_pe_results)
admin.site.register(share_rb_results)
admin.site.register(PE_results_files)
#
