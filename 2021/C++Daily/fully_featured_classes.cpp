#include <cstdio>
#include <iostream>

struct YearKeeper
{
    void add_year(){
        year++;
    }

    int get_year(){
        return year;
    }

    unsigned int set_year(int new_year){
        if (new_year > 2021) return 0;
        else year = new_year;
        return 1;
    }
    private:
        int year;
};

int main(){
    YearKeeper yearkeeper;
    std::cout << yearkeeper.set_year(2022) << "\n";
    std::cout << yearkeeper.get_year() << "\n";
    std::cout << yearkeeper.set_year(2019) << "\n";
    std::cout << yearkeeper.get_year() << "\n";
}