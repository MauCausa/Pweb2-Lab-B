public class Calculator {
    public static void main(String[] args) throws Exception {
      Scanner sc=new Scanner(System.in);
      System.out.println("Hello, World!");
      
      System.out.println("Ingrese el primer número: ");
      int first=sc.nextInt();
      System.out.println("Ingrese el segundo número: ");
      int second=sc.nextInt();
      System.out.println("¿Qué operación desea realizar?");
      System.out.println("1: suma\n 2: resta\n 3: multiplicación\n 4: división\n 5: módulo\n");
      int operacion=sc.nextInt();
      
      switch(operacion){
        case 1: System.out.println("La suma es: "+add(first,second));
          break;
        case 2: System.out.println("La resta es: "+sub(first,second));
          break;
        case 3: System.out.println("El producto es: "+mul(first,second));
          break;
        case 4: System.out.println(div(first,second));
          break;
        case 5: System.out.println(mod(first,second));
          break;                        
      }
     public int add(int first,int second){
        return first+second;
     }
     public int sub(int first,int second){
        return first-second;
     }
     public int mul(int first,int second){
         return first*second;
     }
     public String div(int first,int second){
         if (second != 0)
         return " " + first/second;
         else 
         return "no se puede dividir";
     }
     public String mod(int first, int second){
         if(second==0)
         return "La operación no se puede realizar porque hay una división entre 0";
         else
         return first%second;
     }
    }
}
