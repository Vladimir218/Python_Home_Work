duration = int(input("Введите временной интервал (целое число) в секундах:"))
_seconds = 0
_minutes = 0
_hour = 0
_years = 0
if duration < 60:
    if len(str(duration)) < 2:
        print("<0", duration, ">сек", sep="")
    else:
        print("<", duration, ">сек", sep="")
elif duration < 3600:
    _minutes = duration//60
    _seconds = duration-_minutes*60
    if len(str(_minutes)) < 2:
        _minutes = "0" + str(_minutes)
    if len(str(_seconds)) < 2:
        _seconds = "0" + str(_seconds)
    print("<", _minutes, ">мин<", _seconds, ">сек", sep="")
elif duration < 3600*24:
    _hour = duration // 3600
    duration = duration - _hour * 3600
    _minutes = duration // 60
    _seconds = duration-_minutes * 60
    if len(str(_hour)) < 2:
        _hou = "0" + str(_hour)
    if len(str(_minutes)) < 2:
        _minutes = "0" + str(_minutes)
    if len(str(_seconds)) < 2:
        _seconds = "0" + str(_seconds)
    print("<", _hour, ">час<", _minutes, ">мин<", _seconds, ">сек", sep="")
