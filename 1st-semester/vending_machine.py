kaffee = 1.80
tee = 1.75
kakao = 2.00
wasser = 1.00

while True:
    z_getränk = int(input("""Geben Sie bitte an, welches Getränk Sie gerne hätten
                      Kaffee    = 1
                      Tee       = 2
                      Kakao     = 3
                      Wasser    = 4
                      """))
#alte Lösung if not (z_getränk == 1 or z_getränk == 2 or z_getränk == 3 or z_getränk == 4):
#            print("UNBEKANNTER FEHLER, BITTE VERSUCHEN SIE ES NOCHMAL ODER RENNEN SIE SCHREIEND IM KREIS");
    if not z_getränk in [1,2,3,4]:
        print("UNBEKANNTER FEHLER, BITTE VERSUCHEN SIE ES NOCHMAL ODER RENNEN SIE SCHREIEND IM KREIS")
        continue
    break

while True:
    m_getränk = int(input("Geben Sie bitte die Menge an Getränk an, die Sie gerne hätten\n"))
#alte Lösung if not (z_getränk == 1 or z_getränk == 2 or z_getränk == 3 or z_getränk == 4):
#            print("UNBEKANNTER FEHLER, BITTE VERSUCHEN SIE ES NOCHMAL ODER RENNEN SIE SCHREIEND IM KREIS");
    if m_getränk <1:
        print("UNBEKANNTER FEHLER, BITTE VERSUCHEN SIE ES NOCHMAL ODER RENNEN SIE SCHREIEND IM KREIS")
        continue
    break
