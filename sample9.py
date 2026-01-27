#時間を計る

import time

start=time.time()
print(start)  # UNIX時間表示

for n in range(10):
    print(n)
    
end=time.time()
print(end)    # UNIX時間表示

diff=end-start
print(diff)
