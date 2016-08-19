
# coding: utf-8

# In[222]:

x, y, d = 1, 2, "S"


# In[225]:

def move_space_probe(coo_x, coo_y, direction,probe_inst):
    print ("Now, exploring the position  ({}, {}, {})".format(coo_x, coo_y, direction))
    


# In[203]:

move_space_probe(x,y,d,nasa_instr)


# In[219]:

nasa_instr = "DDMM"


# In[206]:

def probe_next_d(current_direction,nasa_inst):
    instr_list = list(nasa_instr)
    return next_direction


# In[214]:

instr_list = list(nasa_instr)


# In[208]:

base_d = list("NESW")


# In[213]:

print (base_d)


# In[226]:

# verifica posicao atual
print ("Step 1 - The current position is ({}, {}, {})".format(x, y, d))
print ("Step 2 - Reading the NASA instruction file")
# entra com a direcao(posicao corrente da sonda) e a saida é a nova posicao da sonda

for i in range(len(instr_list)):
    curr_ind = base_d.index(d)
    if instr_list[i] != "M":
    #left commands
        if instr_list[i] =="L" and curr_ind in (1,2,3):
            d = base_d[curr_ind - 1]
        elif instr_list[i] =="L" and curr_ind ==0 : 
            d = base_d[3]
    #right commands
        elif instr_list[i] =="D" and curr_ind in (0,1,2):
            d = base_d[curr_ind + 1]
        else: 
            d = base_d[0]
        move_space_probe(x,y,d,nasa_instr)
    else:
        print ("Moving foward in the previous direction ")


# In[91]:

"S" in base_d


# In[92]:

base_d.index("S")


# In[ ]:



