<<<<<<< HEAD
def cuboid_surface_area(l,b,h):
	area = 2*(l*b) +  2*(b*h)
	return area

def cuboid_volume(l,b,h):
	volume = l*b*h
	return volume

print cuboid_volume(1,1,1)
print cuboid_surface_are(1,1,1)

print cuboid_volume(1,3,1)
print cuboid_surface_are(3,1,1)
=======
def main():
<<<<<<< HEAD
pass

def cube_volume():
	l=int(raw_input('enter the side'))
	volume=l*l*l
	print 'volume is '
	print volume
	return volume

def cube_surface_area():
	pass

def cuboid_volume():
	l=int(raw_input('enter the length '))
	b=int(raw_input('Enter the breadth'))
	h=int(raw_input('Enter the height '))
	cuboid_volume=l*b*h
	print 'volume is'
	print cuboid_volume
	return cuboid_volume
        

def cuboid_surface_area();
	pass
=======
    print('menu :')
    print('Press')
    print ('1 for cube volume')
    print ('2 for cube surface area')
    print ('3 for cuboid volume')
    print ('4 for cuboid surface area')
    print ('5 to exit')

    ch=input('enter the option number')
   

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
        pass

main()
    

>>>>>>> f55ac429891c2b40a10cb054f789383e48acdccd

>>>>>>> 9f3b3f8d384c381b9ece2dbd79213d73c4982a8d
