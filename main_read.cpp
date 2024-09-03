#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	string sname;
	int score1, score2;
	int N, total;
	double avg;

	ifstream ifs;
	ifs.open ("students.txt");
	if (!ifs) {
		cerr << "Error: open file \n";
		exit (0);
	}
	ifs >> N;
	for (int i=0; i=N;i++)

		ifs >> sname >> score1 >>score2;
		cout << "Students Name: " <<sname << "scores" << score1 << "\t" << score2 ;
		cout << "\tTotal" << total << "\tAverage" << avg;
}