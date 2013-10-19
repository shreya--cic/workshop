def main(ch):
    if ch==1:
        cube_volume()
    elif ch==2:
        cube_surface_area()
    elif ch==3:
        cuboid_volume()
    elif ch==4:
        cuboid_surface_area()
    else:
        print('Exiting...')
    
    


print('menu: Press')
print ('1 for cube volume')
print ('2 for cube surface area')
print ('3 for cuboid volume')
print ('4 for cuboid surface area')
print ('5 to exit')


ch=input('enter the option number')
main(ch);
    
