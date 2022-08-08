#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

bool st(pair<int,int> p1,pair<int,int> p2)
{
	if(p1.second == p2.second)
		return p1.first < p2. first;//
	return p1.second < p2.second;
}
int main()
{
	pair<int, int> p;
	vector<pair<int,int>> v;
	int num;
	int res = 0;
	int index = 0, current = 0;
	scanf("%d", &num);
	for (int i = 0; i < num; i++)
	{
		scanf("%d %d", &p.first, &p.second);
		v.push_back(p);
	}
	sort(v.begin(),v.end(),st);
	while (true)
	{
		if (index < num)
		{
			if (current <= v[index].first)
			{
				current = v[index].second;
				res++;
			}
			index++;
		}
		else break;
	}
	printf("%d", res);
	return 0;
}