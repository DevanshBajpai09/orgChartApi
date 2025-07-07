#include <gtest/gtest.h>
#include "../models/Dummy.h"

TEST(DummyTest, AddWorks) {
    Dummy d;
    EXPECT_EQ(d.add(3, 4), 7);
}

TEST(DummyTest, IsEvenWorks) {
    Dummy d;
    EXPECT_TRUE(d.isEven(2));
    EXPECT_FALSE(d.isEven(3));
}
