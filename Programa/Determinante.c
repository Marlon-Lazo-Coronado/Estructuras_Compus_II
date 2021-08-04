#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>
#include <pthread.h>
#define MAX 20 //ESTA DEFINICIÓN SE PUEDE ELIMINAR

//ESTRUCTURAS PARA EMPAQUETAR LAS VARIABLES Y PASAR LOS ARGUMENTOS
//SE PUEDE REDUCIR A UNA SOLA ESTRUCTURA
struct params_1 {
    int orden;
    int matriz[MAX][MAX];
};

struct params_2 {
    int orden, fila, columna;
    int matriz[MAX][MAX];
}; 

//DECLARACION DE LAS FUNCIONES
void mostrar_matriz(struct params_1 p);
void mostrar_matriz_2(struct params_2 p);
int *determinante(struct params_1 p);
int *cofactor(struct params_2 q);

//SE TRANSFORMAN LAS FUNCIONES A PARAMETROS GENERICOS
void *cofactor_(void *args){
   struct params_2 q = *((struct params_2*)args);
   return (void*)cofactor(q);
}

void *determinante_(void *args){
   struct params_1 p = *((struct params_1*)args);
   return (void*)determinante(p);
}





//FUNCION PRINCIPAL
int main()
{
   int matriz[MAX][MAX];
   int orden, i, j;

   //SE SOLICITAN LOS DATOS
   printf("Ingresa el orden de la matriz (maximo %d): ", MAX);
   scanf("%d", &orden);
   while (orden < 0 || orden > MAX) {
   	printf("\nEl orden de la matriz no puede negativo no mayor que %d\n", MAX);
   	printf("Ingrese nuevamente el orden de la matriz: ");
      scanf("%d", &orden);
   }

   printf("\nIngrese los elementos de la matriz:\n\n");
   for (i = 0; i < orden; i++) {
      for (j = 0; j < orden; j++) {
         scanf("%d", &matriz[i][j]);
      }
   } 

   //SE PREPARA LA ESTRUCTURA A CALCULAR
   struct params_1 params_x;
   params_x.orden = orden;
   for (i = 0; i < orden; i++) {
      for (j = 0; j < orden; j++) {
         params_x.matriz[i][j] = matriz[i][j];
      }
   }    

   printf("\nMostrando la matriz ingresada:\n");
   mostrar_matriz(params_x);

   printf("\nEl determinante es:   %d", determinante(params_x)[0]);
   getchar();
   getchar();
   return 0;
}

//FUNCION MOSTRAR MATRIZ TIPO 2
void mostrar_matriz(struct params_1 p)
{
	int i, j;
	printf("Orden: %d\n", p.orden);
   for (i = 0; i < p.orden; i++) {
      for (j = 0; j < p.orden; j++) {
      	printf("\t%d", p.matriz[i][j]);
      }
      printf("\n");
   }
}

//FUNCION MOSTRAR MATRIZ TIPO 1
void mostrar_matriz2(struct params_2 p)
{
	int i, j;

	printf("Orden: %d\n", p.orden);
   for (i = 0; i < p.orden; i++) {
      for (j = 0; j < p.orden; j++) {
      	printf("\t%d", p.matriz[i][j]);
      }
      printf("\n");
   }
}


//FUNCION PARA CALCULAR EL DETERMINANTE
int *determinante(struct params_1 p)
{
   //SE RESERVA MEMORIA PARA UN VECTOR DE TAMAÑO 1 TIPO ENTERO
   int *deter = (int*)malloc(1*sizeof(int));
   deter[0] = 0;
   //SE GUARGA LA CANTIDAD DE HILOS
   int MAX_THREADS = p.orden;
   //SE RESERVA MEMORIA EN UN VECTOR DE TAMAÑO MAX_THREADS PARA EL RESULTADO DE LOS HILOS
   void **s = (void*)malloc(MAX_THREADS*sizeof(void));

   //CONDICIÓN DE PARO
   if (p.orden == 1) {
      deter[0] = p.matriz[0][0];
   } else {
      //SE DECLARA LA CANTIDAD DE HILOS
      pthread_t thread[MAX_THREADS];
      //FOR QUE CREA LOS HILOS Y LES PASA EL ARGUMENTO
      for (int j = 0; j < MAX_THREADS; j++){
         //SE RESERVA MEMORIA PARA LAS ESTRUCTURAS MATRICES QUE SE PASAN COMO ARGUMENTO
         struct params_2 *params_22 = (struct params_2 *)malloc(4*sizeof(struct params_2));
         //SE CARGA LA ESTRUCTURA
         params_22[0].orden = p.orden;
         params_22[0].fila = 0.0;
         //SE LE PASA LA COLUMNA A TACHAR A LA FUNCION COFACTOR
         params_22[0].columna = j;
         for (int v = 0; v < p.orden; v++){
             for (int b = 0; b < p.orden; b++){
               params_22[0].matriz[v][b] = p.matriz[v][b];
            }
         }
         //FUNCION QUE CREA LOS HILOS
         pthread_create(&thread[j], NULL, cofactor_, &params_22[0]);
      }               
      //FOR PARA SICRONIZAR LO HILOS Y GUARDAR LOS RESULTADOS DE LAS LOS HILOS EN ELVECTOR S                                                                             
      for (int j = 0; j < MAX_THREADS; j++){
         pthread_join (thread[j], &s[j]);
      }
      //FOR PARA CALCULAR EL DETERMIANANTE
      for (int j = 0; j < MAX_THREADS; j++) {
         deter[0] = deter[0] + p.matriz[0][j] * *((int*)s[j]);;
      }
   }
   return deter;
}

//FUNCION PARA CALCULAR LOS COFACTORES
int *cofactor(struct params_2 q)
{
   //SE RESERVA MEMORIA PARA UN ENTERO
   int *deter = (int*)malloc(1*sizeof(int));
   int x = 0;
   int y = 0;
   //SE CALCULA LA SUBMATRIZ
   struct params_1 params_11;
   params_11.orden = q.orden - 1;
   for (int i = 0; i < q.orden; i++) {
      for (int j = 0; j < q.orden; j++) {
         if (i != q.fila && j != q.columna) {
            params_11.matriz[x][y] = q.matriz[i][j];
            y++;
            if (y >= q.orden - 1) {
               x++;
               y = 0;
            }
         }
      }
   }
   //SE ALTERNAN LOS VALORES DEL DISCRIMINANTE
   deter[0] = pow(-1.0, q.fila + q.columna) * determinante(params_11)[0];
   return deter; 
}