#include<iostream>
using namespace std;

class IntArray{
    private:
        int* m_ptr{nullptr};
        int m_size{0};

    public:
        IntArray() = default;

        explicit IntArray(int size){
            if (size != 0){
                m_ptr = new int[size]{};
                m_size = size;
            }
        }

        ~IntArray() {
            delete[] m_ptr;
        }

        int Size() const {
            return m_size;
        }

        bool IsEmpty() const {
            return (m_size == 0);
        }

        int& operator[](int index){
            return m_ptr[index];
        }

};


int main(){
    using std::cout;
    IntArray a{3};
    cout << "Setting a[0] = 10 \n";
    a[0] = 10;
    cout << "a[0] is " << a[0] << "\n";
}