#%%
%pwd
# %%
from time import sleep

%time sleep(0.1)
# %%
%%time
for i in range(3):
    sleep(0.1)
# %%
!ls /var/log
# %%
dirname = '/var/log'
files = !ls $dirname
print(f'{len(files)} files at {dirname}')

# %%
