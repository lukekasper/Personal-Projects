// illustrates concepts of inheritance and pointers
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
};

class CRectangle: public CPolygon
{
	public:
		int area()
		{
			return (width * height);
		}
};

class CTriangle: public CPolygon
{
	public:
		int area()
		{
			return (width * height / 2);
		}
}; 

int main ()
{
	CRectangle rectangle;
	CTriangle triangle;

	CPolygon * ptr_polygon1 = &rectangle; // pointer to address of rectangle object, but only refers to members inherited from CPolygon
	CPolygon * ptr_polygon2 = &triangle;

	ptr_polygon1->setup(2,2);
	ptr_polygon2->setup(2,2);

	cout << rectangle.area () << endl;
	cout << triangle.area () << endl;

	return 0;
}