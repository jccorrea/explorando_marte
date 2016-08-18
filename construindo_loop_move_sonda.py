
# coding: utf-8

# In[64]:

x, y, d = 1, 2, "N"


# In[61]:

def move_space_probe(coo_x, coo_y, direction,probe_inst):
    print ("the current position is {}, {}, {}".format(coo_x, coo_y, direction))
    


# In[63]:

move_space_probe(x,y,d)


# In[67]:

nasa_instr = "LLMMDLM"


# In[68]:

def probe_next_d(current_direction,nasa_inst):
    instr_list = list(nasa_instr)
    return next_direction


# In[69]:

instr_list = list(nasa_instr)


# In[78]:

base_d = list("NESW")


# In[79]:

print (base_d)


# In[96]:

for i in range(len(instr_list)):
    curr_ind = base_d.index(d)
    if i!="M":
    #left commands
       if i=="L" and curr_ind in (1,2,3):
        new_d = instr_list[curr_ind - 1]
        else: 
            new_d = instr_list[4]
    else:
        print ("apenas movendo a frente")
print (i)


# In[91]:

"S" in base_d


# In[92]:

base_d.index("S")


# In[ ]:



