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