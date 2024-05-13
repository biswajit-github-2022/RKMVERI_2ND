    //create class CallbackExample3 for callback() method  
    public class cbex{  
        //main method start  
        public static void main(String args[]) {  
            //function that passes interface name as parameter  
              
            //create a method and pass the interface as parameter  
            callbackMethod(new interfaceX()  
            {  
                //create callMethodX()   
                public String callMethodX()  
                {  
                    return  "It is the first callback";  
                }  
            });  
              
            // create a method and pass the interface as parameter  
            callbackMethod(new interfaceX()  
            {  
                //create callMethodX()   
                public  String  callMethodX() {  
                    return  "It is the second callback";  
                }  
            });  
              
            callbackMethod(() ->  
            {  
                return "It is the third callback";  
            });  
        }  
          
        //define callbackMethod()  
        public static void callbackMethod(interfaceX obj)  
        {     
            //print callback messages  
            System.out.println(obj.callMethodX());  
        }  
        //create an interface  
        public interface interfaceX {  
            public String callMethodX();  
        }  
    }  
