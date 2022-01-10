int reversDigits(int x)
{
    // Handling negative xbers
    bool negativeFlag = false;
    if (x < 0)
    {
        negativeFlag = true;
        x = -x ;
    }
 
    int prev_rev_x = 0, rev_x = 0;
    while (x != 0)
    {
        int curr_digit = x % 10;
 
        rev_x = (rev_x * 10) + curr_digit;
 
        // checking if the reverse overflowed or not.
        // The values of (rev_x - curr_digit)/10 and
        // prev_rev_x must be same if there was no
        // problem.
        if ((rev_x - curr_digit) /
               10 != prev_rev_x)
        {
            cout << "WARNING OVERFLOWED!!!"
                 << endl;
            return 0;
        }
 
        prev_rev_x = rev_x;
        x = x / 10;
    }
 
    return (negativeFlag == true) ?
                         -rev_x : rev_x;
}