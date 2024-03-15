function display() {
    let age = document.myform.age.value;
    if (age < 0) {
        alert("age must be >0");
        return false;
    }]
        var x = document.myform.email.value;
        var atposition = x.indexOf("@");
        var dotposition = x.lastIndexOf(".");
        if (atposition < 1 || dotposition < atposition + 2 || dotposition + 2 >= x.length) {
            alert("Please enter a valid e-mail address \n atpostion:" + atposition + "\n dotposition:" + dotposition);
            return false;
        }
      

   
    return true;

 }