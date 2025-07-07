#include <gtest/gtest.h>
#include "models/Employee.h"

TEST(EmployeeTest, ConstructorStoresValuesCorrectly) {
    Employee emp("Alice", 101);
    EXPECT_EQ(emp.getName(), "Alice");
    EXPECT_EQ(emp.getId(), 101);
}

TEST(EmployeeTest, RenameUpdatesName) {
    Employee emp("Bob", 102);
    emp.rename("Robert");
    EXPECT_EQ(emp.getName(), "Robert");
}
