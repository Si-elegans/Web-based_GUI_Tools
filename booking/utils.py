from booking.models import Reservation

def give_me_next_reservation ():
    #The models meta expresses that they should be ordered by created date so I don't re-order it
    reservations =Reservation.objects.all()
    superuser=False
    for reservation in reservations:
        creators=reservation.creator.all()
        for creator in creators:
            if creator.is_superuser:
                superuser=True               
        if superuser==True:
            if reservation.status == Reservation.WAITING:                
                return reservation            
    #GE: Implement logic to consider fair usage within users with many reservations, taking into account past usage
    #and load
    for reservation in reservations:
        if reservation.status==Reservation.WAITING:
            return reservation
    #v1.0 Once all waiting have been runned go for WAITING_RESUME
    for reservation in sorted (reservations, key=lambda Reservation:Reservation.start_time):
        if reservation.status==Reservation.WAITING_RESUME:
            return reservation        
    return None

