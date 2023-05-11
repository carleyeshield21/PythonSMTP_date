# import smtplib
#
# aking_email = 'carleyeshield21@gmail.com'
# password = 'qtqwejktaeqkldps'
#
# kuneksyon = smtplib.SMTP('smtp.gmail.com')
# kuneksyon.starttls()
# kuneksyon.login(user=aking_email, password=password)
# kuneksyon.sendmail(from_addr=aking_email, to_addrs='rus_greg@yahoo.com', msg='Subject:Hilaw o Hinog\n\nHinog o Hilaw')
# kuneksyon.close()

# import smtplib
#
# aking_email = 'carleyeshield21@gmail.com'
# password = 'qtqwejktaeqkldps'
#
# with smtplib.SMTP('smtp.gmail.com') as kuneksyon:
#     kuneksyon.starttls()
#     kuneksyon.login(user=aking_email, password=password)
#     kuneksyon.sendmail(from_addr=aking_email, to_addrs='rus_greg@yahoo.com', msg='Subject:Hilaw o Hinog\n\nHinog o Hilaw')

import smtplib

aking_email = 'rus_greg@yahoo.com'
password = 'nwmzjrnrejtiymdy'

with smtplib.SMTP('smtp.mail.yahoo.com') as kuneksyon:
    kuneksyon.starttls()
    kuneksyon.login(user=aking_email, password=password)
    kuneksyon.sendmail(from_addr=aking_email, to_addrs='carleyeshield21@gmail.com', msg='Subject:Hilaw o Hinog\n\nHinog o Hilaw')