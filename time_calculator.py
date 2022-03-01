def add_time(start, duration,day=None):
  start_arr = start.split(":")
  start_arr[1] = start_arr[1].split(" ")
  dur_arr = duration.split(":")
  start_hr, start_min = int(start_arr[0]),int(start_arr[1][0])
  dur_hr, dur_min = int(dur_arr[0]),int(dur_arr[1])

  DAYS = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
  
  # add time elapsed to current time, using miniutes as base unit
  total_min = (60*start_hr) + start_min + (60*dur_hr) +  dur_min

  # convert total_min to military time to not loose track of AM/PM
  if start_hr == 12:
    total_min -= 720
  if "PM" in start_arr[1]:
    total_min +=720

  #1440 min is 24 hrs
  num_days = total_min // 1440
  #get the new mil time in minutes by subtracting elapsed days, then convert to hrs
  new_hr = (total_min - (num_days*1440))//60
  #extract remainder of min that don't make up a full hour
  new_min = (total_min%60)

#if day is provided, calculate new day using positions in tuple DAY. 
  if day:
    day_index = DAYS.index(day.capitalize())
    new_day = f', {DAYS[(num_days + day_index)%7]}'
  else:
    new_day =''
  
  if num_days < 2:
    days_later = ''
    if num_days > 0:
      days_later = ' (next day)'
  else:
    days_later = f' ({num_days} days later)'

  # convert back to cvilian Time

  if new_hr >= 12:
    # if new hour equals 12,ensure AM gets changed to PM, if greater than 12 convert to civilian time
    if new_hr != 12:
      new_hr-=12
    new_time = f'{new_hr}:{new_min:0>2} PM{new_day}{days_later}'
  else:
   # 00 in miliatry time equals 12am in civ time
   if new_hr == 0:
      new_hr = 12
  #all other AM hrs are same, no conversion needed
   new_time =  f'{new_hr}:{new_min:0>2} AM{new_day}{days_later}'

  return new_time