// models/Employee.cc
#include "Employee.h"

Employee::Employee(const std::string& name, int id)
    : name_(name), id_(id) {}

std::string Employee::getName() const {
    return name_;
}

int Employee::getId() const {
    return id_;
}

void Employee::rename(const std::string& newName) {
    name_ = newName;
}
