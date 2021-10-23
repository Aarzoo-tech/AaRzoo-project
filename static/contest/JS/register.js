function validation()
{
    var flag=true;
    const input=document.getElementsByTagName("input");
    const s1= document.getElementById("s1");
    s2=document.getElementById("s2");
    s3=document.getElementById("s3");
    s4=document.getElementById("s4");
    if(input[0].value.length==0)
    {
        input[0].style.borderColor="brown";
        flag=false;
        s1.style.color="brown";
        s1.innerHTML="Field cannot leave empty";
    }
    else
    {
        input[0].style.borderColor="white";
        s1.innerHTML="";
    }
    if(input[1].value.length==0)
    {
        input[1].style.borderColor="brown";
        flag=false;
        s2.style.color="brown";
        s2.innerHTML="Field cannot leave empty";
    }
    else
    {
        input[1].style.borderColor="white";
        s2.innerHTML="";
    }
    if(input[2].value.length!=8)
    {
        input[2].style.borderColor="brown";
        flag=false;
        s3.style.color="brown";
        s3.innerHTML="Field cannot leave empty";
    }
    else
    {
        input[2].style.borderColor="white";
        s3.innerHTML="";
    }
    if(input[3].value.length==0)
    {
        input[3].style.borderColor="brown";
        flag=false;
        s4.style.color="brown";
        s4.innerHTML="Field cannot leave empty";
    }
    else
    {
        input[3].style.borderColor="white";
        s4.innerHTML="";
    }
    return flag;
}
function remove_error_msg(e)
{
        if(e.value.length!=0)
            {document.getElementById("s1").innerHTML="";}
        else
            {document.getElementById("s1").innerHTML="Field cannot leave empty";}
        if(e.value.length!=0)
            {document.getElementById("s1").innerHTML="";}
        else
            {document.getElementById("s1").innerHTML="Field cannot leave empty";}
        if(e.value.length!=0)
            {document.getElementById("s1").innerHTML="";}
        else
            {document.getElementById("s1").innerHTML="Field cannot leave empty";}
        if(e.value.length!=0)
            {document.getElementById("s1").innerHTML="";}
        else
            {document.getElementById("s1").innerHTML="Field cannot leave empty";}
}
