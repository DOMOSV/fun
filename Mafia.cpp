using namespace std;
#include <iostream>
#include <vector>
#include <string>
#include "windows.h"
void printArray(vector<string> sVector)
{
	cout << "Массив: ";
	for (int i = 0; i < sVector.size(); i++)
		cout << sVector[i] << " ";
}
int main()
{
	setlocale(0, "");
	vector <string> Uchastniki = {"da","net","huy","kal","gabno","penis","penis", "penis", "penis","penis","penis", "penis", "penis", "penis", "penis", "penis", 
	"penis", "penis", "penis", "penis", };
	vector <string> roly{"Mafia","Doc","Komis","Mir"};
	int mafia, doc=1, police=1, mir,kolvo_uchastnikov;
	cout << "Введите количество участников: ";
	cin >> kolvo_uchastnikov;
	if (kolvo_uchastnikov < 6) {
		cout << "Недостаточно игроков ";
		return 0;
	}
	mafia = kolvo_uchastnikov / 4;
	mir = kolvo_uchastnikov	- mafia - doc - police;
	bool first_true = true;
	while (first_true)
	{
		char menu;
		cout << "1.Добавление участника\n"
			 << "0.Выход: ";
		cin >> menu;
		string Uchastnik_to_pushback;
		switch (menu)
		{
		case'1':
			cout << "Введите имя участника: ";
			cin >> Uchastnik_to_pushback;
			Uchastniki.push_back(Uchastnik_to_pushback);
			break;
		case'2':
			printArray(Uchastniki);
			break;
		case'0':
			if (Uchastniki.size() < kolvo_uchastnikov) {
				cout << "Количество участников указанных в начале меньше количества внесенных участников \n";
				break;

			}
			if(Uchastniki.size() > kolvo_uchastnikov) {
				cout << "Перебор ";
				exit(0);

			}
			if (Uchastniki.size() == kolvo_uchastnikov) {
				first_true = false;
				break;
			}
		default:
			cout << "Неверный ввод \n";
			break;
		}
	}
	string result;
	//roly.erase(remove(roly.begin(), roly.end(),элемент для удаления), v.end());
	int min=0, max=roly.size()-1;
	for (int i = 0; i < Uchastniki.size(); i++) {
		bool second_true = true;
		while (second_true)
		{
			srand(time(0));
			int nomer_roly = rand() % (max - min + 1) + min;
			if (mafia == 0 || doc == 0 || police == 0 || mir == 0)
			{
				if (mafia == 0 && nomer_roly == 0) {
					continue;
				}
				if (doc == 0 && nomer_roly == 1) {
					continue;
				}
				if (police == 0 && nomer_roly == 2) {
					continue;
				}
				if (mir == 0 && nomer_roly == 3) {
					continue;
				}
			}
			if (roly[nomer_roly] == "Mafia") {
				if (mafia != 0) {
					result = Uchastniki[i] + " " + roly[nomer_roly] + "\n";
					mafia--;
					second_true = false;
					continue;
				}
				else
				{
					continue;
				}
			}
			if (roly[nomer_roly] == "Doc") {
				if (doc != 0) {
					result = Uchastniki[i] + " " + roly[nomer_roly] + "\n";
					doc--;
					second_true = false;
					continue;
				}
				else
				{
					continue;
				}
			}
			if (roly[nomer_roly] == "Komis") {
				if (police != 0) {
					result = Uchastniki[i] + " " + roly[nomer_roly] + "\n";
					police--;
					second_true = false;
					continue;
				}
				else
				{
					continue;
				}
			}
			if (roly[nomer_roly] == "Mir") {
				if (mir != 0) {
					result = Uchastniki[i] + " " + roly[nomer_roly] + "\n";
					mir--;
					second_true = false;
					continue;
				}
				else
				{
					continue;
				}
			}
		}
	cout << result;
	}
}
