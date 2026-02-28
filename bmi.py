/*
---------BMI CALCULATOR----------

The program below is a BMI calculator. It computes BMI in both Imperial as well as Metric unit system.
This program takes you weight and height as input and responds with following data:
1. Your BMI calculated as per formula prescribed by WHO.
2. Your weight classification and health risk.
3. Amount of weight to be lost by a person in order to acheive healthy weight.
*/

#include <stdio.h>
#include <math.h>

int main(){
    float w_kg, w_lb, h_cm, h_in, bmi, w_loss, w_nor; char sys_ch;

    // Choosing the system for calulation

    printf("Enter I to continue with Imperial system and M to continue with Metric system: ");
    scanf("%c", &sys_ch);

    // DEFINING IMPERIAL SYSTEM

    if (sys_ch == 'I'){
        
        // Taking user inputs for weight and height
        
        printf("\nEnter your weight in pounds (lb): ");
        scanf("%f", &w_lb);
        printf("\nEnter your height in inches (in): ");
        scanf("%f", &h_in);

        // Calculation of BMI

        bmi = (w_lb * 703)/(h_in * h_in);
        printf("\nYour BMI is: %f", bmi);

        // BMI Classifications and health risks

        if (bmi < 18.5){
            printf("\nClassification: Underweight");
            printf("\nHealth risk: Low");
        }
        else if (18.5 <= bmi && bmi < 25){
            printf("\nClassification: Normal weight");
            printf("\nHealth risk: Average");
        }
        else if (25 <= bmi && bmi < 29.9){
            printf("\nClassification: Overweight");
            printf("\nHealth risk: Mildly increased");
        }
        else if (30 <= bmi && bmi < 34.9){
            printf("\nClassification: Obese Class 1");
            printf("\nHealth risk: Moderate");
        }
        else if (35 <= bmi && bmi < 39.9){
            printf("\nClassification: Obese Class 2");
            printf("\nHealth risk: Severe");
        }
        else if (40 < bmi){
            printf("\nClassification: Obese Class 3");
            printf("\nHealth risk: Very Severe");
        }
        else{
            printf("\nInvalid input.");
        }
        
        // Weight loss calculation

        if (bmi > 25){        
        w_nor = (25 * h_in * h_in)/703;
        w_loss = w_lb - w_nor;
        printf("\nYou need to loose %f pounds", w_loss);
        }
    }
    
        // Defining Metric system
    
        if (sys_ch == 'M'){
        
        // Taking user inputs for weight and height
        
        printf("\nEnter your weight in kg: ");
        scanf("%f", &w_kg);
        printf("\nEnter your height in cm: ");
        scanf("%f", &h_cm);

        // Calculation of BMI

        bmi = (w_kg * 10000)/(h_cm * h_cm);
        printf("\nYour BMI is: %f", bmi);

        // BMI Classifications and health risks

        if (bmi < 18.5){
            printf("\nClassification: Underweight");
            printf("\nHealth risk: Low");
        }
        else if (18.5 <= bmi && bmi < 25){
            printf("\nClassification: Normal weight");
            printf("\nHealth risk: Average");
        }
        else if (25 <= bmi && bmi < 29.9){
            printf("\nClassification: Overweight");
            printf("\nHealth risk: Mildly increased");
        }
        else if (30 <= bmi && bmi < 34.9){
            printf("\nClassification: Obese Class 1");
            printf("\nHealth risk: Moderate");
        }
        else if (35 <= bmi && bmi < 39.9){
            printf("\nClassification: Obese Class 2");
            printf("\nHealth risk: Severe");
        }
        else if (40 < bmi){
            printf("\nClassification: Obese Class 3");
            printf("\nHealth risk: Very Severe");
        }
        else{
            printf("\nInvalid input.");
        }
        
        // Weight loss calculation

        if (bmi > 25){        
        w_nor = (25 * h_cm * h_cm)/10000;
        w_loss = w_kg - w_nor;
        printf("\nYou need to loose %f kg", w_loss);
        }
    }

    return 0;

}
