// Illustrates concept of virtual functions, polymorphism, and virtual base classes

#include <iostream>
using namespace std;

class CPolygon
{
	protected:
		int width, height;
	public:
		void setup (int first, int second)
		{
			width= first;
			height= second;
		}
        // define area function in base class as virtual so that pointers to base class can call this method
		virtual int area() = 0;     // setting the virtual method = 0 makes this an abstract base class
        void onscreen(void)
		{
			cout << this->area() << endl;
		}
}

class CRectangle: public CPolygon
{
	public:
		int area(void)  // override area function in subclass to make it specific to a rectangle, must add extra void in derived classes of abstract base class
		{
			return (width * height);
		}
}; 

class CTriangle: public CPolygon
{
	public:
		int area(void)  // same for trianlge, must add extra void in derived classes of abstract base class
		{
			return (width * height / 2);
		}
}; 

int main ()
{
	CRectangle rectangle;
	CTriangle triangle;

	CPolygon * ptr_polygon1 = &rectangle;   // create pointers to refer to class object addresses
	CPolygon * ptr_polygon2 = &triangle;

	ptr_polygon1->setup(2,2);
	ptr_polygon2->setup(2,2);

	ptr_polygon1->onscreen();  // pointers can now invoke correct method based on what object they refer to
	ptr_polygon2->onscreen();

	return 0;
}