def bucle(count,image,l):
    count+=1
    if count>=len(l):
        image-=1
        if image<1:
            count=image=0
    else:
        image+=1
    return count,image
