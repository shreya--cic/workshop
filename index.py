def cuboid_surface_area(l,b,h):
	area = 2*(l*b) +  2*(b*h)
	return area

def cuboid_volume(l,b,h):
	volume = l*b*h
	return volume
print cuboid_volume(1,1,1)