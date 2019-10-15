# flag_shop
## Points: 300
### Solved by: Vermillion
<br></br>
### Description

`There's a flag shop selling stuff, can you buy a flag? `[Source](store.c)`. Connect with` `nc 2019shell1.picoctf.com 11177.`

### Solve

Open up the source, and we see that the service is a simple store. It offers us 3 options, but the one we're interested in is the second one.

The second one offers fake flags and the real flag. Of course, the real flag costs `100000` dollars, and we only start with `1100`. So how in the world do we get more money? Let's look at the fake flags.

```
if(auction_choice == 1){
    printf("These knockoff Flags cost 900 each, enter desired quantity\n");
    int number_flags = 0;
    fflush(stdin);
    scanf("%d", &number_flags);
    if(number_flags > 0){
        int total_cost = 0;
        total_cost = 900*number_flags;
        printf("\nThe final cost is: %d\n", total_cost);
        if(total_cost <= account_balance){
            account_balance = account_balance - total_cost;
            printf("\nYour current balance after transaction: %d\n\n", account_balance);
        }
        else{
            printf("Not enough funds to complete purchase\n");
        }
    }
}
```

We see that every fake flag costs `900` dollars and it subtracts the total cost from our account balance. But what if `total_cost` is negative? Then we add `total_cost` to our balance, and if `total_cost` is negative enough, then we can get a huge account balance. How do we get a negative `total_cost`?

Notice that `total_cost` is declared as an `int`. This is specifically a *Signed Integer*, which has a range between `-2,147,483,648` to `2,147,483,647`. Signed integers use the first bit to store whether it is negative or positive, `0` indicating positive and `1` indicating negative. What happens if you add `1` to `2,147,483,647` and store the result in a signed integer? Well the first bit goes from `0` to `1`, meaning that the number is now negative! In fact, due to the way [Two's Complement](https://en.wikipedia.org/wiki/Two%27s_complement), the method used to represent negative numbers in binary, works, it actually wraps around to the most negative integer: `-2,147,483,648`. 

This is what is known as an Integer Overflow. We can use this to overflow the `total_cost` variable and increase our account balance. We need a `total_cost` that is a large negative number, but not too large that it also overflows our `account_balance`. `3000000` works nicely as the number of fake flags to buy:

![](/Images/2019/picoCTF/flagshopsolve.PNG)

### Flag:
`picoCTF{m0n3y_bag5_b9f469b5}`
