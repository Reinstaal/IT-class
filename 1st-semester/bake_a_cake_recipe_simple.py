
#print   ( f"Bro Torten sind literally besser butt sure hier hast du deine Mengen für {M_Kuchen} Zuckerkuchen.\n    Eier: {3*M_Kuchen}\n    Mehl: {300*M_Kuchen}g\n    Zucker: {300*M_Kuchen}g\n    Milch: {300*M_Kuchen}mL\n" )

while True:
    m_kuchen = int(input("\nHeiliger Bruder im Himmel, wie viel Kuchen möchten Sie backen??\n"))
    print("\n\n\n\n")
    m_eier = m_kuchen * 3
    m_mehl = m_kuchen * 300
    m_zucker = m_kuchen * 300
    m_milch = m_kuchen * 300
    print (f"""Sie benötigen für {m_kuchen} Kuchen folgende Menge an Zutaten:
           Eier:    {m_eier}
           Mehl:    {m_mehl}g
           Zucker:  {m_zucker}g
           Milch:   {m_milch}mL\n"""
           )

    if input("Möchten Sie aufhören? Wir bei Stiftung Kuchentest geben auf bevor wir es versuchen!\n") == "ja":
        break