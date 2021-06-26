#include <cstdio>
#include <iostream>

struct YearKeeper
{
    YearKeeper(int year_in){
        if(set_year(year_in) == 0){
            year = 2021;
        }
        else year = year_in;
    }
    void add_year(){
        year++;
    }

    unsigned int get_year(){
        return year;
    }

    unsigned int set_year(int new_year){
        if (new_year > 2021) return 0;
        else year = new_year;
        return 1;

    
    }

      ~YearKeeper(){
          std::cout << "\nDestructor question: What is your name? ";
          std::cin >> my_name;
          std::cout << "Cleaning up the class now " << my_name;
    }
    private:
        int year{};
        char my_name[64]{};
    
};

int main(){
    YearKeeper clock{ 2021 };
    std::cout << clock.get_year();
}