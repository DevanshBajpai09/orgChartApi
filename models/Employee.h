// models/Employee.h
#pragma once
#include <string>

class Employee {
public:
    Employee(const std::string& name, int id);
    std::string getName() const;
    int getId() const;
    void rename(const std::string& newName);

private:
    std::string name_;
    int id_;
};
