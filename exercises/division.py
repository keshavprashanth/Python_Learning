total_secs = 7684
hours = 7684//(60*60)
print(hours)
seconds_still_remaining = 7684%(60*60)
print(seconds_still_remaining)
minutes = seconds_still_remaining // 60
print(minutes)
seconds_finally_remaining = seconds_still_remaining % 60
print(seconds_finally_remaining)
print(hours, ':', minutes, ':', seconds_finally_remaining)

print(2*60*60+8*60+4)



a = int(input())
b = int(input())

print(a//b) # Integer division.
print(a/b)  # Float Division
print(a%b)  # Remainder
