s/**
 * Created by lizhen on 2017/6/28.
 */
function add()
{
    var add1=Number(document.form1.adder1.value);
    var add2=Number(document.form1.adder2.value);
    var result=add1+add2;
    document.form1.result.value=result;
}