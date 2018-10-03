while True:
    v = input("Windgeschwindigkeit als float eingeben.")
    t = input("Tatsächliche Temparatur als float eingeben.")
    try:
        v = float(v)
        t = float(t)
        w_old = 33+(0.478+0.237*(v)**0.5-0.0124*v)*(t-33)
        w_new = 13.12+0.6215*t-11.37*v**0.16+0.3965*t*v**0.16
        print("w_old", w_old)
        print("w_new", w_new)
        break
    except:
        if((type(v) is not float) or (type(t) is not float)):
            print ("Bitte Float einfügen")


