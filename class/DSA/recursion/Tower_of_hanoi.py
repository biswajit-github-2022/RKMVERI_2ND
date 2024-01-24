def tower(disks,source,temporary,destination):
    if disks>0:
        tower(disks-1,source,destination,temporary)
        print(f"move disk from {source} to {destination}")
        tower(disks-1,temporary,source,destination)
    
tower(6,"A","B","C")
