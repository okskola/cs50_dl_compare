#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

// my functions to calculate letters, words
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    float calculation = (0.0588 * letters / words * 100) - (0.296 * sentences / words * 
    100) - 15.8;

    int index = round(calculation);

    if (index < 1)
    {
        printf("Before grade 1.\n");
    }
    else if (index >= 16)
    {
        printf("Grade: 16+.\n");
    }
    else
    {
        printf("Grade: %i.\n", index);
    }
}

int count_letters(string text)

{
    int letters = 0;
    for (int i = 0; i < strlen(text); i++)

        //((text[i] > 65 && text[i] < 90) || (text[i] > 97 && text[i] < 122))
        if (isalpha(text[i]))
        {
            letters++;
        }
    return letters;
}

int count_words(string text)
{
    int words = 0;
    for (int i = 0; i < strlen(text); i++)
        if isspace ((text[i]))
        {
            words++;
            words = words + 1;
        }

    return words;
}

int count_sentences(string text)
{
    int sentences = 0;
    for (int i = 0; i < strlen(text); i++)
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
    return sentences;
}