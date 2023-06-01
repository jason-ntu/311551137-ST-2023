// (a) How many mutants are there?
// 237

// (b) How many test cases do you need to kill the non-equivalent mutants?
// 10

// (c) What mutation score were you able to achieve before analyzing for equivalent mutants?
// 88.0%

// (d) How many equivalent mutants are there?
// 27

import org.junit.Assert;
import org.junit.Test;

public class CalTest {
    // Normal year
    @Test
    public void test1() {
        Assert.assertEquals(59, Cal.cal(1, 1, 3, 1, 2022));
    }

    // leap year
    @Test
    public void test2() {
        Assert.assertEquals(121, Cal.cal(1, 1, 5, 1, 2020));
    }

    // (m100 == 0) && (m400 != 0)
    @Test
    public void test3() {
        Assert.assertEquals(181, Cal.cal(1, 1, 7, 1, 2100));
    }

    // int m400 = --year % 400;
    @Test
    public void test4() {
        Assert.assertEquals(121, Cal.cal(1, 1, 5, 1, 2000));
    }

    // numDays = --day2 - day1;
    @Test
    public void test5() {
        Assert.assertEquals(30, Cal.cal(1, 1, 1, 31, 2022));
    }

    // if (month2 == --month1)
    @Test
    public void test6() {
        Assert.assertEquals(1, Cal.cal(2, 1, 2, 2, 2022));
    }

    // numDays = day2 + (daysIn[--month1] - day1);
    @Test
    public void test7() {
        Assert.assertEquals(59, Cal.cal(2, 1, 4, 1, 2022));
    }

    // if (m4 > 0 || m100 == 0 && m400 != 0)
    @Test
    public void test8() {
        Assert.assertEquals(0, Cal.cal(1, 1, 5, 1, -1));
    }

    // if (month2 <= month1)
    @Test
    public void test9() {
        Assert.assertEquals(0, Cal.cal(2, 1, 1, 1, 2020));
    }

    // if (m4 != 0 || m100 == 0 && m400 > 0)
    @Test
    public void test10() {
        Assert.assertEquals(0, Cal.cal(1, 1, 5, 1, -100));
    }
}
