#include <iostream>

using namespace std;

int main()
{
	for (char i = 'a'; i <= 'z'; i++)
	{
		cout << "'" << i << "'" << ", ";
	}

	for (char i = 'A'; i <= 'Z'; i++)
	{
		cout << "'" << i << "'" << ", ";
	}

	cout << endl;
}